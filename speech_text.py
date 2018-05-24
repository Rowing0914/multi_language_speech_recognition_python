import speech_recognition as sr

r = sr.Recognizer()
flg = True

while flg:
	with sr.Microphone() as source:
	    print('Say Something:')
	    audio = r.listen(source)
	    if(audio):
	    	print ('Done!')
	    	flg = False

text = r.recognize_google(audio, language = 'en-US')
if(text):
	flg = 'en'
text = r.recognize_google(audio, language = 'ja-JP')
if(text):
	flg = 'jp'
print("lang_flg: ", flg, " and what you mentioned is: ", text)