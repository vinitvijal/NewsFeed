import requests
import json

from requests.api import request

# My Functions Are Down Here :
def weather(city):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=0c42f7f6b53b244c78a418f4f181282a')    
    # json_key = json.loads(response.text)
    # print(json_key)
    # return response
    json_key = json.loads(response.text)
    if str(json_key['cod']) == "404":
        print()
        print()
        print("Please check your spelling!!!!")
        print()
        return "notWorking"
    else:
        return response
        print()

# Main Program
def init():


    print()
    print()
    print()
    print('# ' + '=' * 78)
    print('Author: ' + "Vinit Vijal")
    print('Version: ' + "1.0.1")
    print('Maintainer: ' + "Vinit Vijal")
    print('Email: ' + "Vinudev.web@gmail.com")
    print('Status: ' + "Development")
    print('Date: ' + "7th July 2021")
    print('Username: ' + "@vinuDev_")
    print('Description: ' + "Its a Weather App Created by Vinit Vijal. ")
    print('# ' + '=' * 78)
    print()
    print("To Exit the program write : exit")


    num = 0                     #at 0 it will directly run without asking do you want details....
    work = 1                    #Here 1 means Yes and 0 means No
    while work == 1:
        while num == 0:
            if num == 0:
                print()
                print()
                print()
                city = input("Enter Your City Name : ")
                if city == "exit":
                    print()
                    print()
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("'                                                                   '")
                    print("'      Thanks For Using Our Weather Python Program - Byy !!!!!      '")
                    print("'                      CREATED BY - Vinit Vijal                     '")
                    print("'                                                                   '")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    print()
                    num = 5
                    work = 0
                    break
                else : 
                    # weather(city)
                    data = weather(city)
                    if data == "notWorking":
                        print("Try Again!")
                        break
                    else:
                        json_data = json.loads(data.text)
                        longitude = str(json_data['coord']['lon'])
                        latitude = str(json_data['coord']['lat'])
                        txt = 'https://api.openweathermap.org/data/2.5/onecall?lat='+latitude+'&lon='+longitude+'&appid=0c42f7f6b53b244c78a418f4f181282a'
                        timezoner = requests.get(txt)
                        json_time = json.loads(timezoner.text)
                        # print(json_time)
                        print()
                        # print(json_data)
                        print()
                        print()
                        print()
                        print("===========================================================")
                        print("Name of City : " + json_data['name'])
                        print()
                        print("Current Temperature of Today is : " + str(str(round(float(json_data['main']['temp'])-273.16)))+ " C")
                        print()
                        print("Current Mood of weather : " + str(((json_data['weather'])[-1])['main']))
                        print()
                        print("Time Zone : " + json_time['timezone'])
                        print("===========================================================")
                    
            
    # elif num == 0:
    #         city = input("Enter Your City Name : ")
    #         weather(city)
    #         data = weather(city)
    #         json_data = json.loads(data.text)
    #         print()
    #         # print(json_data)
    #         print()
    #         print()
    #         print()
    #         print("===========================================================")
    #         print()
    #         print("Name of City : " + json_data['name'])
    #         print()
    #         print("Current Temperature of Today is : " + str(str(round(float(json_data['main']['temp'])-273.16)))+ " C")
    #         print()
    #         print("Current Mood of weather : " + str(((json_data['weather'])[-1])['main']))
    #         print()
    #         print("===========================================================")
    #         print()
    #         print()
    #         num += 1