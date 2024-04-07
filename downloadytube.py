# pip install yt-dlp
import yt_dlp

url = input("Ingrese la URl del Video: ")
ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.dowload([url])
print("Video descargado satisfactoriamente!")
