import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la API key desde la variable de entorno
API_KEY = os.getenv("API_KEY")

# Define el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Enviar el mensaje "Hola Mundo" y un número aleatorio
    random_number = random.randint(1, 100)  # Número aleatorio entre 1 y 100
    await update.message.reply_text(f"Hola Mundo! Aquí tienes un número aleatorio: {random_number}")

def main():
    # Usamos la API key cargada desde el archivo .env
    application = Application.builder().token(API_KEY).build()

    # Registra el comando /start
    application.add_handler(CommandHandler("start", start))

    # Comienza a escuchar los mensajes
    application.run_polling()

if __name__ == '__main__':
    main()
