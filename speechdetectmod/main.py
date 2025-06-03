import libpath
import time

from naoqi import ALModule, ALProxy

class SpeechDetectionModule(ALModule):
	""" 
	A module that handles NAO speech recognition commands based on a vocabulary.
	The vocabulary can be a list of keywords or a list of phrases. Keep the phrases short.
	"""
	
	def exit(self):
		print("exiting module")
		self.memory.unsubscribeToEvent("WordRecognized", self.getName(), "onWordRecognized")
		self.asr.unsubscribe(self.getName())
		ALModule.exit(self)

	def __init__(self, name):
		ALModule.__init__(self, name)
		self.detectedPhrase = None
		self.spottingMode = False
		self.timestamp = time.time()
		self.name = name
		self.memory = ALProxy("ALMemory")
		self.asr = ALProxy("ALSpeechRecognition")
		# need to pause the asr before changing specs
		self.asr.pause(True)
		self.asr.setLanguage("English")
		vocabulary = ["color", "text", "hand", "phone", "stop"]
		self.asr.setVocabulary(vocabulary, self.spottingMode)
		self.asr.pause(False)
		self.asr.subscribe(self.getName())
		self.memory.subscribeToEvent("WordRecognized", self.getName(), "onWordRecognized")

	def onWordRecognized(self, key, value, message):	
		""" A method that handles command recognition. """
		print("Detected speech values:", value)
		
		# check confidences
		# threshold of 0.45 can be fine-tuned
		if(len(value) > 1 and value[1] >= 0.30):
			self.timestamp = time.time()	# record the time
			splits = value[0].split('<...>') #if wordSpotting is enabled, value[0] = "<...> keyword <...>" else "keyword"
			vocab = value[0] if len(splits) == 1 else splits[1].strip()

			'''
			TODO: 
			Add code to capture the detected phrase and pass beyond the handler to the main calling program
			'''
			self.detectedPhrase = vocab  # Store the detected phrase for use outside this handler
   
			pass
		else:
			print('insufficient threshold')

			'''
			TODO: 
			Add code here remove the detected phrase and not pass beyond the handler
			'''
			self.detectedPhrase = None  # Clear the detected phrase due to low confidence
			pass

	def setVocabulary(self, vocabulary, spotting=False):
		"""Change the vocabulary used"""
		self.asr.pause(True)
		self.spottingMode = spotting
		self.asr.setVocabulary(vocabulary, spotting)
		self.asr.pause(False)		
