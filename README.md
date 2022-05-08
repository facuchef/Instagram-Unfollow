# Instagram-Unfollow
Tells you who doesn't follow you back on Instagram.


El programa principal "Instagram Unfollow Git.py" se encarga de crear un archivo de texto con los nomres de usuarios de las personas que seguimos pero no nos siguen.



Pasos para usarlo:
1-Instala la librería Selenium (permite que el programa utilice el browser de manera automatica)
2-Descarga el Chromedriver correspondiente a la versión de Chrome que uses y guardarlo en: C:\Webdrivers/chromedriver.exe (Si la carpeta no existe, creala y guardalo ahí).
    -El chromedriver descarga instala desde https://chromedriver.chromium.org/ 
3-Completa con tu usuario y contraseña de instagram en el archivo "InstaUser.py". (Nadie va a poder lo que está en este archivo)
4-Anda al archivo "Instagram Unfollow Git.py" e inicialo, el programa automaticamente va a iniciar sesión, va a analizar tus seguidores y seguidos, va a comprarlos y finalmente va a crear un archivo .txt con los nombres de los usuarios que seguís pero no te siguen.
5-Y LISTO! Ya tenes una lista que te buchonea todo :)
Extra-Finalmente tenes que cerrar la sesión de manera manual, el programa no cierra sesión solo.