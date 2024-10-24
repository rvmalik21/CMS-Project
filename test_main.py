import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestCCTBRepublish:
    def test_RepublishCCTB(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://cctbweb-qa.azurewebsites.net/umbraco")
        driver.find_element(By.NAME,"username").send_keys("ravi.malik@gus.global")
        driver.find_element(By.NAME, "password").send_keys("Ravi@12345")
        driver.find_element(By.XPATH,"//button[@class='btn umb-button__button btn-success umb-button--m']").click()
        time.sleep(4)
        driver.get("https://cctbweb-qa.azurewebsites.net/umbraco/dialogs/republish.aspx?xml=true")
        wait=WebDriverWait(driver, 3)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//input[@id='body_bt_go']")))
        driver.find_element(By.XPATH,"//input[@id='body_bt_go']").click()
        time.sleep(5)
        publish_content_upto_date=driver.find_element(By.XPATH,"//input[@value='Ok']").get_attribute("value")
        assert publish_content_upto_date =="Ok"
        print("The website cache has been refreshed. All publish content is now up to date. While all unpublished content is still unpublished")
        driver.quit()