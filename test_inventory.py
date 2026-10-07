from selenium import webdriver
from selenium.webdriver.common.by import By


def test_inventory_page():
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

        # Verificar que titulo sea correcto
        titulo = driver.title
        assert titulo == "Swag Labs"
        
        # verificar que haya productos
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")        
        assert len(productos) > 0
        
        # lista nombre y precio del primer producto
        primer_producto = productos[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

        print(f"Nombre: {nombre_producto}, Precio: {precio_producto}")
        
        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == "$29.99"
        
        #verificar la existencia del menu hamburguesa
        menu_hamburguesa = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu_hamburguesa.is_displayed()
        
        #verificar la existencia del filtro de ordenamiento
        filtro_ordenamiento = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro_ordenamiento.is_displayed()

    finally:
        driver.quit()