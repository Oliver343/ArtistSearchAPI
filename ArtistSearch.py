import requests

# Enter Spotify web API access token credentials below
# If you don't have them you can get them here:
# https://developer.spotify.com/dashboard/applications
client_id = "YOUR_CLIENT_ID_HERE"
client_secret = "YOUR_SECRET_ID_HERE"

# The below code generates a temporary access token using the credentials
# entered above through the Spotify web API
raw_response = requests.post('https://accounts.spotify.com/api/token', {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})

print(raw_response)
# Converts the response to json
json_response = raw_response.json()

# Checks response code and runs search if connection made,
# otherwise tries to provide useful advice.
if raw_response.status_code == 200:
    print("Connection established and authorised.")

    # Asks user for an artist. The artists information is then retrieved from
    # the Spotify web API.
    artist_name = input("Please enter an artist: ")

    # Checks if nothing has been entered by user and provides default answer
    if artist_name == "":
        print("No artist entered, so you will be provided Justin Bieber instead.")
        artist_name = "Justin Bieber"

    artist_info = requests.get('https://api.spotify.com/v1/search',
                               headers={'authorization': "Bearer " + json_response['access_token']},
                               params={'q': artist_name, 'type': 'artist'})

    # Converts the artist_info to json
    artist_info = artist_info.json()
    # Prints artists name rating and a link to them on Spotify
    print("You have selected: {}  \nThis artist has a popularity of {}%".format(artist_info["artists"]["items"][0]["name"], artist_info["artists"]["items"][0]["popularity"]) )
    print(artist_info["artists"]["items"][0]["external_urls"]["spotify"])

elif raw_response.status_code == 400:
        print("Unable to connect. This is most likely due to "
              "invalid 'client_id' or 'client_secret'.")
        print("For more information check the website: "
              "'https://developer.spotify.com/documentation/general/guides/authorization/'")
# Any other response code grouped here, can add more to this later.
else:
    print("Unable to connect. Error unknown.")
