# -*- coding: utf8 -*-
#from underthesea import classify
#from underthesea import *
from googletrans import Translator
import bot_ai

def nlp_process(text, sessionId):
    #text = "Chuyên trang chuyển nhượng Transfermarkt" mới cập nhật giá trị chuyển nhượng cầu thủ. Trong đó, Kylian Mbappe là cầu thủ tăng giá mạnh nhất, lên tới 90 triệu euro."
    #result = "#"
    #text_classes = classify(text)
    #for text_class in text_classes:
    #    result += text_class + ", "
    
    #result += ". Sentiment: " + sentiment(text)
    #result += ". NER: " + uts.ner(text)
    translator = Translator()
    eng_text = translator.translate(text, dest='en', src='vi').text
    result = bot_ai.reply(eng_text, sessionId)

    return ('Hello there! Your text is: "{text}". English: {result}'.format(text=text, result= result));
