
from pytube import YouTube
import pandas as pd


def descargar_audio_youtube(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    destino = "temp_audio"
    out_file = video.download(output_path=destino)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


url = "https://youtu.be/PnPvdpJtyEY"

audio_file, detalles_video = descargar_audio_youtube(url)
