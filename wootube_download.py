
#?----------------------------------------------------------------------------
#? Author   |   Ryan Woodward
#?----------------------------------------------------------------------------


#?----------------------------------------------------------------------------
#?                  IMPORTS
#?----------------------------------------------------------------------------

import yt_dlp as youtube_dl
import time

#?----------------------------------------------------------------------------
#?                  VARIABLES
#?----------------------------------------------------------------------------


#?----------------------------------------------------------------------------
#?                  FUNCTIONS
#?----------------------------------------------------------------------------

def init_wootube_download():
    
    userSelection = ""

    while(userSelection != 'X' or userSelection != 'x'):
        print("---------------------------------------\n\t Welcome to Wootube Downloader \n---------------------------------------")
        print("\t Are you downloading: \n\t\t A.) MP3 \n\t\t B.) MP4 \n\t\t X.) Exit the Program")

        userSelection = input()

        if (userSelection == 'A'):
            download_mp3()
        elif (userSelection == 'B'):
            download_mp4()
        elif (userSelection == 'X' or userSelection == 'x'):
            print("Exiting the Program... Auf Wiedersehen!")
        else:
            print("ERROR: Invalid entry. Please enter a valid character....")
 

"""

"""
def download_mp3():
    
    def download_audio(url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'video')
            print(f"Downloading: {video_title}")
            ydl.download([url])
            print(f"{video_title} downloaded as MP3 successfully!")
            time.sleep(3)

    try:
        video_url = input("Enter the video URL: ")
        download_audio(video_url)
    except:
        print("There was some error while attempting to download the video to audio")
        time.sleep(3)
        return

"""

"""
def download_mp4():
    def download_video(url):
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'video')
            print(f"Downloading: {video_title}")
            ydl.download([url])
            print(f"{video_title} downloaded successfully!")
            time.sleep(3)
    
    try:
        video_url = input("Enter video URL: ")
        download_video(video_url)
    except:
        print("There was an error while attempting to download the video")
        time.sleep(3)
        return

#?----------------------------------------------------------------------------
#?                  ENTRY POINT
#?----------------------------------------------------------------------------
init_wootube_download()





