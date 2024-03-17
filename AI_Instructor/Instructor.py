import openai

# Set your OpenAI API key
api_key = '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'
openai.api_key = api_key


def showcontent(topic):
# Example prompt
 prompt = f"Tell me about this ${topic} in detailed manner"

# Call the API
 response = openai.Completion.create(
  engine="gpt-3.5-turbo-instruct",
  prompt=prompt,
  max_tokens=50
 )

# Print the translated text
 return(response.choices[0].text.strip())


def askquestion(topic):
# Example prompt
 prompt = f"ask a question from this ${topic} ?"

# Call the API
 response = openai.Completion.create(
  engine="gpt-3.5-turbo-instruct",
  prompt=prompt,
  max_tokens=50
 )

# Print the translated text
 return(response.choices[0].text.strip())