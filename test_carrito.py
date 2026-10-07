from selenium import webdriver
from selenium.webdriver.common.by import By


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
        boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        boton_agregar.click()

        # Verificar que el carrito tenga un producto
        cantidad_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cantidad_carrito.text == "1"
        
        #navegar al carrito
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        carrito.click()
        
        #verificar que se haya navegado al carrito        
        assert "/cart.html" in driver.current_url
        
        # Verificar que el producto agregado esté en el carrito
        producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        assert producto_carrito.text == "Sauce Labs Backpack"
        
    finally:
        driver.quit()    