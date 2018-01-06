# -*- coding: utf8 -*-
#from underthesea import classify
#from underthesea import classification

def nlp_process(text):
    #text = "Chuyên trang chuyển nhượng Transfermarkt mới cập nhật giá trị chuyển nhượng cầu thủ. Trong đó, Kylian Mbappe là cầu thủ tăng giá mạnh nhất, lên tới 90 triệu euro."
    result = "Classify: "
    #text_classes = classify(text)
    #for text_class in text_classes:
    #    result += text_class + ", "
    
    #result += ". Sentiment: " + sentiment(text)
    #result += ". NER: " + uts.ner(text)
    return ('Hello there! Your text is: "{text}". NLP: {result}'.format(text=text, result= result));
