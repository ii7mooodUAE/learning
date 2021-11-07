from pytube import YouTube
from pytube.cli import on_progress #Progress bar
import subprocess, os, requests

#sp for running commands
#os to move files
#requests to get video thumbnail image


videoUrl = str(input("Enter URL \n"))
invalidChar = ['/', '\\', ':', '?', '*', '"', '<', '>', '|'] #list of invalid chars for windows fileName
yt = YouTube(videoUrl, on_progress_callback=on_progress) #Youtube object, on_progress for progress bar
response = input("--- \n1 - Video \n2 - Audio \n3 - Thumbnail \n--- \n") #File type

def ValidateName(fileName):
    for x in range(len(invalidChar)):
        fileName = fileName.replace(invalidChar[x], '') #remove invalid chars
    return fileName


if int(response) == 1:
    video = yt.streams.get_highest_resolution().download(filename=f'{ValidateName(yt.title)}.mp4', #gets the highest reso video, calls function to remove invalidchars from yt.title
                                                        output_path=os.path.expanduser('~')+'\\Desktop') #downloads it at Desktop
    
elif int(response) == 2:
    audio = yt.streams.filter(only_audio=True).first().download(filename=f'{ValidateName(yt.title)}.mp3', #gets audio-only file, calls function to remove invalidchars from yt.title
                                                        output_path=os.path.expanduser('~')+'\\Desktop') #downloads it at desktop as .mp3
    
elif int(response) == 3:
    with open(os.path.expanduser('~')+f'\\Desktop\\{ValidateName(yt.title)+".jpg"}', "wb+") as fp: #calls ValidateName function to validate yt.title before creating it at Desktop
        fp.write(requests.get(yt.thumbnail_url, stream=True).raw.read()) #uses requests to get yt.thumbnail_urls 's raw data and writes it to the file created ^ (fp)
    
else:
    print("invalid option")


input("Download completed, press any button to quit....")
