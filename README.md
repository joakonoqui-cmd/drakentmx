DrakenTMX

Descargador multimedia hecho en Python para Termux.

Permite descargar:

- Videos de YouTube
- Videos de TikTok
- Audio de YouTube en MP3
- Administrar los archivos descargados
- Eliminar videos y audios desde el propio programa

Requisitos

- Android
- Termux
- Python 3
- yt-dlp
- FFmpeg

Instalación

Cloná el repositorio:

git clone URL_DEL_REPOSITORIO

Entrá a la carpeta:

cd DrakenTMX

Instalá las dependencias:

pip install -r requirements.txt

Dale permiso de almacenamiento a Termux:

termux-setup-storage

Cookies de YouTube

Algunas descargas de YouTube pueden requerir autenticación debido a restricciones anti-bot.

En ese caso, necesitás utilizar tus propias cookies.

Guardá el archivo con el nombre:

cookies.txt

y colocá el archivo en:

/storage/emulated/0/Download/cookies.txt

DrakenTMX buscará automáticamente el archivo en Downloads.

Importante

NO compartas tu "cookies.txt".

Las cookies pueden contener información de sesión de tu cuenta. Cada usuario debe utilizar sus propias cookies.

El archivo "cookies.txt" tampoco debe subirse al repositorio.

Uso

Ejecutá:

python descarga.py

Aparecerá el menú principal:

1-youtube
2-tiktok
3-musica
4-ver archivos descargados
5-eliminar videos
6-eliminar audios
7-salir

Elegí una opción y seguí las instrucciones del programa.

Estructura

DrakenTMX/
├── descarga.py
├── guardar.py
├── requirements.txt
├── README.md
└── .gitignore

El archivo "cookies.txt" es externo al proyecto y no debe incluirse en el repositorio.

Aviso

Este proyecto utiliza "yt-dlp" para realizar las descargas.

Utilizá DrakenTMX respetando los términos de servicio y los derechos de autor correspondientes.

Autor

Draken