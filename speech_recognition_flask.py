from flask import Flask
import speech_recognition as sr

app = Flask(__name__)
@app.route('/')

def identifier():
	flg = True
	while flg:
		with sr.Microphone() as source:
		    print('Say Something:')
		    audio = r.listen(source)
		    if(audio):
		    	flg = False
		    	print ('Done!')
		text = r.recognize_google(audio, language = 'en-US')
		if(text):
			lang_flg = 'en'
		text = r.recognize_google(audio, language = 'ja-JP')
		if(text):
			lang_flg = 'jp'
		print("lang_flg: ", lang_flg, " and what you mentioned is: ", text)
	return text, lang_flg

if __name__ == '__main__':
	r = sr.Recognizer()
	app.run(host='127.0.0.1', port=5000)