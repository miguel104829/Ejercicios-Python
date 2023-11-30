from tkinter import *
import os
from PIL import ImageTk, ImageColor, Image
import getpass

#carga de directorios
#carpeta principal
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")

#creación de usuario nuevo
usuario_nuevo = ()
while True:
    #se pide usuario y contraseña en la consola
    nuevo_usuario = input("Ingrese un usuario: ")
    nueva_contraseña = getpass.getpass("Ingrese una contraseña: ")

    #Se solicita de nuevo el ususario y contraseña
    repite_usuario = input("Ingrese de nuevo el usuario: ")
    repite_contraseña = getpass.getpass("Ingrese de nuevo la contraseña: ")

    #se valida que el usuario y contraseña sean iguales
    if nuevo_usuario != repite_usuario or nueva_contraseña != repite_contraseña:
        print("Usuario o contraseña incorrectos. Intente de nuevo")
    else:
        usuario_nuevo = (nuevo_usuario, nueva_contraseña)
        print("Usuario creado correctamente")
        break
    
root = Tk()

root.title("Ejercicio 5")

#icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes, "1.ico"))

#carga de imagen
imagen = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "2.jpg")).resize((350, 300)))
etiqueta = Label(image=imagen)
etiqueta.pack()

#campos de texto
Label(text="Usuario: ").pack()
usuario = Entry()
usuario.insert(0, "Ej: Miguel")
usuario.bind("<Button-1>", lambda e: usuario.delete(0, END))
usuario.pack()

Label(text="Contraseña: ").pack()
contraseña = Entry()
contraseña.insert(0, "*"*7)
contraseña.bind("<Button-1>", lambda e: contraseña.delete(0, END))
contraseña.pack()

#funcion validar el login 
def validar_login():
    obtener_usuario = usuario.get()
    obtener_contraseña = contraseña.get()
    if obtener_usuario != usuario_nuevo[0] or obtener_contraseña != usuario_nuevo[1]:
        Label(text="Usuario o contraseña incorrectos", fg="red").pack()
    else:
        Label(text=f"Hola, {usuario_nuevo[0]}. Espere unos segundos", fg="green").pack()

Button(text="Iniciar sesión", command=validar_login).pack()


root.mainloop()