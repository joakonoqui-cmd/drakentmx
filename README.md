
# DrakenTMX

Panel de descargas para Termux que permite descargar contenido desde YouTube y TikTok sin marca de agua, además de convertir audio a MP3.

## ¿Qué hace?

DrakenTMX reúne varias funciones en un solo menú:

- Descargar videos de YouTube
- Descargar videos de TikTok
- Descargar música en formato MP3
- Ver los archivos descargados
- Eliminar videos
- Eliminar audios

Los archivos se guardan directamente en el almacenamiento del dispositivo Android.

## Requisitos

- Android
- Termux
- Python 3
- yt-dlp
- FFmpeg
- rutas:
- /storage/emulated/0/Download/musica
- /storage/emulated/0/Pictures/videos
- En caso que no tengas la misma ruta, deje indicaciones en donde editar dentro del Script 

## Instalación

Primero instala Termux y dale acceso al almacenamiento:


```bash
termux-setup-storage

Actualiza los paquetes:

pkg update && pkg upgrade -y

Instala Python, Git y FFmpeg:

pkg install python git ffmpeg -y

Clona el repositorio:

git clone https://github.com/joakonoqui-cmd/drakentmx.git

Entra en la carpeta:

cd drakentmx

Instala yt-dlp:

pip install yt-dlp

Ejecuta el programa:

python descarga.py





Uso

Al iniciar el programa aparecerá un menú con las diferentes opciones.

Selecciona una opción introduciendo el número correspondiente y después proporciona el enlace del contenido que quieras descargar.

Funciones

YouTube

Permite descargar videos de YouTube utilizando la mejor calidad disponible.

TikTok

Permite descargar videos de TikTok.

Música

Permite descargar el audio de un enlace y convertirlo a formato MP3.

Ver archivos descargados

Muestra los videos y audios que se encuentran guardados en el dispositivo.

Eliminar videos

Permite seleccionar y eliminar videos descargados.

Eliminar audios

Permite seleccionar y eliminar archivos de audio descargados.

Carpetas

Los archivos se guardan en las siguientes ubicaciones:

Videos:

/storage/emulated/0/Pictures/videos

Música:

/storage/emulated/0/Download/musica

Tecnologías utilizadas

Python

yt-dlp

FFmpeg

Termux


Autor

Joako Noqui

GitHub: https://github.com/joakonoqui-cmd

Nota

Este proyecto fue creado para utilizar herramientas de descarga directamente desde Termux en Android.

Utiliza las herramientas de forma responsable y respeta los derechos de autor y las condiciones de uso de cada plataforma.


---

Si te gustó el proyecto, puedes dejar una estrella al repositorio.
