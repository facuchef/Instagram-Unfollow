# Instagram-Unfollow
Tells you who doesn't follow you back on Instagram.
- El programa te muestra los usuarios de Instagram que seguís pero no te siguen.

## Instrucciones de uso:

1. Instala la librería Selenium. Esta librería le permite al programa utilizar el browser de manera automatica.
    - Para instalarla debes escribir: ```pip install Selenium```
2. Descarga el Chromedriver correspondiente a la versión de Chrome que uses y guardarlo en: C:\Webdrivers/chromedriver.exe (si la carpeta no existe, creala).
    - Descarga el chromedriver desde: https://chromedriver.chromium.org/ 
3. Completa con tu usuario y contraseña de Istagram en el archivo "InstaUser.py". (Una vez descargado, nadie va a poder ver lo que haces en los archivos, así que tu contraseña está segura :wink: 
4. Finalmente hace correr el archivo "Instagram Unfollow Git.py". El programa automaticamente va a iniciar sesión a tu cuenta de instagrar y va a comparar tus seguidores con tus seguidos para luego crear un archivo .txt con los nombres de los usuarios que seguís pero no te siguen. El archivo .txt se guarda en la misma carpeta.
    - Dato: Dependiendo la cantidad de seguidores y seguidos que tengas el programa puede tardar un ratito.
5. ¡Y... LISTO! :grinning: En el archivo vas a poder ver todos las personas que seguís pero no te siguen.

Finalmente debés cerrar la sesión de Instagram de manera manual. El programa finaliza cuando crea el archivo.
