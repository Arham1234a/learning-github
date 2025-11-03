from googleapiclient.discovery import build
import isodate

api_key = "AIzaSyCuSBIYk6yF1vIVcpUTdryrqQOaZf-lX0o"  # 👈 apni key yaha paste karo
playlist_id = "PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn"

youtube = build('youtube', 'v3', developerKey=api_key)

total_seconds = 0
next_page_token = None

while True:
    pl_request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    )
    pl_response = pl_request.execute()

    video_ids = [item['contentDetails']['videoId'] for item in pl_response['items']]

    vid_request = youtube.videos().list(
        part="contentDetails",
        id=",".join(video_ids)
    )
    vid_response = vid_request.execute()

    for item in vid_response['items']:
        duration = isodate.parse_duration(item['contentDetails']['duration'])
        total_seconds += duration.total_seconds()

    next_page_token = pl_response.get('nextPageToken')
    if not next_page_token:
        break

hours = int(total_seconds // 3600)
minutes = int((total_seconds % 3600) // 60)

print(f"Total Playlist Duration: {hours} hours {minutes} minutes")
