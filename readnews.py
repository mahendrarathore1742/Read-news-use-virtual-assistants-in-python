import pyttsx3
import requests
import json;
import datetime;
engine=pyttsx3.init('sapi5'); #this is voice api provided by Microsoft
voices=engine.getProperty('voices');
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio);
    engine.runAndWait();

def wishMe():
    hour=int(datetime.datetime.now().hour);
    if hour>=0 and hour<12:
        speak('good moringh');
    elif hour>=12 and hour<18:
        speak('Good afternoon');
    else:
        speak('Good eveingh');

def newsa():
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=enter the news api key');
    response = requests.get(url).text;
    news_dicts=json.loads(response);
    arts=news_dicts['articles'];
    
    for articles in arts:
        speak(articles['title']);
        print(articles['title']);
        speak('moving on the next news');
if __name__=="__main__":
    wishMe();
    newsa();