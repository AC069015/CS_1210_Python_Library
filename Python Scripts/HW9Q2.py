# Author: Anthony Cunningham Section A01

import tkinter
import math
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode
import json


def geocodeAddress(addressString):
   urlbase = "http://maps.googleapis.com/maps/api/geocode/json?"
   args = urlencode({'address': addressString})
   url = urlbase + args
   
   resultFromGoogle = urlopen(url).read().decode('utf8')
   jsonresult = json.loads(resultFromGoogle)
   if (jsonresult['status'] != "OK"):
      return
   loc = jsonresult['results'][0]['geometry']['location']
   return (float(loc['lat']),float(loc['lng']))


def geocodeLatLng(lat, lng):
   urlbase = "http://maps.googleapis.com/maps/api/geocode/json?"
   llstring = "{},{}".format(lat,lng)
   args = urlencode({'latlng': llstring})
   url = urlbase+args
   resultFromGoogle = urlopen(url).read().decode('utf8')
   jsonresult = json.loads(resultFromGoogle)
   if (jsonresult['status'] != "OK"):
      print("Status returned from geocoder *not* OK: {}".format(jsonresult['status']))
      return
   loc = jsonresult['results'][0]['formatted_address']
   return loc


def getMapUrl(width, height, lat, lng, zoom, maptype):
   urlbase = "http://maps.google.com/maps/api/staticmap?"
   params = "center={},{}&zoom={}&size={}x{}&maptype={}&format=gif&markers=color:red|size:tiny|{},{}".format(lat,lng,zoom,width,height,maptype,lat,lng)
   return  urlbase+params


def retrieveMap():
   lat, lng = geocodeAddress(mapLocation)
   url = getMapUrl(mapSize, mapSize, lat, lng, zoomLevel, mapType)
   urlretrieve(url, mapFileName)
   return mapFileName


rootWindow = None
mapLabel = None

defaultLocation = "Mauna Kea, Hawaii"
mapLocation = defaultLocation
mapFileName = 'googlemap.gif'
mapSize = 400
zoomLevel = 9
mapType = 'roadmap'
#
#
# Need to press the show map button after changing an aspect of the map to redisplay it.
#
#
def zoomInFunc():
   global zoomLevel
   if zoomLevel >= 21:
      zoomLevel = zoomLevel
   else:
      zoomLevel = zoomLevel + 1
   print(zoomLevel)

def zoomOutFunc():
   global zoomLevel
   if zoomLevel <= 0:
      zoomLevel = zoomLevel
   else:
      zoomLevel = zoomLevel - 1
   print(zoomLevel)

def switchMapTypeRoadMap():
   global mapType
   if mapType == 'satellite':
      mapType = 'roadmap'
   elif mapType != 'roadmap':
      mapType = 'roadmap'

def switchMapTypeSatMap():
   global mapType
   if mapType == 'roadmap':
      mapType = 'satellite'
   elif mapType != 'satellite':
      mapType = 'satellite'
      
def readEntryAndShowMap():
   global mapLocation
   global mapEntry
   mapLocation = mapEntry.get()
   showMap()
    
def showMap():
   retrieveMap()    
   mapImage = tkinter.PhotoImage(file=mapFileName)
   mapLabel.configure(image=mapImage)
   mapLabel.mapImage = mapImage  
  
def initializeGUIetc():
   global rootWindow
   global mapLabel
   global mapEntry

   rootWindow = tkinter.Tk()

   mainFrame = tkinter.Frame(rootWindow) 
   mainFrame.pack()

   entryLabel = tkinter.Label(mainFrame, text="Enter a location:")
   entryLabel.pack()
   mapEntry = tkinter.Entry(mainFrame)
   mapEntry.pack()
   readEntryAndShowMapButton = tkinter.Button(mainFrame, text="Show me the map!", command=readEntryAndShowMap)
   readEntryAndShowMapButton.pack()
   zoomLabel = tkinter.Label(mainFrame, text="Zoom")
   zoomLabel.pack()
   # Zoom button work as long as you press the show map button to redisplay.
   # The zoom level is shown in the shell.
   #
   # Need to type in a location into the entry widget before redisplaying the map
   # with an altered zoom level (ex. Type in "Mauna Kea" before redisplaying instead of leaving
   # the entry eidget blank)
   zoomIn = tkinter.Button(mainFrame, text="+", command=zoomInFunc)
   zoomIn.pack()
   zoomOut = tkinter.Button(mainFrame, text="-", command=zoomOutFunc)
   zoomOut.pack()

   # Same thing with radiobuttons; need to click on the show map button to redisplay the map
   # with different map type. Also can't leave entry widget blank.
   choiceVar = tkinter.IntVar()
   roadMapType = tkinter.Radiobutton(mainFrame, text='Road Map', variable=choiceVar, value=1, command=switchMapTypeRoadMap)
   roadMapType.pack(side='bottom')
   satMapType = tkinter.Radiobutton(mainFrame, text='Satellite Map', variable=choiceVar, value=2, command=switchMapTypeSatMap)
   satMapType.pack(side='bottom')

   mapLabel = tkinter.Label(mainFrame, width=mapSize, bd=2, relief=tkinter.FLAT)
   mapLabel.pack()

def startGUI():
    initializeGUIetc()
    showMap()
    rootWindow.mainloop()

