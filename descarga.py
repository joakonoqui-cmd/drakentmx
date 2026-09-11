import yt_dlp

from log import console,get_progress,get_ydl_opts

from rich import print

import os

from rich.console import Console

from guardar import guardar_video, guardar_tiktok, guardar_audio

ruta1="/storage/emulated/0/Download/musica"

ruta2="/storage/emulated/0/videos"

menu=["youtube","tiktok","musica","ver archivos descargados","eliminar videos","eliminar audios","salir"]

console=Console()

# MENU


def down():
    while True:
        print("[bold yellow]bienvenido al menu de descargas[/bold yellow] 👾")
        for posicion,opcion in enumerate(menu,start=1):
            print("")
            print(f"[bold cyan]{posicion}-[/bold cyan][bold blue]{opcion}[/bold blue]")
        op=console.input("[blue] > [/blue]")
        print("")



        if op=="1":
            try:
                guardar_video()
                print("[bold green]descarga completa[/bold green] ✅✅") 
                print("")
            except Exception as e:
                print(f"[bold red]error [/bold red]🥀{e}")
                print("")




        elif op=="2":
            try:
                guardar_tiktok()
                print("[bold green]descarga completa[/bold green] ✅✅")
                print("")
            except Exception as e:
                print(f"[bold red]error[/bold red]{e}")
                print("")





        elif op=="3":
            try:
                guardar_audio()
                print("[bold green]descargado con exito [/bold green]✅✅")
                print("")
            except Exception as e:
                print(f"[bold red]fallo[/bold red] ❌❌{e}")
                print("")
        elif op=="4":
            print("")       
            if not os.path.exists(ruta1) and not os.path.exists(ruta2):
                print("[bold red]no hay archivos descargados[/bold red]")
            elif not os.path.exists(ruta1):
                print("[bold red]no hay canciones,solo videos[/bold red]")
            elif not os.path.exists(ruta2):
                print("[bold red]no hay videos,solo canciones[/bold red]")
                for archivo in os.listdir(ruta1):
                    print(archivo)
            else:  
                if not os.listdir(ruta1) and not os.listdir(ruta2): 
                    print("[bold red]no hay archivos descargados[/bold red]")
                else:
                    print("")
                    for archivo in os.listdir(ruta1):
                        print("[bold green]canciones descargadas[/bold green]")
                        print(archivo)
                        print("")
                    for archivo in os.listdir(ruta2):
                        print("[bold green]videos descargados[/bold green]")
                        print(archivo)
                        print("")




            # FLUJO DE VIDEO



        elif op=="5":
            while True:
                if not os.path.exists(ruta2):
                    print("[bold red]no hay nada[/bold red]")
                    break
                archivos=os.listdir(ruta2)
                if not archivos:
                    print("[bold red]T_T[/bold red]")
                    break
                for i,archivo in enumerate(archivos,1):
                    print(f"{i}-{archivo}")
                print("[bold blue]00. salir[/bold blue]")
                opcion=console.input("[bold blue]elija que borrar: [/bold blue]").strip()
                if opcion=="00":
                    print("")
                    break
                try:
                    num=int(opcion)
                    if opcion.isdigit():
                        if 1<= num <=len (archivos):
                            archivo_a_borrar=archivos[num - 1]
                            confirmar=console.input(f"[bold yellow]seguro que quieres borrar {archivo_a_borrar}? si/no: [/bold yellow]")
                            if confirmar.lower()=="si":
                               os.remove(os.path.join(ruta2,archivo_a_borrar))
                               print(f"[bold green]{archivo_a_borrar} borrado [/bold green]✅")
                               print("")
                            elif confirmar.lower()=="no":
                                print("[bold red]operacion cancelada[/bold red]")
                        else:
                           print("[bold red]opcion invalida[/bold red]")
                    else: 
                        print("[bold red]solo digitos[/bold red]")
                        print("")
                except ValueError:
                    print("[yellow]pon un numero valido[/yellow]")



                #FLUJO DE AUDIO



        elif op=="6":
            while True:
                if not os.path.exists(ruta1):
                    print("[bold red]no hay archivos para borrar[/bold red]")
                    print("")
                    break
                archivos=os.listdir(ruta1)
                if not archivos:
                    print("[bold red]esta vacio[/bold red]")
                    print("")
                    break
                for i,archivo in enumerate (archivos,1):
                    print(f"{i}-{archivo}")
                    print("")
                print("00. salir")
                opcion=console.input("[bold blue]elija que borrar: [/bold blue]").strip()
                print("")
                if opcion=="00":
                    print("")
                    break
                try:
                    num=int(opcion)
                    if opcion.isdigit():
                        if 1<= num <=len(archivos):
                            borrar=archivos[num -1]
                            confirmar=console.input(f"[bold yellow]seguro que quiere borrar {borrar}? si/no: [/bold yellow]")
                            print("")
                            if confirmar.lower()=="si":
                                os.remove(os.path.join(ruta1,borrar))
                                print(f"[bold green]{borrar} borrado [/bold green]")
                                print("")
                            elif confirmar.lower()=="no":
                                print("[bold red]operacion cancelada[/bold red]")
                        else:
                            print("[bold red] invalido[/bold red]")
                    else:
                        print("[bold red]solo digitos[/bold red]")
                except ValueError:
                    print("[bold red]pon un numero valido[/bold red]")



        elif op=="7":
            print("[bold green]saliendo[/bold green]")
            break
        else:
            print("[bold red]opcion invalida[/bold red]")

if __name__=="__main__":
    down()

