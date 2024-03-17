from flask import Flask, render_template, request

app = Flask(__name__)

# Define the questions for each aspect
learning_questions = [
    "How comfortable are you with using visual aids such as diagrams, charts, and graphs when studying for a test?",
    "When learning a new concept, how do you feel about watching instructional videos or demonstrations?",
    "How comfortable are you with visualizing images or diagrams related to the content to remember information?",
    "When reviewing study materials, how comfortable are you with using color-coded notes, highlighters, or visual organizers?",
    "How comfortable are you with sketching out possible solutions or visualizing complex problems?",
    "How comfortable are you with learning through listening, such as listening to recorded lectures or audio materials?",
    "When receiving instructions for a new task or assignment, how comfortable are you with verbal explanations or demonstrations?",
    "How comfortable are you with repeating information out loud or discussing it with others to retain it?",
    "When studying for an exam, how comfortable are you with listening to group discussions or study sessions?",
    "How comfortable are you with listening to verbal feedback or engaging in verbal discussions to understand concepts?",
    "How comfortable are you with reading written material, such as textbooks or notes, to understand new concepts?",
    "When reviewing for a test, how comfortable are you with writing out key points or creating flashcards?",
    "How comfortable are you with writing out notes or creating summaries of the material you've learned?",
    "When faced with a problem or challenge, how comfortable are you with writing out the problem and analyzing it step by step?",
    "How comfortable are you with consulting written resources or reading about similar problems to solve challenges?",
    "How comfortable are you with using mnemonic devices or creating written lists to remember information?",
    "When working on group projects, how comfortable are you with contributing written reports or documents?",
    "How comfortable are you with writing out explanations or instructions for others to understand?",
    "When presenting information, how comfortable are you with creating written outlines or slides?",
    "How comfortable are you with reading aloud or delivering verbal presentations to others?",
    "When studying, how comfortable are you with organizing information into written categories or hierarchies?",
    "How comfortable are you with engaging in verbal discussions or debates to explore new ideas or concepts?",
    "When reviewing for a test, how comfortable are you with explaining concepts or teaching others?",
    "How comfortable are you with reading written instructions or guidelines to complete tasks or assignments?",
    "When faced with a complex problem, how comfortable are you with seeking out written resources or references for solutions?",
    "How comfortable are you with writing out plans or outlines to organize your thoughts before starting a task?",
    "When learning new vocabulary or terminology, how comfortable are you with writing out definitions or creating flashcards?",
    "How comfortable are you with reading written passages or articles to understand complex topics?",
    "How comfortable are you with writing out explanations or answers in response to questions or prompts?",
    "When studying, how comfortable are you with highlighting important information or annotating texts?"
]

processing_speed_questions = [
    "How comfortable are you with quickly comprehending written instructions or directions?",
    "When presented with new information, how comfortable are you with processing it rapidly?",
    "How comfortable are you with making decisions quickly, even under pressure?",
    "When faced with a complex problem, how comfortable are you with breaking it down into smaller, manageable parts?",
    "How comfortable are you with multitasking, handling multiple tasks simultaneously?",
    "How comfortable are you with quickly identifying patterns or trends in data or information?",
    "How comfortable are you with solving puzzles or riddles within a short timeframe?",
    "When given a task, how comfortable are you with prioritizing and organizing your approach to complete it efficiently?",
    "How comfortable are you with responding promptly to unexpected changes or challenges?",
    "How comfortable are you with processing information presented in various formats (text, visual, auditory)?",
    "When reading, how comfortable are you with scanning text quickly to extract key information?",
    "How comfortable are you with mentally calculating numbers or solving math problems swiftly?",
    "When participating in discussions or meetings, how comfortable are you with quickly grasping the main points and contributing ideas?",
    "How comfortable are you with rapidly adapting to new software or technology tools?",
    "How comfortable are you with efficiently managing your time to meet deadlines or complete tasks within a given timeframe?",
    "How comfortable are you with quickly recalling information from memory when needed?",
    "How comfortable are you with processing and responding to verbal instructions or commands promptly?",
    "When presented with a set of data, how comfortable are you with analyzing it quickly to draw conclusions or make recommendations?",
    "How comfortable are you with rapidly learning new skills or techniques?",
    "How comfortable are you with quickly adjusting your strategy or approach when faced with unexpected obstacles?",
    "How comfortable are you with processing information in fast-paced environments?",
    "How comfortable are you with accurately interpreting and responding to non-verbal cues or signals in real-time?",
    "How comfortable are you with quickly adapting to changes in plans or circumstances?",
    "How comfortable are you with efficiently filtering and prioritizing incoming information or tasks?",
    "How comfortable are you with rapidly synthesizing information from multiple sources to form a coherent understanding?",
    "How comfortable are you with quickly identifying errors or inconsistencies in data or information?",
    "How comfortable are you with rapidly generating ideas or solutions to problems?",
    "How comfortable are you with processing and responding to feedback or criticism constructively and promptly?",
    "How comfortable are you with efficiently managing and organizing large amounts of information or resources?",
    "How comfortable are you with quickly learning and using new vocabulary or terminology in context?"
]

memory_recall_questions = [
    "How comfortable are you with recalling what you had for breakfast yesterday?",
    "Rate your comfort level in recalling the names of your childhood friends.",
    "When asked about the capital cities of countries, how comfortable are you with recalling them?",
    "How confident are you in recalling the plot of the last movie you watched?",
    "Rate your comfort level in recalling the main characters of your favorite book.",
    "How comfortable are you in recalling the items you bought during your last grocery shopping trip?",
    "When recalling song lyrics, how comfortable are you?",
    "How confident are you in recalling your best friend's phone number?",
    "Rate your comfort level in recalling the main events of your last birthday celebration.",
    "How comfortable are you in recalling the formulas you learned in your last math class?",
    "Rate your comfort level in recalling the names of the countries you've visited.",
    "How confident are you in recalling the main historical events you learned in your last history class?",
    "Rate your comfort level in recalling the names of your high school teachers.",
    "How comfortable are you in recalling the ingredients of your favorite dish?",
    "Rate your comfort level in recalling the last conversation you had with a family member.",
    "How confident are you in recalling what you wore to your last job interview?",
    "Rate your comfort level in recalling the last five movies you watched in a theater.",
    "How comfortable are you in recalling the names of all U.S. presidents in order?",
    "Rate your comfort level in recalling the main points of the last article you read online.",
    "How confident are you in recalling the main points of the last TED talk you watched?",
    "Rate your comfort level in recalling your current home address.",
    "How comfortable are you in recalling the last time you visited a museum or art gallery?",
    "Rate your comfort level in recalling the names and birthdays of your immediate family members.",
    "How confident are you in recalling the events of your last vacation?",
    "Rate your comfort level in recalling what you learned in your last science class.",
    "How comfortable are you in recalling the names of all your cousins?",
    "Rate your comfort level in recalling the color of the first car you owned.",
    "How confident are you in recalling the last five items you added to your to-do list?",
    "Rate your comfort level in recalling what you cooked for dinner last night.",
    "How comfortable are you in recalling the color of the shirt you wore two days ago?"
]


attention_span_questions = [
    "How comfortable are you with maintaining focus on a single task for an extended period?",
    "Rate your comfort level in staying attentive during lectures or presentations.",
    "When reading a book or article, how comfortable are you with sustaining your focus?",
    "How confident are you in staying attentive during conversations with others?",
    "Rate your comfort level in staying focused while working on complex tasks.",
    "How comfortable are you with avoiding distractions while studying or working?",
    "Rate your comfort level in staying engaged during meetings or group discussions.",
    "How confident are you in maintaining concentration in noisy or crowded environments?",
    "Rate your comfort level in staying focused while using electronic devices (e.g., smartphones, computers).",
    "How comfortable are you with resisting the urge to check social media or email while working?",
    "Rate your comfort level in staying attentive during repetitive or monotonous tasks.",
    "How confident are you in maintaining focus when under time pressure?",
    "Rate your comfort level in staying attentive during long periods of reading or writing.",
    "How comfortable are you with staying focused during physical activities or exercise?",
    "Rate your comfort level in staying engaged during online classes or webinars.",
    "How confident are you in staying attentive during long drives or commutes?",
    "Rate your comfort level in staying focused when faced with unexpected interruptions or disruptions.",
    "How comfortable are you with maintaining focus while completing tasks that require attention to detail?",
    "Rate your comfort level in staying attentive during phone calls or video conferences.",
    "How confident are you in staying focused during boring or uninteresting activities?",
    "Rate your comfort level in staying engaged during problem-solving or critical thinking tasks.",
    "How comfortable are you with avoiding multitasking and focusing on one task at a time?",
    "Rate your comfort level in staying focused during periods of stress or anxiety.",
    "How confident are you in staying attentive during long periods of listening, such as during podcasts or audiobooks?",
    "Rate your comfort level in staying focused during tasks that require creativity or imagination.",
    "How comfortable are you with maintaining concentration during tasks that involve repetitive movements or actions?",
    "Rate your comfort level in staying engaged during brainstorming or idea generation sessions.",
    "How confident are you in staying focused during tasks that require sustained mental effort?",
    "Rate your comfort level in staying attentive during training sessions or workshops.",
    "How comfortable are you with staying focused during periods of boredom or monotony?"
]

@app.route('/')
def index():
    return render_template('index.html',learning_questions=learning_questions,memory_recall_questions=memory_recall_questions,attention_span_questions=attention_span_questions,processing_speed_questions=processing_speed_questions)

@app.route('/result', methods=['POST'])
def result():
    learning_answers = [request.form.get(f'learning_q{i}', '') for i in range(1, 31)]
    print(learning_answers)

    processing_answers = [request.form.get(f'processing_q{i}', '') for i in range(1, 31)]
   
    memory_answers = [request.form.get(f'memory_q{i}', '') for i in range(1, 31)]

    attention_answers = [request.form.get(f'attention_q{i}', '') for i in range(1, 31)]

  
    learning_result = analyze_learning_style(learning_answers)
    processing_result = analyze_processing_speed(processing_answers)
    memory_result = analyze_memory_recall(memory_answers)
    print(memory_result)
    attention_result = analyze_attention_span(attention_answers)


    efficiency_comparison = calculate_combined_efficiency(memory_result, attention_result, processing_result)

    return render_template('result.html', learning_result=learning_result, processing_result=processing_result, memory_result=memory_result, attention_result=attention_result, efficiency_comparison=efficiency_comparison)


def analyze_learning_style(answers):
    print(answers)
    visual_count = answers.count('a') + answers.count('b')
    auditory_count = answers.count('c')
    read_write_count = answers.count('d') + answers.count('e')
    
    if visual_count > auditory_count and visual_count > read_write_count:
        return "Visual learner"
    elif auditory_count > visual_count and auditory_count > read_write_count:
        return "Auditory learner"
    else:
        return "Read/Write learner"


def analyze_processing_speed(answers):
    response_values = {
        "a": 5,
        "b": 4,
        "c": 3,
        "d": 2,
        "e": 1
    }

    question_scores = {}

    for i, answer in enumerate(answers, start=1):
        score = response_values.get(answer, 0)
        question_scores[f"Question {i}"] = score

    total_score = sum(question_scores.values())
    num_questions = len(question_scores)
    average_score = total_score / num_questions

    return  average_score


def analyze_memory_recall(answers):
    print(answers)
    response_values = {
        "a": 5,
        "b": 4,
        "c": 3,
        "d": 2,
        "e": 1
    }

    question_scores = {}

    for i, answer in enumerate(answers, start=1):
        score = response_values.get(answer, 0)
        question_scores[f"Question {i}"] = score

    total_score = sum(question_scores.values())
    num_questions = len(question_scores)
    average_score = total_score / num_questions

    return  average_score


def analyze_attention_span(answers):
    response_values = {
        "a": 5,
        "b": 4,
        "c": 3,
        "d": 2,
        "e": 1
    }

    question_scores = {}

    for i, response in enumerate(answers, start=1):
        score = response_values.get(response, 0)
        question_scores[f"Question {i}"] = score

    total_score = sum(question_scores.values())
    num_questions = len(question_scores)
    average_score = total_score / num_questions

    return  average_score
def bound_efficiency_score(score):
    return max(0, min(score, 2))

def calculate_combined_efficiency(memory_efficiency, attention_efficiency, processing_efficiency):
    combined_efficiency = (memory_efficiency + attention_efficiency + processing_efficiency) / 3
    bounded_combined_efficiency = bound_efficiency_score(combined_efficiency)
    return bounded_combined_efficiency

if __name__ == '__main__':
    app.run(debug=True)
