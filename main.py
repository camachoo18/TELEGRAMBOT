import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
import subprocess

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la API key desde la variable de entorno
API_KEY = os.getenv("API_KEY")

# Define el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.message.from_user.first_name  # Obtiene el nombre del usuario
    greeting_message = f"¡Hola, {user_name}! Bienvenido a mi bot. 😊\n\n"
    
    # Lista de comandos disponibles
    commands_list = (
        "/start - Saludo e información sobre el bot\n"
        "/goku - Enviar un GIF de Goku\n"
        "/saludo - Saludar con tu nombre\n"
        "/suma <num1> <num2> - Realizar la suma de dos números\n"
        "/resta <num1> <num2> - Realizar la resta de dos números\n"
        "/multiplicar <num1> <num2> - Realizar la multiplicación de dos números\n"
        "/dividir <num1> <num2> - Realizar la división de dos números\n"
        "/aleatorio - Generar un número aleatorio entre 1 y 100"
    )
    
    # Enviar mensaje de saludo junto con los comandos
    await update.message.reply_text(f"{greeting_message}Comandos disponibles:\n{commands_list}")

# Define el comando /goku
async def goku(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # URL de un GIF de Goku (puedes cambiarlo por uno que prefieras)
    goku_gif_url = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjlscHRxMnlmMzAyY200cHdhbjI3bzQ1czM2YWdlN3pkc2Z2eWVhMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zKRlxWqdP4NTok3Ppl/giphy.gif"
    
    # Enviar el GIF de Goku
    await update.message.reply_animation(goku_gif_url)

# Define el comando /saludo
async def saludo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.message.from_user.first_name  # Obtiene el nombre del usuario
    await update.message.reply_text(f"¡Hola, {user_name}! ¿Cómo estás?")

    # Define el comando /saludo_custom
async def saludo_custom(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Verifica si el usuario proporcionó un mensaje adicional
    if context.args:
        custom_message = " ".join(context.args)  # Toma los argumentos como el saludo personalizado
        await update.message.reply_text(f"¡Hola {custom_message}!")
    else:
        # Si no se proporciona un saludo, se envía un mensaje predeterminado
        await update.message.reply_text("¡Hola! ¿Cómo te gustaría saludar?")


# Define el comando /ping
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Ejecutar el comando ping en la terminal
        comando = ["ping", "-c", "4", "google.com"]  # Cambiar el comando según el sistema operativo
        resultado = subprocess.run(comando, capture_output=True, text=True)

        # Verificar si la ejecución fue exitosa
        if resultado.returncode == 0:
            await update.message.reply_text(f"Resultado del ping:\n{resultado.stdout}")
        else:
            await update.message.reply_text(f"Hubo un error al ejecutar el ping:\n{resultado.stderr}")
    except Exception as e:
        await update.message.reply_text(f"Ocurrió un error al ejecutar el comando: {e}")




# Define el comando /suma
async def suma(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        num1 = int(context.args[0])
        num2 = int(context.args[1])
        result = num1 + num2
        await update.message.reply_text(f"La suma de {num1} y {num2} es: {result}")
    except (IndexError, ValueError):
        await update.message.reply_text("Por favor, usa el formato /suma <numero1> <numero2>")

# Define el comando /resta
async def resta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        num1 = int(context.args[0])
        num2 = int(context.args[1])
        result = num1 - num2
        await update.message.reply_text(f"La resta de {num1} y {num2} es: {result}")
    except (IndexError, ValueError):
        await update.message.reply_text("Por favor, usa el formato /resta <numero1> <numero2>")

# Define el comando /multiplicar
async def multiplicar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        num1 = int(context.args[0])
        num2 = int(context.args[1])
        result = num1 * num2
        await update.message.reply_text(f"La multiplicación de {num1} y {num2} es: {result}")
    except (IndexError, ValueError):
        await update.message.reply_text("Por favor, usa el formato /multiplicar <numero1> <numero2>")

# Define el comando /dividir
async def dividir(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        num1 = int(context.args[0])
        num2 = int(context.args[1])
        if num2 == 0:
            await update.message.reply_text("No se puede dividir entre cero.")
        else:
            result = num1 / num2
            await update.message.reply_text(f"La división de {num1} entre {num2} es: {result}")
    except (IndexError, ValueError):
        await update.message.reply_text("Por favor, usa el formato /dividir <numero1> <numero2>")

# Define el comando /aleatorio
async def aleatorio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number = random.randint(1, 100)
    await update.message.reply_text(f"El número aleatorio es: {number}")

def main():
    # Usamos la API key cargada desde el archivo .env
    application = Application.builder().token(API_KEY).build()

    # Registra los comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("goku", goku))
    application.add_handler(CommandHandler("saludo", saludo))
    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("saludo_custom", saludo_custom)) 
    application.add_handler(CommandHandler("suma", suma))
    application.add_handler(CommandHandler("resta", resta))
    application.add_handler(CommandHandler("multiplicar", multiplicar))
    application.add_handler(CommandHandler("dividir", dividir))
    application.add_handler(CommandHandler("aleatorio", aleatorio))

    # Comienza a escuchar los mensajes
    application.run_polling()

if __name__ == '__main__':
    main()
