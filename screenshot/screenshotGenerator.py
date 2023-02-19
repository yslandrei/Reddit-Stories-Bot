import json
import time
from playwright.sync_api import sync_playwright, ViewportSize



def takeScreenShots(subreddit, thread):
    takeScreenshotThread(
        subreddit=subreddit, 
        threadID=thread['id']
    )

    for comment in thread['comments']:
        takeScreenshotComment(
            subreddit=subreddit, 
            threadID=thread['id'], 
            commentID=comment['id']
        )

def takeTranslatedScreenShots(subreddit, thread, sourceLang, targetLang):
    takeTranslatedScreenshotThread(
        subreddit=subreddit, 
        threadID=thread['id'],
        sourceLang=sourceLang,
        targetLang=targetLang
    )

    for comment in thread['comments']:
        takeTranslatedScreenshotComment(
            subreddit=subreddit, 
            threadID=thread['id'], 
            commentID=comment['id'],
            sourceLang=sourceLang,
            targetLang=targetLang
    )

def initScreenshot(p):
    browser = p.chromium.launch(headless=True, slow_mo=0)

    context = browser.new_context(
        locale="en-us",
        color_scheme="dark",
        viewport=ViewportSize(width=1920, height=1080),
        device_scale_factor=3
    )

    cookie_file = open(
        "screenshot/cookies.json", encoding="utf-8"
    )
    cookies = json.load(cookie_file)
    cookie_file.close()
    context.add_cookies(cookies)

    return browser, context
    
    
def takeScreenshotThread(subreddit, threadID):
    with sync_playwright() as p:
        browser, context = initScreenshot(p)

        page = context.new_page()
        page.goto(f'https://www-reddit-com.translate.goog/r/{subreddit}/comments/{threadID}?_x_tr_sl=en&_x_tr_tl=enUS', timeout=0)
        page.wait_for_load_state()
        time.sleep(1)
        page.locator('[data-testid="post-container"]').screenshot(path=f'screenshot/output/{threadID}.png')
        browser.close()

def takeScreenshotComment(subreddit, threadID, commentID):
    with sync_playwright() as p:
        browser, context = initScreenshot(p)

        page = context.new_page()
        page.goto(f'https://www-reddit-com.translate.goog/r/{subreddit}/comments/{threadID}/comment/{commentID}?_x_tr_sl=en&_x_tr_tl=enUS', timeout=0)
        page.wait_for_load_state()
        time.sleep(1)
        page.locator(f"#t1_{commentID}").screenshot(path=f'screenshot/output/{threadID}_{commentID}.png')
        browser.close()


def takeTranslatedScreenshotThread(subreddit, threadID, sourceLang, targetLang):
    with sync_playwright() as p:
        browser, context = initScreenshot(p)

        page = context.new_page()
        page.goto(f'https://www-reddit-com.translate.goog/r/{subreddit}/comments/{threadID}?_x_tr_sl={sourceLang}&_x_tr_tl={targetLang}', timeout=0)
        page.wait_for_load_state()
        time.sleep(1)
        page.locator('[data-testid="post-container"]').screenshot(path=f'screenshot/output/{threadID}.png')
        browser.close()


def takeTranslatedScreenshotComment(subreddit, threadID, commentID, sourceLang, targetLang):
    with sync_playwright() as p:
        browser, context = initScreenshot(p)

        page = context.new_page()
        page.goto(f'https://www-reddit-com.translate.goog/r/{subreddit}/comments/{threadID}/comment/{commentID}?_x_tr_sl={sourceLang}&_x_tr_tl={targetLang}', timeout=0)
        page.wait_for_load_state()
        time.sleep(1)
        page.locator(f"#t1_{commentID}").screenshot(path=f'screenshot/output/{threadID}_{commentID}.png')
        browser.close()
