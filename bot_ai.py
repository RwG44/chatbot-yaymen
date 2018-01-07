from aiml import Kernel
import os

kernel = Kernel()

brain_file = "bot_brain_alice.brn"

if os.path.isfile(brain_file):
    kernel.bootstrap(brainFile=brain_file)
else:
    kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
    kernel.setBotPredicate("name", "Yay")
    kernel.setBotPredicate("city", "Ho Chi Minh City")
    kernel.setBotPredicate("email", "minhtrung995@gmail.com")
    kernel.setBotPredicate("master", "Trung Depzai")
    kernel.setBotPredicate("country", "Vietnam")
    kernel.setBotPredicate("botmaster", "Creator")
    kernel.setBotPredicate("nationality", "Vietnamese")
    kernel.setBotPredicate("age", "22")
    kernel.setBotPredicate("gender", "female")
    kernel.setBotPredicate("language", "python")

    kernel.saveBrain(brain_file)    
    #kernel.resetBrain()
def reply(text, sessionId = 2215):
    return kernel.respond(text, sessionId)

