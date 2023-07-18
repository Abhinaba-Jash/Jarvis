import builtins
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup as soap
import pyttsx3
import speech_recognition as sr
import datetime
import json
import os
import cv2
import wikipedia
from requests import get
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import calendar
import requests
import pyautogui
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from AppOpener import open, close
# for news
import requests
from bs4 import BeautifulSoup
import instaloader
import camelot
import pywikihow
import psutil
import speedtest

# driver
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
# Speak function


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Password function
def password():
    info_read = "Ardip04"
    i = int(1)
    while (i <= 3):

        a = input("Enter the password::->")
        if (a == info_read):
            speak("Welcome to the system sir ")
            break
        elif (i == 3 and a != info_read):
            speak("Get lost...")
            sys.exit()
        elif (a != info_read):
            speak("Please try again")
        i += 1


def whatsMessage():
    speak("Sir, who is the receiver")
    receiver_name = input("Enter the receiver name:")
    map_receiver_number = {"me": "7908484565", "Bardi": "8918840981", "Chordi": "8927723942", "Baba": "8348463211", "Ananya": "8436572520", "Subhodip indas": "9832137149", "Pran": "7797074365", "Asif": "6291848621", "karan": "8972209802", "Tarun": "8777251242",
                           "Riju": "8388011422", "Sohom": "7478162716", "rittik": "9593948801", "gublu": "8617439665", "Rahul": "8436158895", "Ankan": "7047373826", "Saswata": "8617583049", "Dipankar": "9933189591", "Samim": "8250836323", "Bijit": "9382729503", "Sumana": "9064571683"}
    speak("What you want to send")
    input = takecommand().lower()
    when_hour = int(datetime.datetime.now().strftime("%H"))
    when_minute = int(datetime.datetime.now().strftime("%M"))+2
    time.sleep(5)
    kit.sendwhatmsg(
        "+91"+map_receiver_number[receiver_name], f"{input}", when_hour, when_minute)
    time.sleep(7)
    pyautogui.keyDown("alt")
    pyautogui.press("f4")
    time.sleep(1)
    pyautogui.keyUp("alt")

# Taking command from user function


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...Sir")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said::{query}")

    except Exception as e:
        print("Say that again please")
        return "none"
    return query

# Greeting function


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    else:
        speak("It's night ")

# Sending email function

# problem


def sendMail():
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("abhijash04@gmail.com", "Ajash!2000")
    speak("Login success")
    server.sendmail("abhijash04@gmail.com",
                    "abhinabajash48@gmail.com", "That's a testing message")
    speak("Email has been sent , sir")
    # server.close()

# Telling current time function


def currTime():
    time_now = datetime.datetime.now()
    curr_time = time_now.strftime("%H:%M:%S")
    speak(f"The current time is: {curr_time}")

# Telling current date function


def currDate():
    data = datetime.datetime.now()
    date = data.strftime('%d/%m/%Y')
    speak(f"Date is {date}")

# problem


def pdfReader():
    #     import PyPDF2
    #     # sample_pdf = open(r'C:\Datasets\sample.pdf', mode='rb')
    #     book = open('C:\Users\abhij\OneDrive\Desktop\python_01_project\titration.pdf', 'rb')
    #     pdf_reader = PyPDF2.PdfReader(book)
    #     pages = pdf_reader.numPages
    #     speak(f"Sir, total no of pages in this book is {pages}")
    #     speak("Please say the pagenumber to read")
    #     page_number = int(takecommand().lower())
    #     page = pdf_reader.getPage(page_number)
    #     text = page.extractText()
    #     speak(text)
    #     # replace with a valid path on your local filesystem
    #     PDF_FILE_PATH = 'titration.pdf'

    # # raises an exception from PyPDF2
    #     camelot.read_pdf(PDF_FILE_PATH)
    #     # Telling weather at Burdwan function
    from PyPDF2 import PdfFileReader
    pdf_path = r"C:\\Users\\abhij\\Downloads\\GP_OOPS_C++_Encapsulation_interview.pdf"
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        print(information)
    speak(f"Sir, total no of pages in this book is {number_of_pages}")
    speak("Please say the pagenumber to read")
    page_number = int(takecommand().lower())
    # creating a page object
    pageObj = pdfReader.getPage(page_number)
    # extracting text from page
    text = text+pageObj.extractText()
    speak(text)


def weather():
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# upadting the URL
    speak("Of where sir ")
    place = takecommand().lower()
    URL = BASE_URL + "q=" + place + \
        "&appid=" + "3d149737b2d4986d9aace68e2efe5a17"
# HTTP request
    response = requests.get(URL)
# checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
    # getting the main dict block
        main = data['main']
    # getting temperature
        temperature = main['temp']
    # getting the humidity
        humidity = main['humidity']
    # getting the pressure
        pressure = main['pressure']
    # weather report
        report = data['weather']
        speak(f"{place:-^30}")
        speak(f"Temperature: {temperature}")
        speak(f"Humidity: {humidity}")
        speak(f"Pressure: {pressure}")
        speak(f"Weather Report: {report[0]['description']}")

    else:
        # showing the error message
        print("Error in the HTTP request")

# Telling BBC news function


def newsFromBBC():

    url = 'https://www.bbc.com/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    i = 0
    for x in headlines:
        i += 1
        speak(str(i))
        speak(x.text.strip())
        if i >= 10:
            break

# Telling yahoo news function


def yahooNews():

    url = "https://news.yahoo.com/news"
    response = requests.get(url)
    time.sleep(3)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    i = 0
    for x in headlines:
        i += 1
        speak(str(i))
        speak(x.text.strip())
        if i >= 10:
            break

# Setting alarm function


def setAlarm():
    speak("Sir, at what time you want to set the alram")
    alarm_time = takecommand().lower()
    alarm_hour = int(alarm_time[0:2])
    alarm_minute = int(alarm_time[2:4])
    # converting total time into second
    total_second = (alarm_hour*3600)+(alarm_minute*60)
    now = datetime.datetime.now()
    seconds_hms = [3600, 60, 1]
    currentTimeInSeconds = sum(
        [a*b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])
    secondsUntilAlarm = total_second-currentTimeInSeconds
    if secondsUntilAlarm < 0:
        secondsUntilAlarm += 86400  # number of seconds in a day
    speak(f"Sir, alarm is set at {alarm_time} for {secondsUntilAlarm} seconds")
    time.sleep(secondsUntilAlarm)
    while True:
        speak("Sir, please wake up, Sir, please wake up")
        stop = takecommand().lower()
        if "stop" in stop:
            break


def getLocation():
    response = requests.get('https://api64.ipify.org?format=json').json()
    ip_address = response["ip"]
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "currency": response.get("currency_name")
    }
    speak(
        f"Sir I think we are in {location_data['city']} city , in region of {location_data['region']} , {location_data['country']}, currency name {location_data['currency']}.")


def openMobileCamera():
    import urllib.request
    import cv2
    import numpy as np
    import time
    speak("Please enter the mobile code correctly")
    code = input("Enter the code here::->")
    url = f"http://{code}/shot.jpg"
    while True:
        img_arr = np.array(
            bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        cv2.imshow("IPWebcam", img)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break
    cv2.destroyAllWindows()


def checkInstaProfile():
    speak("Sir please enter the username")
    user_name = input("Enter the username here(correctly):")
    time.sleep(5)
    webbrowser.open(f"www.instagram.com/{user_name}")
    time.sleep(5)
    speak("Sir, would you like to download the profile picture")
    take_input = takecommand().lower()
    if "yes" in take_input:
        mod = instaloader.Instaloader()
        mod.download_profile(user_name, profile_pic_only=True)
        speak("Sir , the profile picture is downloaded successfully")
    else:
        pass


def task_execution():
    wish()
    currDate()
    while True:
        speak("How can I help you ")
        query = takecommand().lower()
        if "open telegram" in query:
            path1 = "C:\\Users\\abhij\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(path1)
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:

                result, image = cap.read()
                if result:
                    # Taking image
                    cv2.imshow("webcam", image)
                    # Saving image in local file
                    speak("Sir please tell me the file to save the image")
                    file_name = takecommand().lower()
                    cv2.imwrite(f"{file_name}.png", image)
                    cv2.waitKey(1)
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                else:
                    speak("No image detected! please try again")
        elif "what is my ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your ip address is {ip}")
        elif "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("Accroding to wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open google" in query:
            speak("What should I search on google sir")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif "refresh" in query:
            pyautogui.press("f5")
            time.sleep(1)
        elif "weather" in query:
            weather()
        elif "message in whatsapp" in query:
            whatsMessage()
        elif "send message to my group" in query:
            # group_id ="C7zdTTVjclBAK0njX01BQP"
            speak("What you want to send")
            input = takecommand().lower()
            # time.sleep(2)
            when_hour = int(datetime.datetime.now().strftime("%H"))
            when_minute = int(datetime.datetime.now().strftime("%M"))+1
            time.sleep(4)
            kit.sendwhatmsg_to_group(
                "C7zdTTVjclBAK0njX01BQP", f"{input}", when_hour, when_minute)
            time.sleep(4)
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "play song" in query:
            speak("What song")
            song = takecommand().lower()
            kit.playonyt(f"{song}")
        elif "send mail" in query:
            sendMail()
        elif "the time" in query:
            currTime()
        elif "the date" in query:
            currDate()
        elif "switch" in query:
            pyautogui.keyDown("alt")
            pyautogui.keyDown("tab")
            pyautogui.keyUp("tab")
            time.sleep(1)

            while True:
                speak("Want tab")
                query1 = takecommand().lower()
                if "tab" in query1:
                    pyautogui.keyDown("tab")
                    pyautogui.keyUp("tab")
                    time.sleep(1)

                if "no" in query1:
                    speak("Thanks for confirming")
                    time.sleep(1)
                    break

            pyautogui.keyUp("alt")
        elif "bbc news" in query:
            speak("Please wait sir , fetching news")
            newsFromBBC()
        elif "yahoo news" in query:
            speak("Please wait sir , fetching news")
            yahooNews()
        elif "close window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "close tab" in query:
            pyautogui.keyDown("ctrl")
            pyautogui.press("f4")
            time.sleep(1)
            pyautogui.keyUp("ctrl")
        elif "take screenshot" in query:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(
                'C:\\Users\\abhij\\OneDrive\\Pictures\\Screenshots\\python.png')
            speak("Screenshot has been taken")
        elif "notification" in query:
            pyautogui.keyDown("Win")
            pyautogui.press("n")
            time.sleep(1)
            pyautogui.keyUp("Win")
            time.sleep(10)
            pyautogui.keyDown("Win")
            pyautogui.press("n")
            time.sleep(1)
            pyautogui.keyUp("Win")
        elif "settings" in query:
            pyautogui.keyDown("Win")
            pyautogui.press("i")
            time.sleep(1)
            pyautogui.keyUp("Win")
        elif "file explorer" in query:
            pyautogui.keyDown("Win")
            pyautogui.press("e")
            time.sleep(1)
            pyautogui.keyUp("Win")
        elif "home" in query:
            pyautogui.keyDown("Win")
            pyautogui.press("d")
            time.sleep(1)
            pyautogui.keyUp("Win")
        elif "clipboard" in query:
            pyautogui.keyDown("Win")
            pyautogui.press("v")
            time.sleep(1)
            pyautogui.keyUp("Win")
        elif "virtual" in query:
            pyautogui.keyDown("Win")
            pyautogui.keyDown("ctrl")
            pyautogui.press("d")
            time.sleep(1)
            pyautogui.keyUp("ctrl")
            pyautogui.keyUp("Win")
        elif "close virtual" in query:
            pyautogui.keyDown("Win")
            pyautogui.keyDown("ctrl")
            pyautogui.press("f4")
            time.sleep(1)
            pyautogui.keyUp("ctrl")
            pyautogui.keyUp("Win")
        elif "open emoji" in query:
            pyautogui.keyDown("Win")
            pyautogui.keyDown(".")
            pyautogui.press(";")
            time.sleep(1)
            pyautogui.keyUp(".")
            pyautogui.keyUp("Win")
        elif "open search" in query:
            pyautogui.keyDown("Win")
            pyautogui.press("s")
            time.sleep(1)
            pyautogui.keyUp("Win")
            # problem
        elif "volume up" in query:
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif "set an alarm" in query:
            setAlarm()
        elif "where we are" in query:
            speak("Wait sir, let me check")
            try:
                getLocation()
            except Exception as e:
                speak("Sorry sir I couldn't find")
                pass
        elif "instagram profile" in query:
            checkInstaProfile()
        # problem
        elif "read" in query:
            pdfReader()
        elif "temperature" in query:
            speak("Of where sir")
            place = takecommand().lower()
            search = f"temperature in {place}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")

        elif "want to search" in query:
            from pywikihow import search_wikihow

            speak("What you want to search sir")
            what = takecommand().lower()
            max_results = 1
            how_to = search_wikihow(what, max_results)
            assert len(how_to) == 1
            how_to[0].print
            speak(how_to[0].summary)
        elif "power" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir you system have {percentage}% battery left")
            if percentage >= 75:
                speak("Sir we have enough power to continue ")
            elif percentage < 75 and percentage >= 40:
                speak("Sir we shall connect our syster to charging port ")
            elif percentage < 40 and percentage > 15:
                speak(
                    "Sir we have very low power left, we must connect our system for charging")
            elif percentage <= 15:
                speak("Sir we gone down to 15, connect to charger immediately")
        elif "speed test" in query:
            st = speedtest.Speedtest()
            dl = st.download()*1.25e-7
            ul = st.upload()*1.25e-7
            speak(
                f"Sir this internet has {dl} MB per second download speed and {ul} MB per second upload speed ")
        elif "open mobile camera" in query:
            openMobileCamera()
        elif "sleep" in query or "no thanks" in query:
            speak("Ok sir, you can call me anytime.")
            break
        elif "goodbye" in query or "bye" in query:
            speak("Glad to help you sir, have a nice day")
            sys.exit()
        speak("Sir, do you have any other work")


if __name__ == "__main__":
    password()
    while True:
        permission = takecommand().lower()
        if "wake up" in permission:
            task_execution()
        elif "goodbye" in permission or "no thanks" in permission:
            speak("Glad to help you sir, have a nice day")
            sys.exit()
