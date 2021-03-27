from selenium import webdriver
from Classes import HomePage
from time import sleep
browser = webdriver.Firefox()                       # open the firefox browser
browser.implicitly_wait(5)

home_page = HomePage(browser)                       #creating a HomePage object that will store the home_page
login_page = home_page.go_to_login_page()           #calling the go_to_login_page method in order to login in the appropriate page
login_page.login("my username", "<my password")     #giving the appropriate usarname and password in order to login with my account


sleep(50)                                           #the program will wait 50 seconds before it's closed 
browser.close()
