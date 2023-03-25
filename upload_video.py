import time
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui

def close_handles(self, driver):
    global main_handle

    handles = driver.window_handles
    size = len(handles)

    main_handle = driver.current_window_handle
    for x in range(size):
    	if handles[x] != main_handle:
    		driver.switch_to.window(handles[x])
    		driver.close()

    driver.switch_to.window(main_handle)

    driver.switch_to.frame(0)

options = uc.ChromeOptions()

options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = uc.Chrome(options=options)
driver.get('https://www.youtube.com/')
element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(('xpath', '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]'))
        )
driver.find_element("xpath", '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]').click()
driver.find_element("xpath", '//*[@id="identifierId"]').send_keys('ourPsy25@gmail.com')
driver.find_element("xpath", '//*[@id="identifierNext"]/div/button/span').click()
element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(('xpath', '//*[@id="password"]/div[1]/div/div[1]/input'))
        )
time.sleep(1)
driver.find_element("xpath", '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('*Rhrl3131')
driver.find_element("xpath", '//*[@id="passwordNext"]/div/button/span').click()
element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(('xpath', '//*[@id="button"]/a'))
        )
driver.find_element("xpath", '//*[@id="button"]/a').click()

element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(('xpath', '//*[@id="items"]/ytd-compact-link-renderer[1]'))
        )
time.sleep(1)
driver.find_element("xpath", '//*[@id="items"]/ytd-compact-link-renderer[1]').click()

element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(('xpath', '//*[@id="select-files-button"]/div'))
        )
time.sleep(1)
driver.find_element("xpath", '//*[@id="select-files-button"]/div').click()

element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(('xpath', '//*[@id="content"]/input'))
        )
time.sleep(1)
driver.find_element("xpath", '//*[@id="content"]/input').send_keys('/Users/realizer/Documents/youtubeDown/test.mp4')
element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(('xpath', '//*[@id="dialog"]/div/ytcp-animatable[2]/div/div[2]'))
        )
time.sleep(1)
pyautogui.click(835, 611)
time.sleep(1323)