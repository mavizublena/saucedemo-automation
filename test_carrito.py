from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_carrito():
    # Configuración del navegador
    driver = webdriver.Chrome()
    
    try:
        #  login
        driver.get("https://www.saucedemo.com/")

        # Ingresar credenciales válidas
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()
        
                
        # Agregar un producto al carrito
        boton_agregar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        boton_agregar.click()
        
        # Verificar que el carrito tenga un producto
        cantidad_carrito = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert cantidad_carrito.text == "1"
        
        # navegar al carrito
        carrito = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        carrito.click()

        # esperar hasta que navegue al carrito
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

        # verificar que se haya navegado al carrito
        assert "/cart.html" in driver.current_url
        
    finally:
        driver.quit()    