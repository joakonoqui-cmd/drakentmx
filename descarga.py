import yt_dlp

import os

from guardar import guardar_video, guardar_tiktok, guardar_audio

ruta1="/storage/emulated/0/Download/musica"

ruta2="/storage/emulated/0/videos"

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
            try:
                guardar_video()
                print("descarga completa ✅✅") 
                print("")
            except Exception as e:
                print(f"error 🥀{e}")
                print("")




        elif op=="2":
            try:
                guardar_tiktok()
                print("descarga completa ✅✅")
                print("")
            except Exception as e:
                print(f"error{e}")
                print("")





        elif op=="3":
            try:
                guardar_audio()
                print("descargado con exito ✅✅")
                print("")
            except Exception as e:
                print(f"fallo ❌❌{e}")
                print("")
        elif op=="4":
            print("")       
            if not os.path.exists(ruta1) and not os.path.exists(ruta2):
                print("no hay canciones descargadas")
            elif not os.path.exists(ruta1):
                print("no hay canciones,solo videos")
            elif not os.path.exists(ruta2):
                print("no hay videos,solo canciones")
                for archivo in os.listdir(ruta1):
                    print(archivo)
            else:  
                if not os.listdir(ruta1) and not os.listdir(ruta2): 
                    print("no hay canciones descargadas")
                else:
                    print("")
                    for archivo in os.listdir(ruta1):
                        print("canciones descargadas")
                        print(archivo)
                        print("")
                    for archivo in os.listdir(ruta2):
                        print("videos descargados")
                        print(archivo)
                        print("")




            # FLUJO DE VIDEO



        elif op=="5":
            while True:
                if not os.path.exists(ruta2):
                    print("no hay nada")
                    break
                archivos=os.listdir(ruta2)
                if not archivos:
                    print("esta vacio")
                    break
                for i,archivo in enumerate(archivos,1):
                    print(f"{i}-{archivo}")
                print("00. salir")
                opcion=input("elija que borrar: ").strip()
                if opcion=="00":
                    print("")
                    break
                try:
                    num=int(opcion)
                    if opcion.isdigit():
                        if 1<= num <=len (archivos):
                            archivo_a_borrar=archivos[num - 1]
                            confirmar=input(f"seguro que quieres borrar {archivo_a_borrar}? si/no: ")
                            if confirmar.lower()=="si":
                               os.remove(os.path.join(ruta2,archivo_a_borrar))
                               print(f"{archivo_a_borrar} borrado ✅")
                               print("")
                            elif confirmar.lower()=="no":
                                print("operacion cancelada")
                        else:
                           print("opcion invalida")
                    else: 
                        print("solo digitos")
                        print("")
                except ValueError:
                    print("pon un numero valido")



                #FLUJO DE AUDIO



        elif op=="6":
            while True:
                if not os.path.exists(ruta1):
                    print("no hay archivos para borrar")
                    print("")
                    break
                archivos=os.listdir(ruta1)
                if not archivos:
                    print("esta vacio")
                    print("")
                    break
                for i,archivo in enumerate (archivos,1):
                    print(f"{i}-{archivo}")
                    print("")
                print("00. salir")
                opcion=input("elija que borrar: ").strip()
                print("")
                if opcion=="00":
                    print("")
                    break
                try:
                    num=int(opcion)
                    if opcion.isdigit():
                        if 1<= num <=len(archivos):
                            borrar=archivos[num -1]
                            confirmar=input(f"seguro que quiere borrar {borrar}? si/no: ")
                            print("")
                            if confirmar.lower()=="si":
                                os.remove(os.path.join(ruta1,borrar))
                                print(f"{borrar} borrado")
                                print("")
                            elif confirmar.lower()=="no":
                                print("operacion cancelada")
                        else:
                            print("invalido")
                    else:
                        print("solo digitos")
                except ValueError:
                    print("pon un numero valido")



        elif op=="7":
            print("saliendo")
            break
        else:
            print("opcion invalida")

if __name__=="__main__":
    down()

