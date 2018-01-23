from aiml import Kernel
import os
import ast

kernel = Kernel()

# read bot properties from files
bot_properties = ast.literal_eval(open('bot.properties', 'r', encoding="utf-8").read())
kernel._botPredicates = bot_properties

# read brain file if availble, else learn aiml file
#brain_file = "bot_brain_alice.brn"
brain_file = "bot_brain_standard.brn"
if os.path.isfile(brain_file):
    kernel.bootstrap(brainFile=brain_file)
else:
    kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
    kernel.saveBrain(brain_file)    
    #kernel.resetBrain()
def reply(text, sessionId = 2215):
    return kernel.respond(text, sessionId)