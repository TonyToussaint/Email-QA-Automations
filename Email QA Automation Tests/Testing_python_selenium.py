# Python program to demonstrate
# selenium
 
# import webdriver
from selenium import webdriver

# import by (wtf lmao?)
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()
 
# enter keyword to search - unsure what this is for 
keyword = "geeksforgeeks"
 
# get geeksforgeeks.org
driver.get("https://en.wikipedia.org/wiki/Cristiano_Ronaldo")
 
# get element 
#element = driver.find_element_by_class_name("gsc-input")
element = driver.find_element(By.ID, "firstHeading")
 
# print complete element
print('Testing element output: ', element.text)





'''from selenium import webdriver

# Initialize Selenium WebDriver (choose appropriate browser driver)
driver = webdriver.Chrome()

# Open the email in a webmail interface (replace URL with actual URL)
driver.get("https://your-webmail.com/inbox")

# Find and click all links in the email
links = driver.find_elements_by_tag_name("a")
for link in links:
    # Click the link
    link.click()
    
    # Verify the URL of the current page (or handle redirection if needed)
    current_url = driver.current_url
    expected_url = link.get_attribute("href")
    assert current_url == expected_url, f"Link {link.text} does not navigate to the expected URL: {expected_url}"

# Close the browser
driver.quit() '''
