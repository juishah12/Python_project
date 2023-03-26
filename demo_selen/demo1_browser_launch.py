import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome() #init will launch it
d.get("http://google.com")
d.title
print(d.title)
time.sleep(15)

