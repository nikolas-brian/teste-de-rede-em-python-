from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print('super alteração')

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors') 

service = Service(ChromeDriverManager().install())
driver = uc.Chrome(service=service, options=chrome_options)

driver.get("https://www.speedtest.net/pt")

try:
    botao_login = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    botao_login.click()
    print('Ele aceitou os cookies')
    time.sleep(3)

    print('Agora ele vai iniciar')
    botao_iniciar = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'))
    )
    botao_iniciar.click()
    print("Iniciou")

    
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[2]/div/div/ul[1]/li[2]/a'))
    )
    time.sleep(5)

   
    download = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
    upload = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    
    textd = download.text
    textu = upload.text   

    print(f'Seu download é: {textd}')
    print(f'Seu upload é: {textu}')
    time.sleep(100000)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
   
    driver.quit()