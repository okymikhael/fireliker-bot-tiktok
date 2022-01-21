from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

id_tiktok = "okymikhael24"
total = 0
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('./driver/chromedriver', options=options)
driver.get('https://fireliker.com/index.php')
WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/fieldset/div[1]/div/input')).send_keys(id_tiktok)
WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/fieldset/div[2]/button')).click()
driver.execute_script("window.history.go(-1)")

time.sleep(2)
captcha = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div/img")
with open(r"captcha.png", 'wb') as f:
    f.write(captcha.screenshot_as_png)

captcha_result = input("Captcha Result: ")
WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/form/div/input')).send_keys(captcha_result)
WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/form/input')).click()
print('---logged in---')

while True:
    print('---Auto Views---')
    driver.get('https://fireliker.com/autoviews.php')
    input = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[1]/div/div[2]/div/form/div/select/option")
    driver.execute_script("arguments[0].value='3';",input)
    WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div/div[2]/div/form/button')).click()
    total += 300
    print(f'---Total: {total} ---', '\n')
    print('---Viewers Added---', '\n')
    time.sleep(320)