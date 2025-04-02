# Instagram Unfollow Bot

Este bot automatiza el proceso de dejar de seguir usuarios en Instagram utilizando Selenium.

## Requisitos

### MacOS
1. Instalar Homebrew si no está instalado:
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Instalar Google Chrome y ChromeDriver:
   ```sh
   brew install --cask google-chrome
   brew install chromedriver
   ```
3. Crear y activar un entorno virtual:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Instalar dependencias dentro del entorno virtual:
   ```sh
   pip install -r requirements.txt
   ```

### Windows
1. Instalar Google Chrome.
2. Descargar ChromeDriver desde [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) y agregarlo al `PATH`.
3. Instalar las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta el script:
   ```sh
   python unfollowig.py
   ```
2. Inicia sesión manualmente en Instagram.
3. Elige la opción `1` para eliminar seguidores.

## Notas
- MacOS requiere un entorno virtual para evitar conflictos con bibliotecas del sistema.
- Instagram podría bloquear temporalmente tu cuenta si detecta demasiadas acciones automáticas.
- Asegúrate de tener instalada la versión correcta de ChromeDriver compatible con tu navegador.
- No uses el bot para dejar de seguir más de 1.000 usuarios a la vez. Si necesitas dejar de seguir a más de 1.000, espera entre 2 y 3 días antes de continuar.

## Contacto
Si tienes problemas o sugerencias, crea un issue en el repositorio.

