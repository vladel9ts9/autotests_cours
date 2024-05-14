from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

options = ChromeOptions()
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)


try:
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)

    x_element_text = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = str(math.log(abs(12*math.sin(int(x_element_text)))))

    input_result = browser.find_element(By.ID, "answer")
    input_result.send_keys(result)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button_input = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button_input.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()