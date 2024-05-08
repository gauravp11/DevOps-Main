import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from locators import LoginPageLocators, TicketPageLocators, CommonLocators, HomePageLocators
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

    selenium.find_element(By.XPATH,HomePageLocators.CreateTicket).click()
    time.sleep(2)
    selenium.find_element(By.XPATH,TicketPageLocators.addTicketButtonClick).click()
    selenium.find_element(By.XPATH,TicketPageLocators.addTitle).send_keys("Test Ticket")
    selenium.find_element(By.XPATH,TicketPageLocators.selectPriority).click()
    selenium.find_element(By.XPATH,TicketPageLocators.inputPrioriy).click()
    selenium.find_element(By.XPATH,TicketPageLocators.clickassignedTo).click()
    selenium.find_element(By.XPATH,TicketPageLocators.inputTO).click()
    
    selenium.find_element(By.XPATH,CommonLocators.clickSave).click()
    homepage_header = selenium.find_element(By.XPATH,CommonLocators.CheckUserName)
    assert "ADMINDOCKER" in homepage_header.text

    assert "Test Ticket" in selenium.find_element(By.XPATH,TicketPageLocators.checkTicket).text
    
