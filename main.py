from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image

from tools import ddddOCR,HandleVerify

img_path = 'img_data/'
OCR_path = 'Edit/1.png'


# 開啟chrome driver並進入目標網站
driver = webdriver.Chrome('D:/work/grabot/chromedriver-win64/chromedriver.exe')
driver.get('https://www.mvdis.gov.tw/m3-emv-plate/webpickno/queryPickNo#gsc.tab=0')

# 操作輸入time out (sec)
input_timeout = 0.25

# 操作
# 接受條款
button_1 = driver.find_element(by=By.XPATH, value='//*[@id="btnConfirmYes"]')
time.sleep(input_timeout)
ActionChains(driver).move_to_element(button_1).click(button_1).perform()
time.sleep(input_timeout)

# 填寫表單
expSelect = Select(driver.find_element_by_name(name="selDeptCode"))
time.sleep(input_timeout)
expSelect.select_by_visible_text("新竹區")
time.sleep(input_timeout)

expSelect = Select(driver.find_element_by_name(name="selStationCode"))
time.sleep(input_timeout)
expSelect.select_by_visible_text("新竹區監理所")
time.sleep(input_timeout)

expSelect = Select(driver.find_element_by_name(name="selWindowNo"))
time.sleep(input_timeout)
expSelect.select_by_visible_text("新竹縣新埔鎮文德路三段58號")
time.sleep(input_timeout)

expSelect = Select(driver.find_element_by_name(name="selCarType"))
time.sleep(input_timeout)
expSelect.select_by_visible_text("汽車")
time.sleep(input_timeout)

expSelect = Select(driver.find_element_by_name(name="selEnergyType"))
time.sleep(input_timeout)
expSelect.select_by_visible_text("非電能")
time.sleep(input_timeout)

expSelect = Select(driver.find_element_by_name(name="selPlateType"))
time.sleep(input_timeout)
expSelect.select_by_visible_text("自用小客貨車")
time.sleep(input_timeout)

# 辨識驗證碼
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(input_timeout)
driver.save_screenshot('test.png')
left = 360
right = left+120
top = 473
bottom = top+40
img = Image.open('test.png')
img = img.crop((left, top, right, bottom))
img.save(img_path+'0.png')
HandleVerify(img_path)
pick_res = ddddOCR(OCR_path)
print(pick_res)

# 輸入驗證碼
driver.find_element_by_xpath('//*[@id="validateStr"]').send_keys(pick_res)
time.sleep(input_timeout)

button_1 = driver.find_element(by=By.XPATH, value='//*[@id="command"]/div[2]/div/div/div/div/a[1]')
time.sleep(input_timeout)
ActionChains(driver).move_to_element(button_1).click(button_1).perform()
time.sleep(input_timeout)


time.sleep(5)
print('finish')

