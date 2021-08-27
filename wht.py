from selenium import webdriver
driver = webdriver.Chrome('C:\\webdriver\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://web.whatsapp.com')
def spam():
    driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
    inputString = input("Enter message to send: ")
    i=int(input("Enter no. of messages: "))
    while(i):
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(inputString)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button').click()
        #driver.implicitly_wait(10)
        i-=1
while(True):
    spam()