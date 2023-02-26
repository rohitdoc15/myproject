#open file containing hindi text and translate it to english and save it in a file using googletrans
#


def trans(channel):
    import os
    from googletrans import Translator
    translator = Translator()
    file_path = os.path.join("channels", channel, channel + '.txt')
    with open(file_path, 'r') as f:
        
        text = f.read()
        
    english_text = translator.translate(text, dest='en').text
    
    # Writing the translated text to a file
    file_path = os.path.join("channels", channel, channel + '_eng.txt')
    with open(file_path, 'w+') as f:
        f.write(english_text)

trans("lallantop")


