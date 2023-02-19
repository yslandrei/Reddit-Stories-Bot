import time, os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def uploadToTikTok(threadID):
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    #options.add_argument("--headless")
    options.add_argument("user-data-dir=C:\\Users\\andre\\AppData\\Local\\Google\\Chrome Beta\\User Data")
    options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
    

    bot = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), 
        chrome_options=options
    )
    bot.get('https://www.tiktok.com/upload?lang=en')
    time.sleep(2)

    iframe = bot.find_element(By.XPATH, '//body/div[@id="__next"]/div[@id="main"]/div[2]/div[1]/iframe[1]')
    bot.switch_to.frame(iframe)
    time.sleep(1)
    
    path = f'video/export/{threadID}.mp4'
    fileUploader = bot.find_element(By.XPATH, '//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]')  
    fileUploader.send_keys(os.path.abspath(path))

    caption = bot.find_element(By.XPATH, '//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]')
    caption.send_keys('#povesti #reddit #povestireddit #fyp #askreddit #romania')
    time.sleep(15)

    post = bot.find_element(By.XPATH, '//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[8]/div[2]/button[1]')
    post.click()
    time.sleep(5)

    bot.quit()
