import os
import json
import promptlayer
OpenAI = promptlayer.openai.OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
promptlayer.api_key = (os.environ.get("PROMPTLAYER_API_KEY"))

response = ""

userText = ""

def cleanerInput(userInput):
    global userText 
    userText = userInput

def cleanerCompute():
    
    global response
    
    messages=[{"role": "system", "content": "The bot enhances any text input by correcting spelling, grammar, punctuation, and formatting while strictly preserving original content. It fixes errors without adding information or altering intent, ensuring readability and adherence to language-specific rules. Ambiguous cases are flagged for review to maintain accuracy. Designed for multiple languages, the bot applies appropriate corrections for each. A feedback feature allows users to review changes, prioritizing user control and clarity. Privacy is paramount, with no text storage beyond processing. This streamlined approach ensures efficient, secure text improvement, focusing on form and precision without compromising the text's essence."}]
    
    messages.append({"role": "user", "content": userText}),
      
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        temperature=0.1,
        max_tokens=2048,
        pl_tags=["cleaner-bot"]
    )
    response = completion.choices[0].message.content
#When appending the responses to the messages variable, the model is able to keep track of the conversation.



def cleanerResponse():
    return response

