from aiml import Kernel
import os

kernel = Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(
        learnFiles="std-startup.xml", commands="load aiml b")
    kernel.saveBrain("bot_brain.brn")

def reply(text, sessionId):
    return kernel.respond(text, sessionId)
