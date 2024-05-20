import pytest
from selenium.webdriver.common.by import By
import time
import math

@pytest.mark.parametrize('link', ["236895", "236896"])
def test_auth_on_site(browser, link):
    browser.get(f"https://stepik.org/lesson/{link}/step/1")
    browser.implicitly_wait(10)
    browser.find_element(By.CSS_SELECTOR, "#ember459").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("vlad.vusat@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("Vvv09091999")
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader").click()


    if is_element_present

    answer = math.log(int(time.time()))

    browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

    time.sleep(5)

    result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text

    assert result == "Correct!", "ТЕКСТ НЕ СОВПАДАЕТ"

