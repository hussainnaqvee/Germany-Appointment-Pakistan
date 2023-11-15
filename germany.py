from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

option_list = ['',
               'Stipendiat bei Finanzierung durch deutsche Wissenschafts- oder Mittlerorganisation z.B. DAAD oder AvH/Recipient of a full scholarship paid by an official German academic institution e.g. DAAD or AvH',
               'Promotionsstudenten mit Zulassung einer deutschen Universität/Phd students holding an admission letter from a german university',
               'Studienvorbereitung (z.B. Sprachkurs mit anschließendem Studienkolleg)/Study preparation (e.g. language course followed by a foundation course)',
                'Sprachkurse zu anderen als Studienzwecken/Language courses for purposes other than study'
               ]
def setup_driver():
    driver = webdriver.Chrome()

    return driver

def navigate_to_page(driver, url):
    # Go to the provided URL
    driver.get(url)

def teardown_driver(driver):
    # Close the driver
    driver.quit()

def main():
    driver = setup_driver()
    isAvailable = False
    while(isAvailable == False):
        try:
            navigate_to_page(
                driver, "https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600")
        
            time.sleep(5)
            element = driver.find_element(
                By.CSS_SELECTOR, 'select[id="appointment_newAppointmentForm_fields_3__content"]')
            options = element.find_elements(By.TAG_NAME,'option')
            if len(options)>5:
                isAvailable = True
            print(len(options))
            for op in options:
                if op.accessible_name not in option_list and 'Master' in op.accessible_name:
                    print(op.accessible_name)
                    isAvailable = True
            time.sleep(25)
        except:
            print("error, Check your internet conenction or website is down.")
    
    print("Appointments are now open.")
    teardown_driver(driver)

if __name__ == "__main__":
    main()