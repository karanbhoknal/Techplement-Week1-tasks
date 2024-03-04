1.Create a folder

On command promt hit this command= mkdir weather

2.To follow this command [pip install pipenv] => It's very importent to keep all packages & dependencies isolated inside your project instead of mixing with your global file system

3.To follow this command [pipenv shell ] =>(Activate the virual enviorment using pipenv shell )

4.The next command follow [pipenv install argparse] =>Basically make it easy to write user freindly command line interface to your python program.it is also allows to define the argument that your program can accpet & provides a help message It has access to different method or classes

5.Follow this command [pipenv install pyfiglet]=>Used for for creating ASCCI R text from normal text

6.Follow this last command [pipenv install simple_chalk] =>[[ We said provides just a simple way to add color text to your python program & it can also be used to highlight ceratin pieces of output or some visual varity to your console

This is file name[main.py]
import argparse

import pyfiglet

from simple_chalk import chalk

import requests

API key for openweathmap
API key you need to call by to weather map
API_KEY="e3bd52a906bb0aa80fd7bc5d84de43f3"

Base URL for openweathermap API
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

Map the weather codes to weather icon
WEATHER_ICONS={ #day icons "01d": "🌞",

"02d": "⛅",

"03d": "☁",

"04d": "☁",

"09d": "🌨",

"10d": "🌦",

"11d": "⛈",

"13d": "🌨",

"50d": "🌫",

#night icons "01d": "🌙",

"02d": "☁",

"03d": "☁",

"04d": "☁",

"09d": "🌨",

"10d": "🌦",

"11d": "⛈",

"13d": "🌨",

"50d": "🌫",

}

Construct API URL with query parameters
parser =argparse.ArgumentParser(description="check the weather for a certaint city")

parser.add_argument("city",help="The city to check the weather for")

args=parser.parse_args()

url=f"{BASE_URL}?q={args.city}&appid={API_KEY}&units=metric"

Make API request and parse response using request module
response=requests.get(url)

if response.status_code !=200:

print(chalk.red("Error:Unable to retrive weather information"))

exit()
parsing the JSON response from the API and extract the weather information
data= response.json()

Get information from response
temprature = data["main"]["temp"]

feels_like = data["main"]["feels_like"]

description=data["weather"][0]["description"]

icon = data["weather"][0]["icon"]

city=data["name"]

Construct the output with weather icons
weather_icon = WEATHER_ICONS.get(icon,"")

output = f"{pyfiglet.figlet_format(city)}\n\n"

output += f"{weather_icon} {description}\n"

output += f"Temprature:{temprature}°C\n"

output += f"fell like:{feels_like}°C\n"

print the output
print(chalk.green(output))

How we can run this code on terminal
1.pyhton main.py city name

Ex => python main.py nashik

