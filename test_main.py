from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_footer_elements():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://only.digital/")
    driver.maximize_window()

    try:
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))

        footer = driver.find_element(By.TAG_NAME, "footer")
        assert footer.is_displayed(), "Футер не отображается на странице"

        footer_elements_to_check = {
            (By.CLASS_NAME, "Footer_logo__2QEhf"): "Логотип",
            (By.TAG_NAME, "button"): "Кнопки"
        }

        for locator, description in footer_elements_to_check.items():
            element = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(locator)
            )
            assert element.is_displayed(), f"{description} не найдены в футере"

    finally:
        driver.quit()
