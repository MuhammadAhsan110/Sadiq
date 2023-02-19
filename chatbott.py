 #making a very basic chatbot using dictionaries in python
 #questions and answers

#trying to integrate openAI to the chatbot


import openai
import os



# Configure the OpenAI API client


# Function to ask a question using the OpenAI API
model_engine = "text-davinci-003"
def ask_openai(question):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=question,
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

if __name__=="__main__":
    apikey=input("Entery your openAPI key: ")
    #openai.api_key =  #os.environ["OPENAI_API_KEY"]
    openai.api_key=apikey
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

