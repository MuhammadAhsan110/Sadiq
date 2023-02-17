# #making a very basic chatbot using dictionaries in python
# #questions and answers

#trying to integrate openAI to the chatbot


import openai
import os

# Configure the OpenAI API client
openai.api_key = os.environ["OPENAI_API_KEY"]

# Function to ask a question using the OpenAI API
def ask_openai(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"I have a question: {question}\nAnswer:",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response.choices[0].text.strip()
    return answer

# Chatbot responses
qna = {
    "hi":'hey!',
    "how are you?":"I am fine, how may I help you?",
    "what is your name?":"My name is Ahsan's Chatbot",
    "Thank you":"No problem!",
    "Bye":"Goodbye, have a good day!",
}

# Main loop
while True:
    question = input()

    if question == 'quit':
        break

    elif question in qna:
        print(qna[question])

    else:
        answer = ask_openai(question)
        if answer:
            print(answer)
        else:
            print("I'm sorry, I don't understand. Can you please rephrase your question?")

