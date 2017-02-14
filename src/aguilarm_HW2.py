#Miguel Aguilar
#CS451 Homework 2

import goslate

gs = goslate.Goslate()

def get_word():
	word = raw_input("Enter a word you would like to be translated: ")
	word = str(word)
	return word

def recognize_language(word):
	return "Recognizing the language...\n"
	language_id = gs.detect(word)
	detect_language = gs.get_languages()[language_id]
	#return "The language of " + str(word) + " is " + str(detect_language)

def translate_word(word):
	translated = gs.translate(word,'es')
	return translated

####################MAIN#############################
print "This is an application to translate a language into Spanish."
print "------------------------------------------------------------\n"
word = get_word()
print recognize_language(word)
translated = translate_word(word)
print "\nThe translation of " + str(word) + " into Spanish is : " + "\n" + str(translated)
