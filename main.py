from openai import OpenAI
# Importing the OpenAI library from OpenAI in order to be able to use the API
import os
# Enables the program to be able to comunicate with the operating system (to be able to call the api key)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
#Calling the secret OPENAI_API_KEY from my system enviroment, this is not necesary, but this approach is more secure. 


messages=[{"role": "system", "content": "You are an experienced psychologist, familiar with the work from Sigmun Freud."}]
#Determining the role of the assistant 
#It is declared outside the loop so the GPT does not receive the same instruction multiple times.


response = ""
#In this variable the model's answer will be registered and printed later.

while True:

  userInput = input("André: ")
  #Declaring the variable "userInput" to be able to communicate dinamically with the model in the terminal.
  messages.append({"role": "user", "content": userInput}),
  #Asigning a prompt from the user.
  
  completion = client.chat.completions.create(
    #Using the chat completition API, to be able to call a pretrained model.
    model="gpt-3.5-turbo-0125",
    #Selection of the model, this can be replaced to make it more powerfull at a higher token cost.
    messages=messages,
    temperature=0.5,
    #Temperature sets the amount of randomization the model could generate, a higher value results on more creative but inaccurate results, and viceversa.
    max_tokens=32
    #Enables a limit on the amount of tokens that can be used by the model, that stuff doesn't grow on trees!
  )
  
  response = completion.choices[0].message
  messages.append(response)
  print(response)
  #Prints only the response, and declares all of the variables used as well.



#The following code is an unsuccesfull attempt to call the streaming function ->



# from openai import OpenAI

# client = OpenAI()

# stream = client.chat.completions.create(
#     model="gpt-4",
#     messages=[{"role": "user", "content": "Say this is a test"}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")

