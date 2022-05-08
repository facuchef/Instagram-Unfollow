#En este caso el programa crea un archivo de texto con los nomres de usuarios de las personas que seguimos pero no nos siguen.
#El programa inicia sesión solo pero el usuario debe desloguearse de manera manual.
#Antes de usarlo verifica que el chromedriver descargado sea el correcto para la versión de Chrome actual!
    #Si no es, descarga el nuevo chromedriver, borra el existente y reemplazalo por el nuevo (toda la data abajo).

from InstaUser import MYusername,MYpassword
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
import time


def loginInstagram(driver, username, password):
    #Ingresamos el usuario y la contraseña:
    u = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))) #seleccionamos el recuadro de username
    p = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))) #seleccionamos el recuadro de password
    '''
    Dato importnte: como la carga de las páginas web es dínamica (o sea tarda en cargar), antes de seleccionar un elemento, debemos escribir:
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(("elemento que seleccionamos"))), ya que de esta manera hacemos que selenium 
            espere a que ele elemento sea clicleable según las expected conditions (ec).
    '''
    u.clear()    #Eliminamos lo que haya escrito
    p.clear()    #idem
    u.send_keys(username)  #Escribimos lo que guarde la variable MYusarname
    p.send_keys(password)  #idem
    #Apretamos el botón de "Log In":
    time.sleep(2) #espera 2 segundos
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()   #Sellecionamos y clicleaos el elemento "Log In"
    #Una vez que entramos aparecen 2 pop ups, por lo que debemos apretar "not now" en cada uno de los carteles que nos salen al ingresar:
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()
    time.sleep(2)   #Esperamos porque instagram es vivo el segundo lo pone trabado al principio.
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()


def goToProfileFromHome(driver):
    #Hacemos click en la fotito que desplega las opciones del profile:
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,"//span[contains(@class,'_2dbep qNELH')]"))).click()
    #Hacemos click en la opción del perfil de la lista desplegable:
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, '-qQT3'))).click()
    #Otra opción: self.browser.find_element_by_xpath(f"//a[contains(@href, '/{MYusername}/')]").click()


def scrollingBox(driver, span):
    if span == "followers": #Hacemos este if porque los span (posts, followers, following) están numerados de 1 a 3 y cambia su xpath.
        numero = 2
    elif span == "following":
        numero = 3
    scrollBox = driver.find_element(By.XPATH,f"/html/body/div[6]/div/div/div/div[{numero}]")    #Seleccionamos la barrita que permite scrolear.
        #OJO que acá en vez de driver.find_elements es element (singular).
    largoActual = 1
    largoAnterior = 0
    #Scroleamos hasta que el largoAnterior de la scrollBox sea igual al largo actual (o sea que no baje más):
    while largoAnterior != largoActual:
        largoAnterior = largoActual
        time.sleep(randint(2,5))
        largoActual = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        return arguments[0].scrollHeight;""", scrollBox)
            #Explicación:   (ojo que esto es código JavaScript)
                #arguments[0].scrollTo(0, arguments[0].scrollHeight) --> Bajamos hasta el fondo de la scrollBox (hasta donde cargue)
                #return arguments[0].scrollHeight --> Nos devuelve el largo de la scrollBox
            #Extra: Si quisieramos hacer scroll de la pantalla principal deberíamos escribir:
                    #largoActual = driver.execute_script("window.scrollTo(0,4000);")
                        #en este caso, como el tope es 4000, se mueve 4 pantallas hacia abajo
    time.sleep(randint(2,5))
    userNames = getNames(scrollBox)
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[1]/div/div[3]/div').click()  #Clickeamos el botón de la X.
        #Antes el XPATH era: "/html/body/div[6]/div/div/div/div[1]/div/div[2]/button"
    return userNames

    
def getNames(scroll_Box):
    links =  scroll_Box.find_elements(By.TAG_NAME,'a') #Cada nombre de usuario está dado por un link en formato a href.
    nombres = []
    for name in links:  #Sacamos el texto de los links siempre y cuando no sea un string vacío "".
        if name.text != '':
            nombres.append(name.text)
    #Forma corta de hacer el for: nombres = [name.text for name in links if name.text != '']
    #print(nombres)
    print("Cantidad de usuarios obtenidos:",len(nombres))
    return nombres


def notFollowingBack(following,followers):
    dejarDeSeguir = []
    for user in following:
        if user not in followers:
            dejarDeSeguir.append(user)
    return dejarDeSeguir


#Programa principal:

#Iniciamos el driver de Chrome.
chromeDriver = webdriver.Chrome(executable_path='C:\Webdrivers/chromedriver.exe') 
    #Datos:
        #-El Web driver está en C:\Webdrivers.  (https://chromedriver.chromium.org/)
        #-Lo tuve que agregar al PATH en: this PC --> Properties --> Advanced system settings --> Enviroment variables --> System variables --> Path --> edit
        #Ojo ahora lo cambiaste. El path lo va a buscar directo a la dirección C:\Webdrivers/chromedriver.exe
            #ya no está más en path.
#chromeDriver.set_window_size(1000, 1000)   #Ajusta el tamaño de la ventana emergente
chromeDriver.get("https://www.instagram.com/") #Entramos a la página de instagram.


#Nos logueamos en instagram:
time.sleep(2)
loginInstagram(chromeDriver, MYusername, MYpassword)


#Vamos al profile:
time.sleep(2)
goToProfileFromHome(chromeDriver)


#Analizamos en followers:
time.sleep(randint(2,5))
print("\nAnalizando seguidores ...")
chromeDriver.find_element(By.XPATH,"//a[contains(@href, '/followers')]").click()    #Clickeamos en folloers
    #Otras opciones que también funcionan:
        #1) chromeDriver.find_element_by_xpath(f"//a[contains(@href, '/{MYusername}/followers/')]").click()
        #2) chromeDriver.find_element_by_partial_link_text("follower").click()
time.sleep(randint(2,5))
followersNames = scrollingBox(chromeDriver, "followers")


#Analizamos en following:
time.sleep(randint(2,5))
print("\nAnalizando seguidos ...")
chromeDriver.find_element(By.XPATH,"//a[contains(@href, '/following')]").click()    #Clickeamos en following
time.sleep(randint(2,5))
followingNames = scrollingBox(chromeDriver, "following")


#Comparamos los followers con los following para ver quien me sigue de los que sigo:
Unfollow = notFollowingBack(followingNames,followersNames)  #Crea una lista con los que sigo y no me siguen.

print(f"\nHay {len(Unfollow)} personas que seguís y no te siguen.")


#Alamacenamos los usuarios que seguís y no te siguen en un archivo de texto nuevo:
file_name = f"Dejar de seguir con {MYusername} en Insta {time.strftime('%d-%m-%Y')}.txt" #Crea un nombre con la fecha del día de hoy.
file = open(str(file_name), "x")   #Crea un nuevo archivo de texto y lo abre para su escritura.
file.write("Dejar de seguir a los siguientes usuarios:\n")
for n in Unfollow:  #Con este for escribimos los nombres de los usuarios uno atrás de otro en el arhcivo.
     file.write(str(n) + ", ")
file.close()

print(f"\nLos usuarios que no te siguen se almacenaron en el siguiente archivo: {file_name}")
print("\nSuerte!")