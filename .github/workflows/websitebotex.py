from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# open seedloaf login page
driver.get("https://seedloaf.io/login")
time.sleep(1)

# click login button on homepage (if present)
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))).click()
except:
    pass # sometimes the login form loads directly

# enter credentials
wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(USERNAME)
wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(PASSWORD)

# click login
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))).click()

# click start button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Start')]"))).click()

# give seedloaf time to start the server
time.sleep(10)

driver.quit()
