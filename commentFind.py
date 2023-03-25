from pytube import YouTube
import ssl
import pandas
from googleapiclient.discovery import build
import os
import time

nameList = {}
def videoEdit(data):
    print(data[3])
    url = 'www.youtube.com/watch?v=' + data[0]
    yt = YouTube(url)
    down_clip = yt.streams.get_highest_resolution().download(save_folder)
    if data[0] in nameList.keys():
        nameList[data[0]] += 1
    else:
        nameList[data[0]] = 0
    os.rename(down_clip, f'/Users/realizer/Documents/youtubeDown/{data[0]}_original_{nameList[data[0]]}.mp4')
    time.sleep(2)
    os.system(f"ffmpeg -i /Users/realizer/Documents/youtubeDown/{data[0]}_original_{nameList[data[0]]}.mp4 -ss {str(data[1])} -to {str(data[1] + 7)} /Users/realizer/Documents/youtubeDown/{data[0]}_shorts_{nameList[data[0]]}.mp4")

def videoId(api_obj, playlistId):
    comments = []
    response = api_obj.playlistItems().list(
        part="snippet",
        playlistId=playlistId,
        maxResults=20
    ).execute()
    while len(comments) < 5:
        for data in response["items"]:
            comments = comment(api_obj, data["snippet"]["resourceId"]["videoId"], comments)

        if 'nextPageToken' in response:
            response = api_obj.playlistItems().list(part='snippet', playlistId=playlistId,
                                                     pageToken=response['nextPageToken'], maxResults=20).execute()
        else:
            break
    for data in comments:
        videoEdit(data)

def comment(api_obj, video_id, comments):
    response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, maxResults=100).execute()
    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            if '&amp;t=' in comment['textDisplay'] and comment['likeCount'] >= 2:
                checkList = comment['textDisplay'].split("\"")
                if len(checkList) == 3:
                    temp = checkList[1].split('&amp;t=')
                    tempSecList = temp[1].split('m')
                    sec = int(tempSecList[0]) * 60 + int(tempSecList[1][:-1]) - 3
                    commentUrl = f"https://www.youtube.com/watch?v={video_id}&t={str(sec)}s"
                    comments.append(
                        [video_id, sec, commentUrl, comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'],
                         comment['likeCount']])
        if 'nextPageToken' in response:
            response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id,
                                                     pageToken=response['nextPageToken'], maxResults=100).execute()
        else:
            break

    return comments

ssl._create_default_https_context = ssl._create_stdlib_context

save_folder = "/Users/realizer/Documents/youtubeDown"

url = "https://www.youtube.com/watch?v=CEYTp0-pRQs"

api_key = 'AIzaSyBfz_p4lfNqouo2TEw-4UDZIYaJN3HvDSU'
# video_id = video_id = url.split('v=')[1]

comments = list()
api_obj = build('youtube', 'v3', developerKey=api_key)

# playlists
# response = channels_response = api_obj.channels().list(
#   part="contentDetails",
#   id="UC3DYSay178fMMPaf3zHwECA"
# ).execute()


# 채널아이디
# response = channels_response = api_obj.videos().list(
#   part="snippet",
#   id="MYknwSKzMao"
# ).execute()
# print(response["items"][0]["snippet"]["channelId"])

# href="/watch?v=CEYTp0-pRQs&t=164s"

videoId(api_obj, 'UU7nVGqibbYgrzh733LDffNQ')

# print(response["items"])

# UU7nVGqibbYgrzh733LDffNQ

# 비디오 아이디, 시간