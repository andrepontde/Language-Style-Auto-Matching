import os
import promptlayer

OpenAI = promptlayer.openai.OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
promptlayer.api_key = os.environ.get("PROMPTLAYER_API_KEY")

class LSMGenerator():
    def __init__(self, user_text):
        self.cleaner_message = [{"role": "system", "content": "The bot enhances any text input by correcting spelling, grammar, punctuation, and formatting while strictly preserving original content. It fixes errors without adding information or altering intent, ensuring readability and adherence to language-specific rules. Ambiguous cases are flagged for review to maintain accuracy. Designed for multiple languages, the bot applies appropriate corrections for each. A feedback feature allows users to review changes, prioritizing user control and clarity. Privacy is paramount, with no text storage beyond processing. This streamlined approach ensures efficient, secure text improvement, focusing on form and precision without compromising the text's essence."}]
        self.cleaner_message.append({"role": "user", "content": user_text})

        self.completion = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=self.cleaner_message,  
            temperature=0.1,
            max_tokens=2048,
            pl_tags=["cleaner-bot"]
        )
    
        self.clean_output = self.completion.choices[0].message.content 
        
        self.green_message = [{"role": "system", "content": "The bot is designed to engage in conversations that closely mimic human interaction, adapting its responses to the context and style of your inquiries. Whether you're asking for information, seeking advice, or just looking for a chat, the bot strives to provide relevant and coherent replies, making the dialogue feel natural and fluid. Its advanced understanding allows it to pick up on nuances, ensuring that each response not only matches the topic at hand but also reflects the tone and complexity of the conversation. This makes interacting with the bot remarkably similar to chatting with a human companion, capable of participating in a wide range of discussions with ease and appropriateness, it considers himself human."}]
        self.green_message.append({"role": "user", "content": self.clean_output})

        self.completion = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=self.green_message,
            temperature=0.1,
            max_tokens=2048,
            pl_tags=["Green-response-bot"]
        )
        
        self.green_output = self.completion.choices[0].message.content  

    def get_output(self):
        return self.green_output

# torero = LSMGenerator("For it, so but it, how did it evolve to what it is now? Was it a vision? Was it a slow sort of a gradual increase in numbers? And yeah, I mean, it's about as slow as it gets. Uh, I mean, I can so like when I was a young teenager, I was getting no views, had no money, had no equipment. So for the most part, it was just like I was just trying to scrounge money so I could buy equipment because I was using my brother's old laptop. And so like my first couple hundred videos, I didn't have a microphone, like imagine just like crackly terrible voice. Um, and so once I got monetized, I saved up for a few months like I told you, I bought a microphone. I didn't just give you a mile-high history, and I saved up for like six months. I mean, I was just doing video game videos, uh, and they were terrible, but I saved up. I got a real computer, so now I can actually record the video game at high quality. I have a microphone. I'm like 15, and I just kept going and going. Um, trying to figure out like what are some of like the hot spots like I, essentially, up until 18, I had been doing YouTube pretty religiously, but I was making no money. Like this is kind of the turning point was when I graduated from high school, and my whole life, I was like, I want to be making enough money by the time I graduated to do this full-time, and I wasn't. I was only making a couple hundred bucks a month.")

# print(torero.get_output())