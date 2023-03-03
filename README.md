# Description

A Python bot that generates Reddit Story Videos and automatically posts them on TikTok / Youtube Shorts. The script pulls threads from a given subreddit, adds Text-To-Speech, and edits them into short videos over some gameplay footage.

# How it works

* Pulls a random thread from a certain subreddit using the **Reddit API**
* Translates the thread(if needed) using the **Google Translate API**
* Generates the Text-To-Speech using **Microsoft's Azure Speech API**
* Takes screenshots using **Playwright**
* Edits the video using **MoviePy**
* Posts the video using **Selenium**

# How to use it

If you wish to use this bot on your machine, you will need to get your own API keys from Reddit, Microsoft Azure and Google Cloud and put them in a file called apiKeys(check the code in main.py for formatting). Also, you will need to update the path of your Chrome Beta browser in the upload functions. Once you do that you will need to install:
* Mutagen
* MoviePy
* Azure.Cognitiveservices.Speech
* Playwright
* Google-Cloud
* Selenium
* Webdriver_Manager

# Results

Here's a video created by this bot:


https://user-images.githubusercontent.com/7760397/222571103-422ca8f9-6178-4129-8d6b-32cf7363aea4.mp4





