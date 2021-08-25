import pyttsx3
import wikipedia
import subprocess
import speech_recognition as sr
engine=pyttsx3.init()
file=open('C:/users/Ashu/desktop/AI projects/datasets_of_science.yml')
ques=[]
ans=[]
k=0
for i in file:
    k+=1
    if k%2:ques.append(i[4:-1].lower())
    else:ans.append(i[4:-1])
print(ques)
print(ans)
while 1:
    engine.say("How can I help?")
    engine.runAndWait() 
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) 
        audio=r.listen(source)
    try:inp=r.recognize_google(audio)
    except:continue
    q=0
    if inp=="stop":
        engine.say("Good Bye Sir See you next time")
        break
    elif "what is" in inp:
        b=inp.split("what is")
        try:
            Ashu=wikipedia.summary(b[1],sentences=3)
            q=1
        except:q=0
    elif "open" in inp:
        subprocess.call(['cmd.exe','/c','notepad'])
    else:
        for i in range(len(ques)):
            if inp==ques[i]:
                Ashu=ans[i]
                q=1
                break
    if q==0:Ashu="Sorry I don't know !!!"
    print(Ashu)
    engine.say(Ashu)
engine.runAndWait()