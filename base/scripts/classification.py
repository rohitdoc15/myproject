import numpy as np
from transformers import pipeline
import os
import sys
import django
import datetime
from googletrans import Translator
#import django models 
sys.path.append('/home/rohit/project/myproject')
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
django.setup()
from base.models import Item,tag,Title,Channel

classifier = pipeline("zero-shot-classification",model="facebook/bart-large-mnli")

#get title from database of today's date
today = datetime.date.today()
today = today.strftime("%Y-%m-%d")
titles = Title.objects.filter(date = today)
#filter titles with no tags
titles = titles.filter(tags__isnull=True)
filtered_labels =[]




for i in titles:

    #get name of title
    name = i.name
    tit = i.tit
    text = name + tit
    print(text)




    try:
    #  translate i to english 
        translator = Translator()
        english_text = translator.translate(text, dest='en').text



      
         
        

            
        
        sequence_to_classify = english_text

        candidate_labels = ['war','politics', 'india','cooking', 'crime', 'entertainment' ,'sports','international','religion', 'terror','pakistan','modi' ,'china']
        result = classifier(sequence_to_classify, candidate_labels,  multi_label=True)
        threshold = 0.8
        filtered_labels = [label for label, score in zip(result['labels'], result['scores']) if score > threshold]
        print(f"{english_text}: {len(filtered_labels)}")
        #save filtered labels to database in Title model tags field
        for j in filtered_labels:

            tag_obj,_  = tag.objects.get_or_create(name=j)
            i.tags.add(tag_obj)
            # filltered_labels is null then save it as 'other'
            

        i.save()


        
        
    except:
        print('error in ', i)

    #if filtered_labels is null then save it as 'other'
    if len(filtered_labels) == 0:
        tag_obj,_  = tag.objects.get_or_create(name='other')
        i.tags.add(tag_obj)
        i.save()

