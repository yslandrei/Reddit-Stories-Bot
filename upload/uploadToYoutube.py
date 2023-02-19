import time, os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def uploadToYoutube(threadID):
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("user-data-dir=C:\\Users\\andre\\AppData\\Local\\Google\\Chrome Beta\\User Data")
    options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
    

    bot = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), 
        chrome_options=options
    )
    bot.get('https://studio.youtube.com')
    time.sleep(3)

    uploadButton = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
    uploadButton.click()
    time.sleep(3)

    path = f'video/export/{threadID}.mp4'
    fileUploader = bot.find_element(By.XPATH, '//*[@id="content"]/input')    
    fileUploader.send_keys(os.path.abspath(path))
    time.sleep(3)

    title = bot.find_element(By.XPATH, '//*[@id="title-textarea"]')
    title.send_keys('#Shorts #reddit #redditstories #story #fyp')
    time.sleep(3)

    notMadeForKids = bot.find_element(By.XPATH, '//*[@name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]')
    notMadeForKids.click()
    time.sleep(3)

    nextButton = bot.find_element(By.XPATH, '//*[@id="next-button"]')
    for i in range(3):
        nextButton.click()
        time.sleep(3)

    public = bot.find_element(By.XPATH, '//*[@name="PUBLIC"]')
    public.click()
    time.sleep(3)

    doneButton = bot.find_element(By.XPATH, '//*[@id="done-button"]')
    doneButton.click()
    time.sleep(3)
    bot.quit()
