from counter2 import compute_counts, count_occurrences, counter_input
from cleaner import cleanerInput, cleanerCompute, cleanerResponse
from raw import rawInput, rawCompute, rawResponse

text = "For it, so but it, how did it evolve to what it is now? Was it a vision? Was it a slow sort of a gradual increase in numbers? And yeah, I mean, it's about as slow as it gets. Uh, I mean, I can so like when I was a young teenager, I was getting no views, had no money, had no equipment. So for the most part, it was just like I was just trying to scrounge money so I could buy equipment because I was using my brother's old laptop. And so like my first couple hundred videos, I didn't have a microphone, like imagine just like crackly terrible voice. Um, and so once I got monetized, I saved up for a few months like I told you, I bought a microphone. I didn't just give you a mile-high history, and I saved up for like six months. I mean, I was just doing video game videos, uh, and they were terrible, but I saved up. I got a real computer, so now I can actually record the video game at high quality. I have a microphone. I'm like 15, and I just kept going and going. Um, trying to figure out like what are some of like the hot spots like I, essentially, up until 18, I had been doing YouTube pretty religiously, but I was making no money. Like this is kind of the turning point was when I graduated from high school, and my whole life, I was like, I want to be making enough money by the time I graduated to do this full-time, and I wasn't. I was only making a couple hundred bucks a month."

cleanerInput(text)
cleanerCompute() 
clean = cleanerResponse()
rawInput(clean)
rawCompute()
raw = rawResponse()
counter_input(clean)
count = compute_counts()

print(count)
print("\n")
print(clean)
print("\n")
print(raw) 
print("\n")