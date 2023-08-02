import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def startChat():
    driver = webdriver.Firefox()
    driver.get("https://chat.openai.com/auth/login?next=%2F%3Fmodel%3Dtext-davinci-002-render-sha")
    button = driver.find_element(By.CLASS_NAME, value="btn-primary")
    button.click()
    googleLogIn = driver.find_element(By.CLASS_NAME, value="c83859ab9")
    googleLogIn.click()
startChat()