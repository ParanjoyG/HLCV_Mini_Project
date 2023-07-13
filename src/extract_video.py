import os
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.sign.mt'
text = 'How are you?'
video_path = './videos/pose_extractions/'

# exist = os.path.exists(video_path)
# if not exist :
#     os.makedirs(video_path)

chrome_options = webdriver.ChromeOptions()
prefs = {'savefile.default_directory' : video_path,
         'directory_upgrade ' : True}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

text_box = driver.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-router-outlet/app-main/ion-tabs/div/ion-router-outlet/app-translate/app-translate-desktop/ion-content/div/app-drop-pose-file/div/div/div/app-spoken-to-signed/app-spoken-language-input/div/textarea')
text_box.clear()
text_box.send_keys(text)

time.sleep(8)
shadow_host = driver.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-router-outlet/app-main/ion-tabs/div/ion-router-outlet/app-translate/app-translate-desktop/ion-content/div/app-drop-pose-file/div/div/div/app-spoken-to-signed/app-signed-language-output/div/ion-button[1]')
script = 'return arguments[0].shadowRoot'
shadow_root = driver.execute_script(script, shadow_host)
download_button = shadow_root.find_element(By.CLASS_NAME, 'button-native')
download_button.click()
time.sleep(5)
# video_url = buttons.get_attribute('src')

# urllib.request.urlretrieve(video_url, f'{text}.mp4')

# download_button = driver.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-router-outlet/app-main/ion-tabs/div/ion-router-outlet/app-translate/app-translate-desktop/ion-content/div/app-drop-pose-file/div/div/div/app-spoken-to-signed/app-signed-language-output/div/ion-button[1]//button')
# download_button.click()

driver.quit()