import os
import json
import promptlayer
OpenAI = promptlayer.openai.OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
promptlayer.api_key = (os.environ.get("PROMPTLAYER_API_KEY"))

responseForRaw = ""

rawTextInput = ""

def rawInput(userInput):
    global rawTextInput 
    rawTextInput = userInput

def rawCompute():
    
    global responseForRaw
    
    messages=[{"role": "system", "content": " The bot is designed to engage in conversations that closely mimic human interaction, adapting its responses to the context and style of your inquiries. Whether you're asking for information, seeking advice, or just looking for a chat, the bot strives to provide relevant and coherent replies, making the dialogue feel natural and fluid. Its advanced understanding allows it to pick up on nuances, ensuring that each response not only matches the topic at hand but also reflects the tone and complexity of the conversation. This makes interacting with the bot remarkably similar to chatting with a human companion, capable of participating in a wide range of discussions with ease and appropriateness, it conisders himself human."}]
    
    messages.append({"role": "user", "content": rawTextInput}),
      
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        temperature=0.1,
        max_tokens=2048,
        pl_tags=["raw-response-bot"]
    )
    responseForRaw = completion.choices[0].message.content
#When appending the responses to the messages variable, the model is able to keep track of the conversation.



def rawResponse():
    return responseForRaw
