from moviepy.editor import *
from moviepy.video.fx.crop import *


class videoEditor:
    def __init__(self, bgFileName):
        self.__video = VideoFileClip(f'video/backgrounds/{bgFileName}.mp4', audio=False)     

    def setAspectRatio(self, wRatio, hRatio):
        oldHeight = self.__video.h
        oldWidth = self.__video.w

        newHeight = oldHeight
        newWidth = newHeight * wRatio / hRatio

        self.__video = crop(self.__video, x_center=oldWidth/2, y_center=oldHeight/2, width=newWidth, height=newHeight)

    def mergeWithAudio(self, audioFileName):
        audio = AudioFileClip(f'audio/output/{audioFileName}.mp3')
        self.__video.audio = CompositeAudioClip([audio])
        self.__video = self.__video.set_duration(audio.duration)

    def mergeWithScreenshots(self, thread, threadAudioTime):
        #thread
        threadID = thread['id']
        threadScreenshots = [self.__video]
        lastAudioTime = 0

        screenshot = (ImageClip(f'screenshot/output/{threadID}.png')
            .set_start(lastAudioTime)
            .set_duration(threadAudioTime[threadID])
            .resize(width=self.__video.w * 0.75)
        )
        centerW = ((self.__video.w - screenshot.w) / 2)
        centerH = (self.__video.h - screenshot.h) / 2
        screenshot = screenshot.set_position((centerW, centerH * 0.50))
        threadScreenshots.append(screenshot)

        lastAudioTime += threadAudioTime[threadID]

        #comments
        for comment in thread['comments']:
            commentID = comment['id']

            screenshot = (ImageClip(f'screenshot/output/{threadID}_{commentID}.png')
                .set_start(lastAudioTime)
                .set_duration(threadAudioTime[commentID])
                .resize(width=self.__video.w * 0.75)
            )
            centerW = ((self.__video.w - screenshot.w) / 2)
            centerH = (self.__video.h - screenshot.h) / 2
            screenshot = screenshot.set_position((centerW, centerH * 0.50))
            threadScreenshots.append(screenshot)

            lastAudioTime += threadAudioTime[commentID]

        self.__video = CompositeVideoClip(threadScreenshots)

    def exportVideo(self, videoFileName):
        self.__video.write_videofile(f'video/export/{videoFileName}.mp4')

        
        
    

