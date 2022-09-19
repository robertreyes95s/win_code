from tkinter import *
import requests
from configparser import ConfigParser
from tkinter import messagebox

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def getweather(city):
    result = requests.get(url.format(city, api_key))
    
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celcius = temp_kelvin - 275.15
        temp_fahrenheit = temp_celcius * 1.8 + 32
        weather1 = json['weather'][0]['main']
        final = [city, country, int(temp_fahrenheit), weather1]
        return final
    else: 
        print("Pease try again")


def search():
    city = city_text.get()
    weather = getweather(city)

    if weather:
        location_lbl['text'] = '{} {}'.format(weather[0], weather[1])
        temprature_lbl['text'] = str(weather[2]) + " Degree Fahrenheit"
        weather_1['text'] = weather[3]

    else:
        messagebox.showerror("error", "Cannot find {}".format(city))
    
app = Tk()

app.geometry("300x300")

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search Weather', width=16, command=search)
search_btn.pack()

location_lbl = Label(app, text='Location', font={'bold', 20})
location_lbl.pack()

temprature_lbl = Label(app, text='')
temprature_lbl.pack()

weather_1 = Label(app, text='')
weather_1.pack()

app.mainloop()
