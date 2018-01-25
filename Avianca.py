import logging
from selenium import webdriver
import time

# def page_has_loaded():
    # new_page = browser.find_element_by_tag_name('html')
    # return new_page.id != old_page.id

# def wait_for(condition_function):
    # start_time = time.time()
    # while time.time() < start_time + 3:
        # if condition_function():
            # return True
        # else:
            # time.sleep(0.1)
    # raise Exception('Timeout waiting for {}'.format(condition_function.__name__))
	
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
browser.implicitly_wait(5)
browser.get('https://www.lifemiles.com')
userName = browser.find_element_by_id('txtUser')
# userName.send_keys('USER')
passwordElem = browser.find_element_by_id('txtPassword')
# passwordElem.send_keys('PASSWORD')
# userName.submit()
loginButton = browser.find_element_by_id('botonlogin')
loginButton.click()
# old_page = browser.find_element_by_tag_name('html')
# print(old_page)
# while (old_page == browser.find_element_by_tag_name('html')):
logging.debug('Ready to request Redime site')
browser.get('https://lifemiles.com/esp/use/red/dynredpar.aspx')
requirementsForm = browser.find_element_by_id('requirementsform')

# try:
    # logging.debug('Before WebDriverWait')
    # element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "requirementsform")))
    # logging.debug('After WebDriverWait')
# finally:
    # logging.debug('finally')
    # browser.quit()
# wait_for(page_has_loaded)
# RedimeButton = browser.find_element_by_xpath(r'//*[@id="mainMenu"]/li[4]')
# RedimeButton.click()
# old_page = browser.find_element_by_tag_name('html')
# browser.get('https://lifemiles.com/esp/use/red/dynredpar.aspx')
# wait_for(page_has_loaded)
# browser.find_element_by_link_text('Redime').click()

