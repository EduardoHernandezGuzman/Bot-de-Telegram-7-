# Bot-de-Telegram

Este proyecto consiste en un bot básico para Telegram desarrollado en Python utilizando la librería TeleBot.

## Descripción

Este bot de Telegram ofrece una variedad de funcionalidades entretenidas, incluyendo contar chistes, resolver adivinanzas, generar excusas divertidas con imágenes y crear contraseñas aleatorias. El bot responde a diferentes comandos enviados por los usuarios, interactuando de manera amigable y divertida.

## Usar el Bot

Puedes interactuar con el bot directamente en Telegram utilizando el siguiente enlace: [Iniciar Bot](https://t.me/proyectoedobot).

## Configuración

Sigue estos pasos para configurar y ejecutar el bot en tu entorno local:

1. **Clonar el Repositorio**: Utiliza Git para clonar este repositorio en tu máquina local utilizando el siguiente comando:

    ```bash
    git clone https://github.com/tu_usuario/Bot-de-Telegram.git
    ```

2. **Instalar Dependencias**: Navega al directorio del proyecto y utiliza pip para instalar las dependencias necesarias:

    ```bash
    cd Bot-de-Telegram
    pip install -r requirements.txt
    ```

3. **Obtener Token de Bot**: Crea un nuevo bot en Telegram utilizando el BotFather y obtén el token del bot recién creado.

4. **Configurar el Token**:
    - Crea un archivo `.env` en el directorio raíz del proyecto.
    - Abre el archivo `.env` en un editor de texto y agrega la siguiente línea, reemplazando `"TU_TOKEN_AQUÍ"` con el token obtenido en el paso anterior:

    ```plaintext
    TELEGRAM_TOKEN=TU_TOKEN_AQUÍ
    ```

5. **Asegurarse de que `.env` esté en `.gitignore`**:
    - Asegúrate de que el archivo `.env` esté incluido en `.gitignore` para que no se suba al repositorio. El contenido de `.gitignore` debería incluir `.env`:

    ```plaintext
    .env
    ```

6. **Ejecutar el Bot**: Ejecuta el script `main.py` utilizando Python para iniciar el bot:

    ```bash
    python main.py
    ```

## Funcionalidades

El bot actualmente cuenta con las siguientes funcionalidades:

- **Comando `/start`**: Inicia el bot y muestra un mensaje de bienvenida con botones interactivos.
- **Comando `/help`**: Proporciona instrucciones sobre cómo interactuar con el bot.
- **Comando `/about`**: Muestra información sobre el bot, incluyendo detalles sobre su propósito y su creador.
- **Comando `/chiste`**: Envía un chiste aleatorio.
- **Comando `/adivinanza`**: Envía una adivinanza aleatoria.
- **Comando `/excusa`**: Genera una excusa divertida acompañada de una imagen.
- **Comando `/password`**: Genera una contraseña aleatoria.


## Personalización

Si deseas agregar nuevas funcionalidades o personalizar el comportamiento del bot, puedes modificar el archivo `main.py` según tus necesidades. La documentación de TeleBot puede ser útil para comprender cómo extender la funcionalidad del bot.

## Autoría

Este proyecto fue desarrollado por [Eduardo Hernández Guzmán](https://github.com/EduardoHernandezGuzman). Puedes encontrar más proyectos interesantes en mi perfil de GitHub.
