DrakenTMX

Panel de descargas multimedia para Termux + Python.

Permite descargar contenido de YouTube y TikTok, convertir audio a MP3 y administrar los archivos descargados directamente desde el menú.

Características

- Descarga de videos de YouTube
- Descarga de videos de TikTok (Sin marca de agua) 
- Descarga de audio en MP3
- Conversión automática mediante FFmpeg
- Visualización de archivos descargados
- Eliminación de videos y audios
- Soporte para "cookies.txt" de YouTube
- Diseñado para Termux en Android

Requisitos

- Android
- Termux
- Python 3
- yt-dlp
- FFmpeg

Instalación

Actualizá los paquetes:

pkg update && pkg upgrade -y

Instalá Python, Git y FFmpeg:

pkg install python git ffmpeg -y

Cloná el repositorio:

git clone https://github.com/joakonoqui-cmd/drakentmx.git

Entrá a la carpeta:

cd drakentmx

Instalá yt-dlp:

pip install yt-dlp

Dale acceso al almacenamiento a Termux:

termux-setup-storage

Ejecutar

Iniciá el programa con:

python descarga.py

Aparecerá el menú:

1-youtube
2-tiktok
3-musica
4-ver archivos descargados
5-eliminar videos
6-eliminar audios
7-salir

Cookies de YouTube

Algunas veces YouTube puede bloquear las solicitudes o pedir autenticación.

En ese caso, DrakenTMX puede utilizar un archivo "cookies.txt" con las cookies de tu propia cuenta/sesión.

Guardá el archivo con este nombre:

cookies.txt

y colocálo en:

/storage/emulated/0/Download/cookies.txt

DrakenTMX buscará automáticamente el archivo en la carpeta "Download".

Importante

Nunca compartas tu "cookies.txt".

Este archivo puede contener información que permita acceder a tu sesión. Cada usuario debe utilizar sus propias cookies.

"cookies.txt" tampoco debe subirse a GitHub.

Si no sabes descargar tus cookies, instala kiwi browser y diríjase a los tres punto de la barra superior derecha. Instala la extensión "Cookie.txt"

Una vez descargado vaya a Youtube.com y y logeate con tu cuenta, luego que hayas iniciado sesion en los tres puntos de arriba a la derecha busca la extensión descargada y pon "Current Site" y listo, su cookie será añadida a su carpeta de descargas para su instalación en DrakenTMX

Estructura

drakentmx/
├── descarga.py
├── guardar.py
├── README.md
└── .gitignore

El archivo "cookies.txt" se mantiene fuera del repositorio.

Uso responsable

DrakenTMX utiliza "yt-dlp" para realizar las descargas.

Utilizá la herramienta respetando los términos de servicio de las plataformas y los derechos de autor correspondientes.

Autor

Joako Noqui

GitHub: https://github.com/joakonoqui-cmd

---

Si te gusta el proyecto, dejá una estrella en el repositorio.
