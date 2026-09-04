import yt_dlp
import os
from guardar import guardar_video
from guardar import guardar_audio
from guardar import guardar_tiktok
menu=["youtube","tiktok","musica","ver archivos descargados","eliminar videos","eliminar audios","salir"]


# MENU


def down():
    while True:
        print("bienvenido al menu de descargas 👾")
        for posicion,opcion in enumerate(menu,start=1):
            print("")
            print(f"{posicion}-{opcion}")
        op=input("> ")
        print("")



        if op=="1":
            print("")
            try:
                guardar_video()
                print("descarga completa ✅✅") 
            except:
                print("error al descargar 🥀")
                print("")




        elif op=="2":
            print("")
            try:
                guardar_tiktok()
                print("descarga completa ✅✅")
            except:
                print("error al descargar 🥀")
                print("")





        elif op=="3":
            print("")
            try:
                guardar_audio()
                print("descargado con exito ✅✅")
            except:
                print("fallo al descargar ❌❌")
        elif op=="4":
            print("")         # Editar esta ruta con la suya.
            if not os.listdir("/storage/emulated/0/Download/musica") and not os.listdir("/storage/emulated/0/Pictures/videos"): # esta igual
                print("no hay canciones descargadas")
            else:
                print("archivos descargados ✅✅")
                print("")
                print("canciones descargadas 🎵🎵") #editar ruta
                for archivo in os.listdir("/storage/emulated/0/Download/musica"):
                    print(archivo)
                print("")
                print("videos descargados 🎥🎥") #editar ruta
                for archivo in os.listdir("/storage/emulated/0/Pictures/videos"):
                    print(archivo)




            # FLUJO DE VIDEO



        elif op=="5":
            print("")# Editar ruta
            ruta="/storage/emulated/0/Pictures/videos"
            archivos=os.listdir(ruta)
            for i,archivo in enumerate(archivos,1):
                print(f"{i}-{archivo}")
            opcion=input("elija que borrar: ")
            if opcion.isdigit():
                opcion=int(opcion)
                if 1<= opcion <=len (archivos):
                    archivo_a_borrar=archivos[opcion - 1]
                    confirmar=input(f"seguro que quieres borrar {archivo_a_borrar}? si/no: ")
                    if confirmar.lower()=="si":
                       os.remove(os.path.join(ruta,archivo_a_borrar))
                       print(f"{archivo_a_borrar} borrado ✅")
                    elif confirmar.lower()=="no":
                        print("operacion cancelada")
                else:
                    print("opcion invalida")
            else: 
                print("solo digitos")



                #FLUJO DE AUDIO



        elif op=="6":
            print("")# Editar ruta
            ruta="/storage/emulated/0/Download/musica"
            archivos=os.listdir(ruta)
            for i,archivo in enumerate (archivos,1):
                print(f"{i}-{archivo}")
                print("")

            opcion=input("elija que borrar: ")
            print("")
            if opcion.isdigit():
                opcion=int(opcion)
                if 1<= opcion <=len(archivos):
                    borrar=archivos[opcion -1]
                    confirmar=input(f"seguro que quiere borrar {borrar}? si/no: ")
                    print("")
                    if confirmar.lower()=="si":
                        os.remove(os.path.join(ruta,borrar))
                        print(f"{borrar} borrado")
                    elif confirmar.lower()=="no":
                        print("operacion cancelada")
                else:
                    print("invalido")
            else:
                print("solo digitos")



        elif op=="7":
            print("saliendo")
            break
        else:
            print("opcion invalida")
down()

