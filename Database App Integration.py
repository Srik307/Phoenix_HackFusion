#Importing necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Flash application instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Defining the User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(50), nullable=False)
    subtopic = db.Column(db.String(50), nullable=False)
    periods = db.Column(db.String(50), nullable=False)

def create_instance_table(user_id):
    table_name = f'user_instance_{user_id}'
    with app.app_context():
        db.engine.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject TEXT,
                topic TEXT,
                subtopic TEXT,
                periods TEXT
            )
        ''')


@app.route('/add_user', methods=['POST'])
def add_user():
    subject = request.form['subject']
    topic = request.form['topic']
    subtopic = request.form['subtopic']
    periods = request.form['periods']

    new_user = User(subject=subject, topic=topic, subtopic=subtopic, periods=periods)
    db.session.add(new_user)
    db.session.commit()

    # Creating new instance table and insert data with modifications
    create_instance_table(new_user.id)
    insert_data_into_instance_table(new_user.id)

    return 'User added successfully'

def insert_data_into_instance_table(user_id):
    # Fetching data from main table
    main_table_data = User.query.filter_by(id=user_id).first()

    # Modifying data slightly
    modified_periods = ((main_table_data.periods*40)*100)/1.5  #To find time taken to complete of the user using efficiency factor

    # Inserting modified data into instance table
    table_name = f'user_instance_{user_id}'
    with app.app_context():
        db.engine.execute(f'''
            INSERT INTO {table_name} (subject, topic, subtopic, periods)
            VALUES (?, ?, ?, ?)
            ''', (main_table_data.subject, main_table_data.topic, main_table_data.subtopic, modified_periods))

if __name__ == '_main_':
    app.run(debug=True)

