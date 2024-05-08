import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from locators import LoginPageLocators, CommonLocators, HomePageLocators
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

def test_check_all_modules_available(selenium):

    assert "Partners" in selenium.find_element(By.XPATH,HomePageLocators.CreatePatner).text
    assert "Tasks" in selenium.find_element(By.XPATH,HomePageLocators.CreateTask).text
    assert "Themes" in selenium.find_element(By.XPATH,HomePageLocators.CreatThemes).text
    assert "Groups" in selenium.find_element(By.XPATH,HomePageLocators.CreateGroup).text
    assert "Users" in selenium.find_element(By.XPATH,HomePageLocators.CreateUser).text
    assert "Internal Tickets" in selenium.find_element(By.XPATH,HomePageLocators.CreateTicket).text
    
