from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
from playsound import playsound as play


def setup_driver():
    driver = webdriver.Chrome()

    return driver

def navigate_to_page(driver, url):
    # Go to the provided URL
    driver.get(url)

def close_driver(driver):
    # Close the driver
    driver.quit()

def main():
    driver = setup_driver()
    isAvailable = False
    while(isAvailable == False):
        try:
            navigate_to_page(
                driver, "https://service2.diplo.de/rktermin/extern/choose_categoryList.do?locationCode=isla&realmId=108&request_locale=en")
        
            time.sleep(5)
            divs = driver.find_elements(By.CSS_SELECTOR, 'div[style="font-size: 14pt; font-weight: bold; margin-bottom: 1em;"]')
            for div in divs:
                if 'study' in div.text.lower():
                    print(div.text)
                    isAvailable = True
                    break
        except:
            print("error, Check your internet conenction or website is down.")
    if isAvailable:
        close_driver(driver)
    while(isAvailable):
        try:
            play('mixkit-classic-winner-alarm-1997.wav')
            print("Appointments are now open.")
        except KeyboardInterrupt:
            sys.exit()

    

if __name__ == "__main__":
    main()