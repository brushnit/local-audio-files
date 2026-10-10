# https://frontend-practical.dev
# https://github.com/varunmaurya-git/Master-Pro-Audio-Analyzer
# https://github.com/likethemammal/css-visualizer
# https://codepen.io/Hyperplexed/pen/MOoQyO
# https://codepen.io/k-ivan/pen/pJMLmJ 
# https://codepen.io/serversideup/pen/Vwrgoea
# https://codepen.io/editor/gregh/pen/015ab7f9-6bc8-7ac0-a718-d2c6645bf11e
# https://codepen.io/broregard/pen/ReBozG  wow!
# https://codepen.io/NiklasKnaack/pen/Qxrmpz
# https://codepen.io/one20/pen/zBGPpb
# https://codepen.io/devildrey33/pen/PWVPag
# https://codepen.io/JoshuaVB/pen/poWQNaJ
# https://codepen.io/ecemgo/pen/vYPadZz
# https://codepen.io/ma77os/pen/xxyywo

from yt_dlp import YoutubeDL

URLS = [
    #"https://youtu.be/zSnbp0z-FGg",
    "https://youtu.be/QmR4zLcORNc",
]

# One pass per format: yt-dlp runs postprocessors in a chain (a second FFmpegExtractAudio would
# re-encode the first one's output), so each gets its own run. Pass 2 finds the source already
# downloaded and only converts it.
for codec in ("mp3", "m4a"):  # m4a = AAC in an .m4a container
    with YoutubeDL({
        "format": "bestaudio/best",
        "outtmpl": "music/%(title)s.%(ext)s",
        "noplaylist": True,
        "ignoreerrors": True,      # a failed URL doesn't stop the rest
        "keepvideo": True,         # keep the original best-quality download next to the conversions
        "cookiesfrombrowser": ("firefox",),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": codec,
            "preferredquality": "128",     # kbps
            "nopostoverwrites": True,      # skip conversions that already exist
        }],
    }) as ydl:
        ydl.download(URLS)