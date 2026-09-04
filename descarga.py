import yt_dlp

import os

from guardar import guardar_video, guardar_tiktok, guardar_audio

ruta1="/storage/emulated/0/Download/musica"

ruta2="/storage/emulated/0/Pictures/videos"

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
            print("")        
            if not os.listdir(ruta1) and not os.listdir(ruta2): 
                print("no hay canciones descargadas")
            else:
                print("archivos descargados ✅✅")
                print("")
                print("canciones descargadas 🎵🎵") 
                for archivo in os.listdir(ruta1):
                    print(archivo)
                print("")
                print("videos descargados 🎥🎥") 
                for archivo in os.listdir(ruta2):
                    print(archivo)




            # FLUJO DE VIDEO



        elif op=="5":
            print("")
            archivos=os.listdir(ruta2)
            for i,archivo in enumerate(archivos,1):
                print(f"{i}-{archivo}")
            opcion=input("elija que borrar: ")
            if opcion.isdigit():
                opcion=int(opcion)
                if 1<= opcion <=len (archivos):
                    archivo_a_borrar=archivos[opcion - 1]
                    confirmar=input(f"seguro que quieres borrar {archivo_a_borrar}? si/no: ")
                    if confirmar.lower()=="si":
                       os.remove(os.path.join(ruta2,archivo_a_borrar))
                       print(f"{archivo_a_borrar} borrado ✅")
                    elif confirmar.lower()=="no":
                        print("operacion cancelada")
                else:
                    print("opcion invalida")
            else: 
                print("solo digitos")



                #FLUJO DE AUDIO



        elif op=="6":
            print("")
            archivos=os.listdir(ruta1)
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
                        os.remove(os.path.join(ruta1,borrar))
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

