import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import dotenv
import os
dotenv.load_dotenv()
# get the GOOGLE_APP_PASSWORD from the .env file
SENDER = "pyautoemail000@gmail.com"
GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")

def send_email(recipent, subject, message):
  print("Enviando correo electrónico...")
  sender_email = SENDER
  # Crea el objeto del mensaje
  msg = MIMEMultipart()
  msg['From'] = sender_email
  msg['To'] = recipent
  msg['Subject'] = subject

  # Agrega el cuerpo del mensaje
  msg.attach(MIMEText(message, 'plain'))

  # Inicia la conexión con el servidor SMTP
  with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(SENDER, GOOGLE_APP_PASSWORD)
    server.send_message(msg)

  print("Correo electrónico enviado exitosamente!")

