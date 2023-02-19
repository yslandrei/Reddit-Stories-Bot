import os
import requests


class redditGenerator:
    def __init__(self, accountData, clientID, redditApiKey):
        #Setting Up Reddit Api
        auth = requests.auth.HTTPBasicAuth(clientID, redditApiKey)
        self.__headers = {'User-Agent': 'TikTokBot/0.0.1'}
        res = requests.post('https://www.reddit.com/api/v1/access_token', 
                            auth=auth, 
                            data=accountData, 
                            headers=self.__headers)
        TOKEN = res.json()['access_token']
        self.__headers['Authorization'] = f'bearer {TOKEN}'

    def getThread(self, subreddit, category, maxCharacters, maxComments):
        res = requests.get(
            f'https://oauth.reddit.com/r/{subreddit}{category}', 
            headers=self.__headers,
            params={'limit': '100'}
        )

        threadLength = 0
        thread = {}
        for post in res.json()['data']['children']:
            if not 'selftext' in post['data']:
                continue

            if post['data']['distinguished'] == 'moderator':
                continue

            if post['data']['over_18'] == True:
                continue
            
            alreadyUsed = False
            for fileName in os.listdir('audio/output'):
                threadID = post['data']['name'][3:]
                if fileName == f'{threadID}.mp3':
                    alreadyUsed = True
                    break

            if alreadyUsed == True:
                continue  

            alreadyUsed = False
            for fileName in os.listdir('video/export'):
                threadID = post['data']['name'][3:]
                if fileName == f'{threadID}.mp4':
                    alreadyUsed = True
                    break

            if alreadyUsed == True:
                continue  

            if threadLength + len(post['data']['selftext'] + post['data']['title']) < maxCharacters:
                threadLength += len(post['data']['selftext'] + post['data']['title'])
                
                thread = {
                    'id': post['data']['name'][3:],
                    'title': post['data']['title'],
                    'text': post['data']['selftext']
                }
                break

        
        threadID = thread['id']
        res = requests.get(f'https://oauth.reddit.com/r/{subreddit}/comments/{threadID}', 
                            headers=self.__headers)
        
        thread['comments'] = []
        commentsNumber = 0
        for comment in res.json()[1]['data']['children']:
            if commentsNumber >= maxComments:
                break

            if not 'body' in comment['data']:
                continue

            if 'bot' in comment['data']['body'] or 'FAQ' in comment['data']['body']:
                continue
            
            if comment['data']['distinguished'] == 'moderator':
                continue
            
            thread['comments'].append({
                'id': comment['data']['name'][3:],
                'text': comment['data']['body']
            })

            threadLength += len(comment['data']['body'])
            if threadLength > maxCharacters:
                break

        self.replaceAbreviations(thread)

        # # testing purposes
        # thread['text'] = thread['text'][:10]
        # for comment in thread['comments']:
        #     comment['text'] = comment['text'][:10]
            
        return thread

    def replaceAbreviations(self, thread):
        # bastard = nenorocit (translation problems)
        thread['title'] = thread['title'].lower().replace('aita', 'Am i the bastard')
        thread['title'] = thread['title'].lower().replace('wibta', 'Would i be the bastard')
        thread['text'] = thread['text'].lower().replace('aita', 'Am i the bastard')
        thread['text'] = thread['text'].lower().replace('wibta', 'Would i be the bastard')
        
        for comment in thread['comments']:
            comment['text'] = comment['text'].lower().replace('yta', 'You are the bastard.')
            comment['text'] = comment['text'].lower().replace('ynta', 'You are not the bastard.')
            comment['text'] = comment['text'].lower().replace('ta', 'You are the bastard.')
            comment['text'] = comment['text'].lower().replace('nta', 'You are not the bastard.')




   

            

        
        

