import requests
import webbrowser

def openMap(postcode):
  """verifies a postcodes value, gets lat and lon from postcodes.io, opens google maps with lat and lon"""
  
  # gets url for postcodes.io website
  url = "https://api.postcodes.io/postcodes/" + postcode
  response = requests.get(url)

  # response code 200: success
  if response.status_code == 200:

    # grabs the latitude and longitude 
    latitude = response.json()["result"]["latitude"]
    longitude = response.json()["result"]["longitude"]
    print(latitude, longitude)

    # opens google maps in accordance with the lon / lat - does not work
    googleMaps = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
    webbrowser.open(googleMaps)
    print(googleMaps)

  else:
    print("Postcode does not exist.")

openMap("BB102EE") 
