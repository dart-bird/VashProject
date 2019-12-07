from gtts import gTTS
text ="결제가 완료되었습니다."

tts = gTTS(text=text, lang='ko')
tts.save("./audio/finish.mp3")

text ="1번 세탁기, 가동을 시작합니다."

tts = gTTS(text=text, lang='ko')
tts.save("./audio/1_run.mp3")