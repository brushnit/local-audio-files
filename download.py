from yt_dlp import YoutubeDL

"""
URLS = [
    #"https://youtu.be/zSnbp0z-FGg",
    #"https://youtu.be/QmR4zLcORNc",
]
"""

PLAYLIST_URL = "https://youtube.com/playlist?list=PLCxm20_O6DW6T4P_JwahQiBja69JidLi2"

opts = {
    "format": "m4a/bestaudio/best",
    "outtmpl": "music/%(title)s.%(ext)s",
    "windowsfilenames": True,
    "ignoreerrors": True,
    "keepvideo": False, 
    "cookiesfrombrowser": ("firefox",),
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        'preferredcodec': 'm4a',
        "preferredquality": "128",     # kbps
        "nopostoverwrites": True,      # skip conversions that already exist
    }],
}

with YoutubeDL(opts) as ydl:
    ydl.download([PLAYLIST_URL])