import os
import csv
import promptlayer

OpenAI = promptlayer.openai.OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
promptlayer.api_key = os.environ.get("PROMPTLAYER_API_KEY")

class LSMBaker():
    #Tomar el input de LSMGenerator
    def __init__(self, percent_list, green_text):
        self.scores = percent_list
        self.pinaac = []
        for item in ["Ppron.csv", "Ipron.csv", "Auxverb.csv", "Negations.csv", "Advrb.csv", "Conj.csv"]:
            file_path = os.path.join("WordLists", item)
            self.word_list = []
            with open(file_path, encoding="utf-8") as data:
                csv_data = csv.reader(data)
                self.word_list = list(csv_data)
            
                self.word_list = self.word_list[0]
                
            self.pinaac.append(self.word_list)
        
        pplist, iplist, auxlist, nelist, adlist, colist = self.pinaac
        ppercent, ipercent, aupercent, nepercent, adpercent, copercent = self.scores
        
        #Tomar las listas de palabras
        #Igual que en el counter pero asignando una lista a cada uno simplemente.
        
        #Tomar el porcentage de cada una de ellas 
                
        #Dentro de el prompt asignar el valor correspondiente
        system_message = (
            f"I want you to rewrite the inputted text maintaining its essence, and you will have to generate a response by also keeping in mind the following values. Personal Pronouns: {pplist}, Impersonal Pronouns: {iplist}, Auxiliary Verbs: {auxlist}, Negations: {nelist}, Adverbs: {adlist}, Conjunctions: {colist}. The response should follow these percentages respectively: {ppercent}%, {ipercent}%, {aupercent}%, {nepercent}%, {adpercent}%, {copercent}%. do not generate a response unless it follows these rules."
        )
        
        self.messages = [{"role": "system", "content": system_message}]
        self.messages.append({"role": "user", "content": green_text})

        self.completion = client.chat.completions.create(
            model="gpt-4o",
            messages=self.messages,  
            temperature=0.9,
            max_tokens=2048,
            pl_tags=["cleaner-bot"]
        )
        
        self.baked_output = self.completion.choices[0].message.content 
        
    def get_output(self):
        return self.baked_output
    #Generar una respuesta valida
    
    
    #Medir el LSM total  <---- Esto hacerlo en el codigo final para que sea mas coherente.
        #Volver a pasar datos por el LSMCounter y simplemente comparar los resultados 