from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("chromedriver_win32\chromedriver.exe")
driver.get(r'C:\Users\Admin\Desktop\Headline detector\index.html')

i = 1
arr = []
for _ in range(3):
    ca = "head" + str(i)
    arr.append(driver.find_element_by_id(ca).text)
    i += 1
print(arr)
