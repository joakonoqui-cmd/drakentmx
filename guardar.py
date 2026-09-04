import os
import yt_dlp


def obtener_cookies():
    if os.path.exists("cookies.txt"):
        return "cookies.txt"

    return None


def guardar_video():
    url = input("ingresar link: ")

    yt_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": "/storage/emulated/0/Pictures/videos/%(title)s.%(ext)s",
    }

    cookies = obtener_cookies()

    if cookies:
        yt_opts["cookiefile"] = cookies

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])


def guardar_audio():
    url = input("ingresar link: ")

    yt_opts = {
        "format": "bestaudio/best",
        "outtmpl": "/storage/emulated/0/Download/musica/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "0"
        }]
    }

    cookies = obtener_cookies()

    if cookies:
        yt_opts["cookiefile"] = cookies

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])


def guardar_tiktok():
    os.makedirs("/storage/emulated/0/Pictures/videos", exist_ok=True)

    url = input("link de tiktok: ")

    yt_opts = {
        "format": "best",
        "outtmpl": "/storage/emulated/0/Pictures/videos/%(title)s.%(ext)s",
    }

    cookies = obtener_cookies()

    if cookies:
        yt_opts["cookiefile"] = cookies

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])
