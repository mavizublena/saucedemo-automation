# Automatización de pruebas - SauceDemo

## Propósito del proyecto

Este proyecto tiene como objetivo realizar pruebas automatizadas sobre el sitio web SauceDemo utilizando Selenium y Pytest.

Las pruebas realizadas verifican:

- Inicio de sesión exitoso.
- Nombre y precio del primer producto del inventario.
- Agregado de un producto al carrito y validación del producto agregado.

## Tecnologías utilizadas

Para ejecutar el proyecto es necesario tener Python instalado.


## Instalación de dependencias

Las dependencias utilizadas son:

- Selenium
- Pytest
- pytest-html

Para instalar todas las dependencias desde el archivo `requirements.txt`, ejecutar:

```bash
python -m pip install -r requirements.txt

```

También pueden instalarse independientemente: 

```bash

python -m pip install selenium
python -m pip install pytest
python -m pip install pytest-html

```