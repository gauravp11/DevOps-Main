import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from locators import LoginPageLocators, ThemePagelocators, CommonLocators, HomePageLocators
@pytest.fixture(scope="module")
def driver():
    # Initialize WebDriver
    global driver
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()

@pytest.fixture(scope="function")
def selenium(driver,login_url):
    # Login
    driver.get(login_url)
    username_input = driver.find_element(By.XPATH,LoginPageLocators.USERNAME_INPUT)
    username_input.send_keys("admindocker")
    password_input = driver.find_element(By.XPATH,LoginPageLocators.PASSWORD_INPUT)
    password_input.send_keys("adminpassword")
    login_button = driver.find_element(By.XPATH,LoginPageLocators.LOGIN_BUTTON)
    login_button.click()
    time.sleep(2)
    homepage_header = driver.find_element(By.XPATH,CommonLocators.CheckUserName)
    assert "ADMINDOCKER" in homepage_header.text
    yield driver

def test_e2e_themepage(selenium):

    selenium.find_element(By.XPATH,HomePageLocators.CreatThemes).click()
    time.sleep(2)
    selenium.find_element(By.XPATH,ThemePagelocators.addThemeButtonClick).click()
    selenium.find_element(By.XPATH,ThemePagelocators.addThemeName).clear()
    selenium.find_element(By.XPATH,ThemePagelocators.addThemeName).send_keys("Test Theme")
    selenium.find_element(By.XPATH,ThemePagelocators.addEnvName).send_keys("Test Env")
    selenium.find_element(By.XPATH,ThemePagelocators.addTitleName).clear()
    selenium.find_element(By.XPATH,ThemePagelocators.addTitleName).send_keys("TaskSync")
    
    selenium.find_element(By.XPATH,CommonLocators.clickSave).click()
    homepage_header = selenium.find_element(By.XPATH,CommonLocators.CheckUserName)
    assert "ADMINDOCKER" in homepage_header.text

    assert "Test Theme" in selenium.find_element(By.XPATH,ThemePagelocators.CheckThemeName).text
    assert "TaskSync" in selenium.find_element(By.XPATH,CommonLocators.CheckBrandingName).text
    
