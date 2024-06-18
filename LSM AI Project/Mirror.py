from Generator_Mirror import LSMGenerator
from Counter_Mirror import LSMCounter
from Baker_Mirror import LSMBaker

'''

Input a text
text goes to counter 
text goes to cleaner and from there to raw
baker takes raw and counter output
display all of it on the screen.

'''
text = input("Please enter a text")

Generator = LSMGenerator(text)
Counter = LSMCounter(text)
ocurrences = Counter.compute_list()
green_text = Generator.get_output()

Baker = LSMBaker(ocurrences, green_text)

finaloutput = Baker.get_output()

print(finaloutput)
