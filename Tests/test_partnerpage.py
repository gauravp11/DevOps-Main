import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from locators import LoginPageLocators, PartnerPageLocators, CommonLocators, HomePageLocators
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

def test_e2e_partnerpage(selenium):

    selenium.find_element(By.XPATH,HomePageLocators.CreatePatner).click()
    time.sleep(5)
    selenium.find_element(By.XPATH,PartnerPageLocators.addButtonClick).click()
    
    selenium.find_element(By.XPATH,PartnerPageLocators.addName).send_keys("TestPartner")
    selenium.find_element(By.XPATH,PartnerPageLocators.addEmail).send_keys("testemail@demo.com")
    selenium.find_element(By.XPATH,PartnerPageLocators.clickIsCompany).click()
    selenium.find_element(By.XPATH,PartnerPageLocators.selectIsCompany).click()
    selenium.find_element(By.XPATH,PartnerPageLocators.addPhone).send_keys("1234567890")
    selenium.find_element(By.XPATH,PartnerPageLocators.addNotes).send_keys("This is a test Partner and this is created via selenium")
    
    selenium.find_element(By.XPATH,CommonLocators.clickSave).click()
    homepage_header = selenium.find_element(By.XPATH,CommonLocators.CheckUserName)
    assert "ADMINDOCKER" in homepage_header.text

    assert "TestPartner" in selenium.find_element(By.XPATH,PartnerPageLocators.CheckForName).text

    # assert "Internal Tickets" in selenium.find_element(By.XPATH,HomePageLocators.CreateTicket).text
    
