from youtube_search import YoutubeSearch
import json
from pytube import YouTube
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from moviepy.editor import *


pathTomp4 = r"P:\spotifyvids"
pathTomp3 = r"P:\spotifysongs"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("Client ID", "Client Secret"))
username = "username"




def downloadMP4(song, singer):
    searchquery = song + ' ' + singer
    results = json.loads(YoutubeSearch(searchquery, max_results=1).to_json())
    title = str(results["videos"][0]['title'])
    title = title.replace('|', '')
    try:
        if title+".mp4" in os.listdir(pathTomp4):
            print(title, "is already downloaded.")
            return
    except FileNotFoundError:
        os.makedirs(pathTomp4)
    link = "https://www.youtube.com"+results["videos"][0]["url_suffix"]
    print(title)
    print("Downloading Now:", link)
    x = YouTube(link)
    print(x.streams.get_lowest_resolution().download(pathTomp4))

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))

def download(playlistID):
    playlist = sp.playlist(playlistID)
    for i in playlist['tracks']['items']:
        try:
            song = i['track']['name']
            artist = i['track']['artists'][0]['name']
            downloadMP4(song, artist)
        except:
            continue

def convertMP4toMP3():
    try:
        mp4list = os.listdir(pathTomp4)
    except FileNotFoundError:
        os.makedirs(pathTomp4)
    try:
        mp3list = os.listdir(pathTomp3)
    except FileNotFoundError:
        os.makedirs(pathTomp3)
    print(mp4list)
    print(mp3list)
    for mp4 in mp4list:
        if mp4[:-1]+"3" not in mp3list:
            video = VideoFileClip(os.path.join(pathTomp4+'\\'+mp4))
            video.audio.write_audiofile(os.path.join(pathTomp3+'\\'+mp4[:-1]+'3'))
def convertByPath(x):

    video = VideoFileClip(os.path.join(x))
    name = x.replace(pathTomp4, "")
    ans = input("leave name as is ? (y/n): ")
    if ans == "y":
        video.audio.write_audiofile(os.path.join(pathTomp3+name[:-1]+"3"))
    else:
        video.audio.write_audiofile(os.path.join(pathTomp3+input("Give me the name please: ")+".mp3"))


while True:
    print("Choose:\n1- Download songs of playlist!\n2- Convert from mp4 to mp3!\n3- Download from link Youtube!\n4- Convert mp4 to mp3 with full path!\n5- Exit!")
    choice = input("Enter your choice: ")
    if choice == "1":
        download(input("Please Enter the playlist ID: "))
    elif choice == "2":
        convertMP4toMP3()
    elif choice == "3":
        x = YouTube(input("Link: "))
        path = x.streams.get_lowest_resolution().download(pathTomp4)
        print(path)
        convertByPath(path)
    elif choice == "4":
        convertByPath(input("The full path please: "))
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")
