from googleapiclient.discovery import build

# Set up the YouTube Data API client
youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')

# Call the API to retrieve comments for a specific video
request = youtube.commentThreads().list(
    part='snippet',
    videoId='YOUR_VIDEO_ID',
    maxResults=100  # Adjust as needed
)
response = request.execute()

# Extract comments from the response
comments = [item['snippet']['topLevelComment']['snippet']['textOriginal'] for item in response['items']]
