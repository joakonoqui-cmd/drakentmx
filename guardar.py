import yt_dlp 
def guardar_video():
    url=input("ingresar link: ")
    yt_opts={
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": "/storage/emulated/0/Pictures/videos/%(title)s.%(ext)s", # editar ruta de descarga
        
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])


def guardar_audio():
    url=input("ingresar link: ")
    yt_opts={
        "format": "bestaudio/best",
        "outtmpl":"/storage/emulated/0/Download/musica/%(title)s.%(ext)s",# editar ruta 
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "0"
        }]
        
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])



def guardar_tiktok(): #editar ruta 
    os.makedirs("/storage/emulated/0/Pictures/videos", exist_ok=True)
    url = input("link de tiktok: ")
    yt_opts = {
        "format": "best",
        "outtmpl": "/storage/emulated/0/Pictures/videos/%(title)s.%(ext)s",# editar ruta
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])
