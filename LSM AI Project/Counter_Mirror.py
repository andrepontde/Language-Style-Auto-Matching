import csv
import os

class LSMCounter():
    def __init__(self, text):
        self.input_text = text
        
    def get_list(self, list_name):
        file_path = os.path.join("WordLists", list_name)
        self.word_list = []
        with open(file_path, encoding="utf-8") as data:
            csv_data = csv.reader(data)
            self.word_list = list(csv_data)
            
            self.word_list = self.word_list[0]
        return self.word_list
    
    def count_occurrences(self, text, word_list):
        # Creates a dictionary with the count of each word in word_list found in the text
        word_counts = {word: text.split().count(word) for word in word_list}
        # Filters the dictionary to keep only words with a count greater than 0
        return {word: count for word, count in word_counts.items() if count > 0}
    
    def compute_list(self):
        self.ocurrences = []
        for item in ["Ppron.csv", "Ipron.csv", "Auxverb.csv", "Negations.csv", "Advrb.csv", "Conj.csv"]:
            word_list = self.get_list(item)
            ocations = self.count_occurrences(self.input_text, word_list)
            avg = sum(ocations.values()) / len(self.input_text.split()) if len(self.input_text.split()) else 0
            self.ocurrences.append(avg)
            
        return self.ocurrences
            