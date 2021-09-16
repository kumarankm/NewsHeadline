from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("chromedriver_win32\chromedriver.exe")

driver.get("https://www.epicenternews.net")

# driver.find_element_by_id("input_search-box-input-comp-k84bxp22").send_keys("news")
'''
arr = []
for i in range(5):
    ele = driver.find_element_by_class_name('blog-post-homepage-title-color')
    arr.append(ele.text)
print(arr)
'''
ele = driver.find_element_by_css_selector(
    ".blog-post-homepage-title-color blog-post-homepage-title-font _3gVhF")
print(ele.text)
