#: Import modules
import polyglot
import chardet
import langid
from textblob import TextBlob
from polyglot.text import Text, Word
from langdetect import detect, DetectorFactory, detect_langs
from guess_language import guess_language

# method: textBlob
# Dedect which language used
# @return: True
# @completed
def textBlob():
	with open("./yourinputfile.txt", "r") as sentences:
		try:			
			for sentence in sentences:
				sentence = sentence.strip()
				blob = TextBlob(sentence)
				result = blob.detect_language()
				with open("./output/textBlobResult.short.txt", "w") as output:
					output.write(sentence, ":", result)
		except:
			pass
	return True

# method: polyglot
# Dedect which language used
# @return: True
# @completed
def polyglot():
	#: Import dataset
	with open("./yourinputfile.txt", "r") as sentences:
		try:
			for sentence in sentences:
				sentence = sentence.strip()
				result = Text(sentence)
				print(sentence, "Language Detected: Code={}, Name={}\n".format(result.language.code, 
					result.language.name), file = open("./output/polyglotResult.short.txt", "a"))
		except:
			pass
	return True

# method: chardetExport
# Dedect which language used
# @return: True
# @completed
def chardetExport():
	#: Import dataset
	with open("./yourinputfile.txt", "r") as sentences:
		try:
			for sentence in sentences:
				sentence = sentence.strip()
				result = chardet.detect(sentence.encode('utf-8'))
				#print(result)
				print(sentence, result, file = open("./output/chardetResult.short.txt", "a"))
		except:
			pass
	return True

# method: langDedect
# Dedect which language used
# @return: True
# @completed
def langDedect():
	#: Import dataset
	with open("./yourinputfile.txt", "r") as sentences:
		try:
			for sentence in sentences:
				sentence = sentence.strip()
				result = detect_langs(sentence)
				#print(result)
				print(sentence, ":" ,result, file = open("./output/langDedectResult.short.txt", "a"))
		except:
			pass
	return True

# method: guessLanguage
# Dedect which language used
# @return: True
# @completed
def guessLanguage():
	#: Import dataset
	with open("./yourinputfile.txt", "r") as sentences:
		for sentence in sentences:
			try:
				sentence = sentence.strip()
				result = guess_language(sentence)
				#print(result)
				print(sentence, ":" ,result, file = open("./output/guessLanguageResult.short.txt", "a"))
			except:
				pass
	return True

# method: lanidExport
# Dedect which language used
# @return: True
# @completed
def langidExport():
	#: Import dataset
	with open("./yourinputfile.txt", "r") as sentences:
		for sentence in sentences:
			try:
				sentence = sentence.strip()
				result = langid.classify(sentence)
				#print(result)
				print(sentence, ":" ,result, file = open("./output/langidResult.short.txt", "a"))
			except:
				pass
	return True


if __name__ == '__main__':
	textBlob()
	polyglot()
	chardetExport()
	langDedect()
	guessLanguage()
	langidExport()