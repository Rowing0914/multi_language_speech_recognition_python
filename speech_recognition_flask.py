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
		text = r.recognize_google(audio, language = 'ja-JP')
		print(text)
	return text

if __name__ == '__main__':
	r = sr.Recognizer()
	app.run(host='0.0.0.0', port=8080)