import easyocr
from PIL import Image
import os
import sys
import django
from googleapiclient.discovery import build


#import django models
sys.path.append('/home/rohit/project/myproject')
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
django.setup()
from base.models import Item,tag,Title,Channel

# os.chdir('/home/rohit/project/myproject/scripts')
reader = easyocr.Reader(['en', 'hi'], gpu=False )

#api key
API_KEY = 'AIzaSyDzQngwEKSXznBCvRoURIXs4-WZeps4uHA'

def ocr(channel, channel_id):
    directory = "base/scripts/channels/"+channel+"/thumb"
    
     

    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            path = os.path.join(directory, filename)
            image = Image.open(path)
            
            id = filename[-15:-4]

            youtube = build('youtube', 'v3', developerKey=API_KEY)
            #get video title from youtube api with given id
            request = youtube.videos().list(
                part="snippet",
                id=id
            )   
            response = request.execute()
            title = response['items'][0]['snippet']['title']
            #save title in database
            


            
            #if id in database then skip
            if Title.objects.filter(v_id = id).exists():
                print('already exists')
                continue    
            

        result = reader.readtext(image, detail=0,paragraph=True,min_size=300, blocklist='०१२३४५६७८९', add_margin= 0.3 )
        text =  ''
        for i in result:
            text = i +'  '
            text.format()
        print(text)
        #save text in database
        item = Title.objects.create( name = text , v_id = id , channel = Channel.objects.get(name = channel) , tit = title)
        item.save()    
            
   


channels = {'lallantop': 'UCx8Z14PpntdaxCt2hakbQLQ', 'aajtak': 'UCt4t-jeY85JegMlZ-E5UWtA', 'abpnews': 'UCRWFSbif-RFENbBrSiez1DA', 'altnews': 'UCdDjoZAtt6PjQKAbr2FTOAQ', 'indiatoday': 'UCYPvAwZP8pZhSMW8qs7cVCw', 'indiatv': 'UCttspZesZIDEwwpVIgoZtWQ',
            'ndtv': 'UC9CYT9gSNLevX5ey2_6CK0Q', 'theprint': 'UCuyRsHZILrU7ZDIAbGASHdA', 'thequint': 'UCSaf-7p3J_N-02p7jHzm5tA', 'repulicbharat': 'UC7wXt18f2iA3EDXeqAVuKng', 'timesnow': 'UC6RJ7-PaXg6TIH2BzZfTV7w', 'zeenews': 'UCIvaYmXn910QMdemBG3v1pQ', 'wion': 'UC_gUM8rL-Lrg6O3adPW9K1g'}


for i in channels:
    try:
        ocr(i, channels[i])

    except :
        # handle the ZeroDivisionError exception and print the actual error message
        print("An error occurred:", i)
