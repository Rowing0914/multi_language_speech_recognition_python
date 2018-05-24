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
text = r.recognize_google(audio, language = 'ja-JP')
print(text)
