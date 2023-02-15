import os
import time
import shutil
from video.videoEditor import videoEditor
from reddit.redditGenerator import redditGenerator
from audio.textToSpeechGenerator import textToSpeechGenerator
from translate.translate import translateThread
from screenshot.screenshotGenerator import takeScreenShots, takeTranslatedScreenShots


print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


with open('apiKeys.txt', 'r') as f:
    lines = []
    for line in f:
        lines.append(line.strip('\n'))

    ACCOUNT_DATA = {
        'grant_type': lines[0],
        'username': lines[1],
        'password': lines[2]
    }

    CLIENT_ID = lines[3]
    REDDIT_API_KEY = lines[4]

    SPEECH_KEY = lines[5]
    SERVICE_REGION = lines [6]


print('🟢 LOADED API KEYS')


SUBREDDIT = 'AmItheAsshole'
CATEGORY = '/top' #leave empty if you want the home subreddit page
MAX_CHARACTERS = 2000 #the maximum of characters a thread and its comments text can contain
MAX_COMMENTS = 0 #the maximum of comments a thread can contain

rGenerator = redditGenerator(
    accountData=ACCOUNT_DATA, 
    clientID=CLIENT_ID, 
    redditApiKey=REDDIT_API_KEY
)


print('🟢 CONNECTED TO REDDIT API')


VOICE_NAME = 'ro-RO-EmilNeural'

ttsGenerator = textToSpeechGenerator(
    speechKey=SPEECH_KEY,
    serviceRegion=SERVICE_REGION,
    voiceName=VOICE_NAME
)


print('🟢 CONNECTED TO MICROSOFT TTS API')

VIDEO_BACKGROUND = 'parkour2'

vEditor = videoEditor(
    bgFileName=VIDEO_BACKGROUND
)


###TESTING

i = 0
n = int(input('🟢 How many videos do you want to generate?\n🟢 '))

while(i < n):

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    startTime = time.time()
    

    thread = rGenerator.getThread(
        subreddit=SUBREDDIT, 
        category=CATEGORY, 
        maxCharacters=MAX_CHARACTERS,
        maxComments=MAX_COMMENTS
    )
    print('🟢 THREAD PULLED')


    translatedThread = translateThread(
        thread=thread,
        sourceLang='en-US', 
        targetLang='ro'
    )
    print('🟢 THREAD TRANSLATED')


    threadAudioTime = ttsGenerator.generateAudio(thread=translatedThread)
    print('🟢 TTS GENERATED')


    takeTranslatedScreenShots(
        subreddit=SUBREDDIT,
        thread=thread,
        sourceLang='en',
        targetLang='ro'
    )
    print('🟢 SCREENSHOTS GENERATED')


    vEditor.setAspectRatio(wRatio=9, hRatio=16)
    vEditor.mergeWithAudio(audioFileName=thread['id'])
    vEditor.mergeWithScreenshots(thread=thread, threadAudioTime=threadAudioTime)
    vEditor.exportVideo(videoFileName=thread['id'])

    threadID = thread['id']
    print(f'🟢 [{threadID}.mp4] EXPORTED IN {int(time.time() - startTime)} SECONDS')



    #DELETING USELESS FILES
    shutil.rmtree('audio/output')
    shutil.rmtree('screenshot/output')
    os.mkdir('audio/output')
    os.mkdir('screenshot/output')
  
    i += 1


