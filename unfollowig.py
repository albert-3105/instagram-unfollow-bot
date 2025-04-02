import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Nombre del script siempre será ALB3105
SCRIPT_NAME = "ALB3105"

# Se inicializan las credenciales vacías ya que el usuario las ingresará manualmente en la página
USERNAME = ""
PASSWORD = ""
USERNAME = input("Por favor, ingrese su nombre de usuario de Instagram: ")

def mostrar_menu():
    os.system("clear" if os.name == "posix" else "cls")  # Limpia la terminal
    print(f"""
    ┌───────────────────────────────────┐
    │{SCRIPT_NAME} - Instagram Bot      │
    ├───────────────────────────────────┤
    │ 1. Eliminar seguidores            │
    │ 2. Salir                          │
    └───────────────────────────────────┘
    """)

def iniciar_sesion(driver): 
    print("[INFO] Abriendo Instagram...")
    driver.get("https://www.instagram.com/")
    time.sleep(5)

    print("[INFO] Inicie sesión manualmente en la página de Instagram.")
    print("[INFO] El bot continuará después de que haya ingresado sus credenciales.")
    input("[INFO] Presione Enter cuando haya iniciado sesión.")
    print("[INFO] Sesión iniciada correctamente.")

def abrir_lista_seguidos(driver):
    print("[INFO] Accediendo a la lista de seguidos...")
    driver.get(f"https://www.instagram.com/{USERNAME}/")
    time.sleep(5)

    contenedor_xpath = "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span"
    try:
        contenedor = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, contenedor_xpath))
        )
        contenedor.click()
        print("[INFO] Contenedor padre clickeado para abrir la lista de seguidos.")
        time.sleep(5)
    except Exception as e:
        print(f"[ERROR] No se encontró o no se pudo hacer click en el contenedor padre: {e}")

def buscar_botones(driver):
    xpath_botones = "//div[@role='dialog']//button[.//div[normalize-space()='Following']]"
    try:
        return WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath_botones))
        )
    except:
        return []

def eliminar_seguidores():
    # Se inicia ChromeDriver solo si el usuario elige esta opción
    service = Service("/opt/homebrew/bin/chromedriver")  # Verifica la ruta correcta
    driver = webdriver.Chrome(service=service)

    iniciar_sesion(driver)
    abrir_lista_seguidos(driver)  # Se asegura de abrir la lista de seguidos después de iniciar sesión
    
    while True:
        follow_buttons = buscar_botones(driver)
        if not follow_buttons:
            print("[INFO] No quedan usuarios por dejar de seguir. Recargando página...")
            abrir_lista_seguidos(driver)
            continue
        
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(2)
                unfollow_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Unfollow')]"))
                )
                unfollow_button.click()
                print("[ÉXITO] Se dejó de seguir a un usuario.")
                time.sleep(3)
            except Exception as e:
                print(f"[ERROR] No se pudo dejar de seguir a un usuario: {e}")
                continue
        break

    driver.quit()  # Cierra el navegador al finalizar

# Menú interactivo
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        eliminar_seguidores()
    elif opcion == "2":
        print("[INFO] Cerrando programa...")
        break
    else:
        print("[ERROR] Opción no válida. Intente de nuevo.")
        time.sleep(2)
