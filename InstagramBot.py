from selenium import webdriver
from Classes import HomePage
from time import sleep
browser = webdriver.Firefox()           # open the firefox browser
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login("yddos1", "3208411505b")


sleep(50)
browser.close()
