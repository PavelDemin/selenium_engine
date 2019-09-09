from selenium import webdriver
from time import sleep
import constants


chromedriver_path = 'C:\\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)


def init(webdriver):
    constants.init()
    login(webdriver)


def login(webdriver):
    #Open the instagram login page
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    #sleep for 3 seconds to prevent issues with the server
    sleep(3)
    #Find username and password fields and set their input using our constants
    username = webdriver.find_element_by_name('username')
    username.send_keys(constants.INST_USER)
    password = webdriver.find_element_by_name('password')
    password.send_keys(constants.INST_PASS)
    #Get the login button
    try:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
    except:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button/div')
    #sleep again
    sleep(2)
    #click login
    button_login.click()
    sleep(3)
    #In case you get a popup after logging in, press not now.
    #If not, then just return
    try:
        notnow = webdriver.find_element_by_css_selector(
            'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click()
    except:
        return


def get_last_post(webdriver, account):
    webdriver.get(('https://www.instagram.com/{}/').format(account))
    sleep(5)
    post_xpath = '//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div/div/a'
    a = webdriver.find_element_by_xpath(post_xpath)
    url = a.get_attribute('href')
    print(url)

if __name__ == "__main__":
    init(webdriver)
    get_last_post(webdriver, 'borodylia')
    webdriver.close()