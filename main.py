import argparse
import pyfiglet
from simple_chalk import chalk
import requests

#API key for openweathmap
API_KEY="e3bd52a906bb0aa80fd7bc5d84de43f3"


# Base URL for openweathermap API
BASE_URL="https://api.openweathermap.org/data/2.5/weather"


#Map the weather codes to weather icon
WEATHER_ICONS={
    #day icons
   "01d": "🌞",
   "02d": "⛅",
   "03d": "☁",
   "04d": "☁",
   "09d": "🌨",
   "10d": "🌦",
   "11d": "⛈",
   "13d": "🌨",
   "50d": "🌫",
   
   #night icons
   "01d": "🌙",
   "02d": "☁",
   "03d": "☁",
   "04d": "☁",
   "09d": "🌨",
   "10d": "🌦",
   "11d": "⛈",
   "13d": "🌨",
   "50d": "🌫",
   
   
}
#Construct API URL with query parameters
parser =argparse.ArgumentParser(description="check the weather for a certaint city")
parser.add_argument("city",help="The city to check the weather for")
args=parser.parse_args()
url=f"{BASE_URL}?q={args.city}&appid={API_KEY}&units=metric"

#Make API request and parse response using request module
response=requests.get(url)
if response.status_code !=200:
    print(chalk.red("Error:Unable to retrive weather information"))
    exit()

# parsing the JSON response from the API and extract the weather information
data= response.json()

# Get  information from response 
temprature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description=data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city=data["name"]



# Cnstruct the output with weather icons
weather_icon = WEATHER_ICONS.get(icon,"")
output = f"{pyfiglet.figlet_format(city)}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temprature:{temprature}°C\n"
output += f"fell like:{feels_like}°C\n"

#print the output
print(chalk.green(output))



