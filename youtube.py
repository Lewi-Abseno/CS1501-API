from googleapiclient.discovery import build

api_key = 'AIzaSyBicT7oAD0GDUm67LavNHwdi0KI4gCiavs'
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(part='statistics', 
                                channelId="UC9qkQ1s5iWY6PzYZ5BiD-tQ")
                    
pl_request = youtube.playlists().list(part='contentDetails, snippet', playlistId="UC9qkQ1s5iWY6PzYZ5BiD-tQ")

response = request.execute()
response_pl = pl_request.execute()

print(response)
print(response_pl)
