import os
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import shutil


def whats_login():
  # get the whatsapp web qr code
  options = webdriver.EdgeOptions()
  options.add_experimental_option("detach", True)  # Keep the window open after script execution
  driver = webdriver.Edge(options=options)
  driver.implicitly_wait(10)
  driver.get('https://web.whatsapp.com/')
  # wait for the canvas element to exist
  canvas_element = driver.find_element('css selector', 'canvas')
  
  driver.save_screenshot('screenshot.png')
  shutil.move('screenshot.png', 'temp/screenshot.png')
  #move the file to the temp folder

def main():
  # get the current hr and min
  now = datetime.datetime.now()
  hr = now.hour
  mi = now.minute + 1
  pywk.sendwhatmsg("+573012167977","hi",hr,mi)