import time
import random

from loadjsonintents import load_json_intents
# the order of imports are important
import libpath
from naoqi import ALProxy, ALModule, ALBroker

from speechdetectmod import SpeechDetectionModule

"""
Convenient function to disable speech recognition while speaking
"""
def speak(text):
	SpeechDetection.asr.pause(True)
	tts.say(text)
	time.sleep(1)
	SpeechDetection.asr.pause(False)
	time.sleep(0.5)

# get robot ip
'''
TODO: You need to find out your robot IP address
'''
ip = "172.20.10.2"
port = 9559

# load intents from file and extract a list of all example phrases
intents = load_json_intents("intents.json")
phrases = []
for intent in intents:
	phrases += intent["examples"]
print(phrases)

# setup subsystems
tts = ALProxy("ALTextToSpeech", ip, port)
tts.setVolume(0.4)

try:
	# this is required to use the ALModule for SpeechDetection
	print("Create an ALBroker")

	myBroker = ALBroker("NaoAppBroker",
		"0.0.0.0",   # listen to anyone
		0,           # find a free port and use it
		ip,      # parent broker IP
		port)    # parent broker port
	SpeechDetection = SpeechDetectionModule("SpeechDetection")

	if SpeechDetection:
		SpeechDetection.setVocabulary(phrases)

	done = False
	detected_intent = None
	last_phrase = ""  # Store last handled phrase
	tts.say("Hello, I am Nao. I am your treatment assistant. Speak freely")
	last_hint = time.time()

	while not done:
		if SpeechDetection.detectedPhrase:
			phrase = SpeechDetection.detectedPhrase.lower()
   
			 # Only process if the phrase is different from last handled phrase
			if phrase != last_phrase:
				last_phrase = phrase  # Update last handled phrase
				detected_intent = None  # Reset before each loop

				for intent in intents:
					for example in intent['examples']:
						if phrase == example.lower():
							detected_intent = intent
							break
					if detected_intent:
						break

				if detected_intent:
					response = random.choice(detected_intent['responses'])
					print("Bot:", response)
					tts.say(response)

					if detected_intent['intent'].lower() == 'farewell':
						done = True
						time.sleep(2)
						tts.say("My work is done here. Goodbye.")
			'''
			TODO:
			- Loop over all the intents loaded from intents.json
			- Extract the detected phrase in the handler
			- check against each intents' examples to find a match => detected intent
			- Once you found one, choose randomly one string from the detected intent's responses to speak
			- If the detected intent is 'end', terminate the while loop
			'''

except KeyboardInterrupt:
	print("User keyboard interrupted")
except Exception as e:
	print(e)
finally:
	# print(SpeechDetection.words)
	del SpeechDetection
	myBroker.shutdown()

