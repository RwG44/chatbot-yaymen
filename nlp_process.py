# -*- coding: utf8 -*-
#from underthesea import classify
#from underthesea import *
from googletrans import Translator
import bot_ai

def nlp_process(input_vi, sessionId):
    #text = "Chuyên trang chuyển nhượng Transfermarkt" mới cập nhật giá trị chuyển nhượng cầu thủ. Trong đó, Kylian Mbappe là cầu thủ tăng giá mạnh nhất, lên tới 90 triệu euro."
    #result = "#"
    #text_classes = classify(text)
    #for text_class in text_classes:
    #    result += text_class + ", "
    
    #result += ". Sentiment: " + sentiment(text)
    #result += ". NER: " + uts.ner(text)
    translator = Translator()
    input_en = translator.translate(input_vi, dest='en', src='vi').text
    
    output_en = bot_ai.reply(input_en, sessionId)
    output_vi = translator.translate(output_en, dest='vi', src='en').text
    return output_vi
