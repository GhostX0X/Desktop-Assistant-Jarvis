import pyttsx3
import speech_recognition as sr
import webbrowser  
import pywhatkit
import os
import pyautogui
import pyjokes
import datetime
import playsound
import speedtest
import wikipedia
import pyautogui

Assi = pyttsx3.init('sapi5')
voices = Assi.getProperty('voices')
#print(voices)
Assi.setProperty('voices',voices[0].id)

def Speak(audio):
    print("  ")
    Assi.say(audio)
    print(f":{audio}")
    Assi.runAndWait()

def takecommand():
    cmd = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        cmd.pause_threshold = 1
        audio = cmd.listen(source)

        try:
            print("Recognizing...")
            query = cmd.recognize_google(audio,language='en-in')
            #print(f"You said :{query}")  

        except Exception as Error:
            return None

        return query

def taskexe():

    def music():
        Speak("Tell the name of the song you want to play")
        musicname = takecommand()
        musicname = musicname.replace("jarvis","")
        musicname = musicname.replace("youtube","")
        musicname = musicname.replace("search","")
        web = 'https://www.youtube.com/results?search_query= '+ musicname
        webbrowser.open(web)
        Speak("Your requested song has been played")

    def speedtest():
        import speedtest
        Speak("Checking the speed...")
        st = speedtest.Speedtest()
        dl = (st.download()/1048576)
        up = (st.upload()/1048576)

        if 'uploading' in query:
            Speak(f"The uploading speed is mbps")
            print(up)

        elif 'downloading' in query:
            Speak(f"The downloading speed is mbps")
            print(dl)

        else:
            Speak("The Downloading speed and uploading speed are as followed : ")
            print("Downloading speed :",dl)
            print("Uploading speed : ",up)

    def OpenApps():
        Speak("Ok Sir , Wait A Second!")
        
        if 'code' in query:
            os.startfile("C:\\Applications\\Microsoft VS Code\\Microsoft VS Code\\Code.exe")

        elif 'telegram' in query:
            os.startfile("https://web.telegram.org/z/")
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your Command Has Been Completed Sir!")        

    while True:

        query = takecommand()

        if 'hello jarvis' in query:
            Speak("Hello sir I am Jarvis 1.0")
            Speak("Your personal desktop assisant")
            Speak("How may I help you ?")

        elif 'how are you' in query:
            Speak("I am fine sir")
            Speak("What about you ?")
            Speak("How's your day ?")   

        elif 'youtube search' in query:
            Speak("Searching on youtube this is what I found in youtube search")
            query = query.replace("jarvis","")
            query = query.replace("youtube","")
            query = query.replace("search","")
            web = 'https://www.youtube.com/results?search_query= ' + query
            webbrowser.open(web)
            Speak("Completed the search")

        elif 'google search' in query:
            Speak("Searching on google this is what I found in google search")
            query = query.replace("Jarvis","")
            query = query.replace("google search","")    
            pywhatkit.search(query)
            Speak("Completed the search ")

        elif 'open chrome' in query:
            Speak("what should I search ?")
            qry = takecommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            Speak(results)    

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")    

        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'music' in query:
            music()     

        elif 'wikipedia' in query:
            Speak("searching in wikipedia for results")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According to wikipedia : {wiki}")

        # elif 'screenshot' in query:
        #     scrshot = pyautogui.screenshot()
        #     scrshot.save('D:\screenshot_jarvis ')

        elif 'repeat my words' in query:
            Speak("I am ready sir you may speak the words I will be repeating them for you")
            rpt = takecommand()
            Speak(f"You said : {rpt}")

        elif 'tell me jokes' in query:
            get = pyjokes.get_jokes()
            Speak(get)

        elif 'alarm' in query:
            Speak("Enter the time for alarm")
            time = input("Enter time for alarm : ")

            while True:
                Time_ac = datetime.datetime.now()
                now = Time_ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up sir !")
                    playsound('JarvisAlarm.mp3')
                    Speak("Its time to end the alarm")

                    if now>time:
                        break

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open telegram' in query:
            OpenApps()            

        elif 'speedtest' in query:
            speedtest()

        elif 'internet speed' in query:
            speedtest() 

        elif "open camera" in query:
            import cv2
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWndows() 

        elif "take screenshot" in query:
            import pyautogui
            img = pyautogui.screenshot()
            img.save("jarvis_screenshot.png")
            Speak("screenshot saved")  

        elif 'selfie' in query:
            import pyautogui
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(3)
            Speak("Smile Please ") 
            pyautogui.press("enter")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strTime}")  

        elif 'open' in query:
            query = query.replace("open","")
            query = query.replace("jarvis","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")    

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")      

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "Lock" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  

        elif 'you need a break' in query:
            Speak("Ok sir you can call me anytime you need ")   
            break    
   
taskexe()
