import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from locators import LoginPageLocators, UserPageLocators, CommonLocators, HomePageLocators
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

    selenium.find_element(By.XPATH,HomePageLocators.CreateUser).click()
    time.sleep(2)
    # Add User
    selenium.find_element(By.XPATH,UserPageLocators.addUserClick).click()
    selenium.find_element(By.XPATH,UserPageLocators.inputUserName).send_keys("TestUser")
    selenium.find_element(By.XPATH,UserPageLocators.inputPassword).send_keys("TaskSync@123")
    selenium.find_element(By.XPATH,UserPageLocators.confirmPassword).send_keys("TaskSync@123") 
    selenium.find_element(By.XPATH,CommonLocators.clickSave).click()
    homepage_header = selenium.find_element(By.XPATH,CommonLocators.CheckUserName)
    assert "ADMINDOCKER" in homepage_header.text

    # Add details

    selenium.find_element(By.XPATH,UserPageLocators.inputFirstName).send_keys("Test")
    selenium.find_element(By.XPATH,UserPageLocators.inputLastName).send_keys("User")
    selenium.find_element(By.XPATH,UserPageLocators.isStaffTrue).click()
    selenium.find_element(By.XPATH,UserPageLocators.addInternalTicket).click()
    selenium.find_element(By.XPATH,CommonLocators.clickSave).click()
    
    assert "TestUser" in selenium.find_element(By.XPATH,UserPageLocators.checkUser).text

    

    
    
    
    
    
    
