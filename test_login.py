import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_exitoso():
    # Configuración del navegador
    driver = webdriver.Chrome()
    
    try:
        # Abrir la página de inicio de sesión
        driver.get("https://www.saucedemo.com/")

        # Ingresar credenciales válidas
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Verificar que se haya iniciado sesión correctamente
        assert "/inventory.html" in driver.current_url
        
        #validacion texto logo
        
        logo = driver.find_element(By.CLASS_NAME, "app_logo")        
        assert logo.text == "Swag Labs"
        
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"
        
    
    finally:
        driver.quit()
        
    
    