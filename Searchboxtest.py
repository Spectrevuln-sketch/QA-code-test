from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
browser.set_window_size(900,900)
browser.set_window_position(0,0)
sleep(1)
browser.get("https://www.amazon.com/")
browser.find_element_by_id("searchDropdownBox").send_keys("Computers,Electronics,office")
browser.find_element_by_id("twotabsearchtextbox").send_keys("Television & Video")
browser.find_element_by_linkText("Go").click()
sleep(60)

browser.find_element_by_id("searchDropdownBox").send_keys(Keys.RETURN)
browser.find_element_by_id("twotabsearchtextbox").send_keys(Keys.RETURN)




sleep(60)
browser.reload()
browser.close()
