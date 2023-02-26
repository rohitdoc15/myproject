from googletrans import Translator
from googleapiclient.discovery import build
import datetime
import requests
import os




os.chdir('/home/rohit/project/myproject/base/scripts')
# from trans import trans

translator = Translator()

# Replace with your own API key
API_KEY = 'AIzaSyDzQngwEKSXznBCvRoURIXs4-WZeps4uHA'

# Create a service object for making requests to the YouTube API
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Specify the date range
now = datetime.datetime.utcnow()
date = datetime.datetime.utcnow().date()
published_after = datetime.datetime.combine(
    date, datetime.time.min).isoformat() + 'Z'
published_before = datetime.datetime.combine(
    date, datetime.time.max).isoformat() + 'Z'
yesterday = datetime.date.today() - datetime.timedelta(days=1)
today = datetime.date.today()
# this needs to run only once to load the model into memory



def ocr(channel, channel_id):

    #delete all files which is not created today
    folder = 'channels'
    subfolder = os.path.join(folder, channel, 'thumb')
    #delete old files whi`ch is not created today
    for filename in os.listdir(subfolder):
        if filename.endswith(".jpg"):
            path = os.path.join(subfolder, filename)
            file_date = datetime.datetime.fromtimestamp(os.path.getmtime(path)).date()
            if file_date != today:
                os.remove(path)
                print('file deleted')
 

            

    search_response = youtube.search().list(
        channelId=channel_id,
        type='video',
        part='id',
        maxResults=50,
        publishedAfter=published_after,
        publishedBefore=published_before
    )
    response = search_response.execute()

    # Print the video IDs
    for search_result in response.get('items', []):
        
        video_id = search_result['id']['videoId']
        #save title to database
        
        channel = channel
        print(search_result)
        id = search_result['id']['videoId']
        image_url = 'https://i.ytimg.com/vi/'+id+'/maxresdefault.jpg'
        print(channel)

        folder = 'channels'
        subfolder = os.path.join(folder, channel, 'thumb')
                
        

    # Create the subfolder if it doesn't exist
        os.makedirs(subfolder, exist_ok=True)

    # Save the image to the subfolder
        response = requests.get(image_url)
        with open(os.path.join(subfolder, channel+'__' + id+'.jpg'), 'wb') as f:
            f.write(response.content)

        folder = 'channels'
        subfolder = os.path.join(folder, channel, 'thumb')
        filename = channel+'__' + id+'.jpg'
        filepath = os.path.join(subfolder, filename)

    # Create the subfolder if it doesn't exist
        os.makedirs(subfolder, exist_ok=True)

    # Check if the file already exists
        if os.path.exists(filepath):

            print(f"File {filename} already exists in {subfolder}")
            
        else:
            # Save the new file
            response = requests.get(image_url)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Saved new file {filename}")


channels = {'lallantop': 'UCx8Z14PpntdaxCt2hakbQLQ', 'aajtak': 'UCt4t-jeY85JegMlZ-E5UWtA', 'abpnews': 'UCRWFSbif-RFENbBrSiez1DA', 'altnews': 'UCdDjoZAtt6PjQKAbr2FTOAQ', 'indiatoday': 'UCYPvAwZP8pZhSMW8qs7cVCw', 'indiatv': 'UCttspZesZIDEwwpVIgoZtWQ',
            'ndtv': 'UC9CYT9gSNLevX5ey2_6CK0Q', 'theprint': 'UCuyRsHZILrU7ZDIAbGASHdA', 'thequint': 'UCSaf-7p3J_N-02p7jHzm5tA', 'repulicbharat': 'UC7wXt18f2iA3EDXeqAVuKng', 'timesnow': 'UC6RJ7-PaXg6TIH2BzZfTV7w', 'zeenews': 'UCIvaYmXn910QMdemBG3v1pQ', 'wion': 'UC_gUM8rL-Lrg6O3adPW9K1g'}


for i in channels:
    try:
        ocr(i, channels[i])

    except ZeroDivisionError as e:
        # handle the ZeroDivisionError exception and print the actual error message
        print("An error occurred:", i)

