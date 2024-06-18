import os
# Enables the program to be able to comunicate with the operating system (to be able to call the api key)
import json
#This is used so in the future a function is able to communicate with the API in json format.
import promptlayer
#This enables the promptlayer API to keep track of the requests and usage of the OpenAI API
OpenAI = promptlayer.openai.OpenAI
# Importing the OpenAI library from OpenAI in order to be able to use the API, this is done on top of the promptlayer library.

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
#Calling the secret OPENAI_API_KEY from my system enviroment, this is not necesary, but this approach is more secure. 
promptlayer.api_key = (os.environ.get("PROMPTLAYER_API_KEY"))


messages=[{"role": "system", "content": "This GPT, LSM Bot , is specialized in performing Linguistic Style Matching (LSM) on texts through a structured three-step process. Upon receiving a text for LSM, LSM Bot 3 first counts and analyzes personal pronouns, impersonal pronouns, auxiliary verbs, negations, conjunctions, adverbs, articles, and prepositions, along with the total word count, sharing these metrics with the user. In the next step, after the user prompts with Next step, LSM Bot  calculates the average occurrence of these linguistic elements relative to the text size and shares the insights. In the final step, when the user either makes final adjustments or simply prompts Next step, LSM Bot  crafts a response. This response adheres closely to the original text's linguistic style, specifically matching the average occurrence of personal pronouns, impersonal pronouns, auxiliary verbs, negations, conjunctions, adverbs, articles, and prepositions. The emphasis is on matching these metrics closely, rather than on matching the text's size or word count, ensuring the response mirrors the original text's style accurately."}]
#Determining the role of the assistant 
#It is declared outside the loop so the GPT does not receive the same instruction multiple times.

with open(r'C:\Users\andre\OneDrive\Programming\LSM_Tests\OpenAI_Learning_Program\OpenAI_API_Tests\testCode.py', mode="r", encoding="utf-8") as theCode:
  fixIt = theCode.read()
#Function to open, read, copy and close a python code in the same directory.

print(fixIt)

response = ""
#In this variable the model's answer will be registered and printed later.

while True:

  userInput = input("André: ")
  #Declaring the variable "userInput" to be able to communicate dinamically with the model in the terminal.
  
  if userInput.lower() in ["check this code", "use my code"]:
    messages.append({"role": "user", "content": "please fix this code: " + fixIt}),
    #simple function to trigger a code correction tool
  else:
    messages.append({"role": "user", "content": userInput}),
    #Asigning a prompt from the user.  
      
  completion = client.chat.completions.create(
    #Using the chat completition API, to be able to call a pretrained model.
    model="gpt-3.5-turbo-0125",
    #Selection of the model, this can be replaced to make it more powerfull at a higher token cost.
    messages=messages,
    temperature=0.5,
    #Temperature sets the amount of randomization the model could generate, a higher value results on more creative but inaccurate results, and viceversa.
    max_tokens=512,
    #Enables a limit on the amount of tokens that can be used by the model, that stuff doesn't grow on trees!
    pl_tags=["getting-started"]
    #This tag serves as a bookmark for the promptlayer website to facilitate the location of prompts.
  )
  response = completion.choices[0].message
  messages.append(response)
  #When appending the responses to the messages variable, the model is able to keep track of the conversation.
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

