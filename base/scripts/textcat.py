import spacy
import classy_classification

data = ["crime", "politics", "sports", "religion", "entertainment"]

with open('english.txt', 'r', encoding='utf-8') as file:
    english_text = file.readlines()
    for line in english_text:
        
        data= data
        nlp = spacy.blank("en")
        nlp.add_pipe(
        "text_categorizer",
        config={
        "data": data,
        "model": "facebook/bart-large-mnli",
        "cat_type": "zero",
        "device": "cpu",
        # "multi_label": True,
        })
        print(line)
        #get the category of the text Allow multiple true classes
        print(nlp(line)._.cats)
            
       
            
            
    
    

        

       

