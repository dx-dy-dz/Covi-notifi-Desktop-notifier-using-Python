import time 
import requests 
from plyer import notification 
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    print("Please! Check your internet connection")
if (covidData != None):
    data = covidData.json()['Success'] 
    while(True):
        notification.notify(
            title = "COVID-19 Stats in India",
            message = "Total cases reported : {totalcases}\nCases reported today : {todaycases}\nDeaths reported : {todaydeaths}\nTotal active cases : {active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]),
            app_icon =  "coronavirus.ico",
            timeout  = 100
        )
        time.sleep(60*60*4)
