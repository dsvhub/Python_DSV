from tkinter import *
from PIL import ImageTk, Image
import requests
import json

import os
os.system('clear')

root = Tk()
root.title('Air Quality App')
root.iconbitmap("C:/Users/nemes/Documents/My_Files/MyCodes/Media/dsvarietyhublogo1.ico")
root.geometry("500x100")

# Create Zipcoce Lookup Function
def zipLookup():
	#zip.grid(row=0, column=1, columnspan=2)
	#zipLabel = Label(root, text=zip.get())
	#zipLabel.grid()

	try:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode= " + zip.get() + "&distance=25&API_KEY=4E0A1EC5-6065-4448-A721-A53FF192D564")
		api = json.loads(api_request.content)
		city = api[0]['ReportingArea']
		quality = api[0]['AQI']
		category = api[0]['Category']['Name']

		if category == "Good":
			weather_color ="#0c0"
		elif category == "Moderate":
			weather_color = "#FFFF00"
		elif category == "Unhealthy for Sensitive Groups":
			weather_color = "#ff9900"
		elif category == "Unhealthy":
			weather_color = "#FF0000"
		elif category == "Very Unhealthy":
			weather_color = "#990066"
		elif category == "Hazardous":
			weather_color = "#660000"

		root.configure(background=weather_color)

		myLabel1 = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
		myLabel1.grid(row=1, column=0, columnspan=2)
	except Exception as e:
		api = "Error..."

##My Airnow API URL Link##
# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=11234&distance=25&API_KEY=4E0A1EC5-6065-4448-A721-A53FF192D564

zip = Entry(root, relief=SUNKEN)
zip.grid(row=0, column=0, stick=W+E+N+S)


zipButton = Button(root, text="Press For Result", relief=RAISED, fg='yellow', font='arial', bg='brown', command=zipLookup)
zipButton.grid(row=0, column=1, stick=W+E+N+S)


root.mainloop()