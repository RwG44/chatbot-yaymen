# -*- coding: utf8 -*-
from underthesea import classify

def nlp_process(text):
    result = classify(text)
    return ("Hello there! Your text is: {text}. Classify: {result}".format(text=text, result=result));