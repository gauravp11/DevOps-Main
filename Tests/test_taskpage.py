import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from locators import LoginPageLocators, TaskPageLocators, CommonLocators, HomePageLocators
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

def test_e2e_taskpage(selenium):

    selenium.find_element(By.XPATH,HomePageLocators.CreateTask).click()
    time.sleep(2)
    selenium.find_element(By.XPATH,TaskPageLocators.addTaskButtonClick).click()
    
    selenium.find_element(By.XPATH,TaskPageLocators.addTitle).send_keys("Test Task")
    selenium.find_element(By.XPATH,TaskPageLocators.assignedtoClick).click()
    time.sleep(5)
    selenium.find_element(By.XPATH,TaskPageLocators.selectUserAssign).click()
    selenium.find_element(By.XPATH,TaskPageLocators.partnerToclick).click()
    time.sleep(5)
    selenium.find_element(By.XPATH,TaskPageLocators.selectOptionPart).click()
    selenium.find_element(By.XPATH,TaskPageLocators.deadlineInput).send_keys("2024-07-01")
    selenium.find_element(By.XPATH,TaskPageLocators.selectPriority).click()
    time.sleep(5)
    selenium.find_element(By.XPATH,TaskPageLocators.inputPrioriy).click()
    selenium.find_element(By.XPATH,TaskPageLocators.inputDecs).send_keys("demo text")

    
    selenium.find_element(By.XPATH,CommonLocators.clickSave).click()
    homepage_header = selenium.find_element(By.XPATH,CommonLocators.CheckUserName)
    assert "ADMINDOCKER" in homepage_header.text

    assert "Test Task" in selenium.find_element(By.XPATH,TaskPageLocators.checkTitle).text

    # assert "Internal Tickets" in selenium.find_element(By.XPATH,HomePageLocators.CreateTicket).text
    
