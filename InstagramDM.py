from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

from_username = input("Enter the user name to send from: ")
from_user_password = input("Enter the user password: ")

to_username = input("Enter user name: ")
msg = input("Enter message: ")
num = int(input("How many times send the message? "))

# Create WebDriver
chrome_options = Options()
chrome_options.add_argument("maximized")
driver = webdriver.Chrome(r"C:\Users\illay\Programming\chromedriver.exe",
                          options=chrome_options)
try:
    driver.get('https://www.instagram.com/')
    time.sleep(1)

    # Enter user name + password
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(from_username)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(from_user_password)
    time.sleep(1)

    # Log in to instagram
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
    time.sleep(4)
    print("\nConnected to instagram.")

    # Ordinary clicks
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    time.sleep(0.2)
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(1)
    except NameError:
        pass

    # Go to user
    driver.get('https://www.instagram.com/' + to_username + '')
    time.sleep(2)
    print("In user's profile.")

    # Go to messages with the user
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button').click()
    time.sleep(1)
    print("In DM.")

    for i in range(num):
        # Type message
        driver.find_element_by_xpath(
            "//body/div[@id='react-root']/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div["
            "1]/div[ "
            "1]/div[2]/textarea[1]").send_keys(msg)
        # Send message
        driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div['
                                     '2]/div/div/div[ '
                                     '3]/button').click()

    if num > 1:
        print("\nMessages sent")
    else:
        print("\nMessage sent")

except NameError:
    print(NameError)

driver.close()
driver.quit()
