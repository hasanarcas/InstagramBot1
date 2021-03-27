from time import sleep

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")            #it finds the appropriate place of the username input
        password_input = self.browser.find_element_by_css_selector("input[name='password']")            #it finds the appropriate place of the password input
        username_input.send_keys(username)                                                              #it will take the username parameter that we sent through the main function
        password_input.send_keys(password)                  
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(1)
        try:
            event_handler = self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
            event_handler.click()
        except:
            pass
        try:
            event_handler = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
            event_handler.click()
        except:
            pass
        try:
            event_handler = self.browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/button[2]")
            event_handler.click()
        except:
            pass
        sleep(1)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):             # the name explains itself
        sleep(2)
        return LoginPage(self.browser)

    def go_to_messages(self):               # the name explains itself
        messages_page = self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
        messages_page.click()
