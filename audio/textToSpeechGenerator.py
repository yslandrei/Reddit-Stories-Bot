import azure.cognitiveservices.speech as speechsdk
from mutagen.wave import WAVE
from moviepy.editor import *


class textToSpeechGenerator:
    def __init__(self, speechKey, serviceRegion, voiceName):
        #Setting up Microsoft Azure TTS Api
        self.__speechConfig = speechsdk.SpeechConfig(subscription=speechKey, region=serviceRegion)
        self.__speechConfig.speech_synthesis_voice_name = voiceName

    def generateAudio(self, thread):

        threadAudioTime = {}
        threadID = thread['id']
        audioNumber = 0
        
        audioConfig = speechsdk.audio.AudioOutputConfig(filename=f'audio/output/{threadID}_{audioNumber}.mp3')
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.__speechConfig, audio_config=audioConfig)
        synthesizer.speak_text(text=thread['title'] + thread['text'])

        #threadAudioTime[threadID] = WAVE(f'audio/output/{threadID}_{audioNumber}.mp3').info.length        
        audioNumber += 1

        for comment in thread['comments']:
            audioConfig = speechsdk.audio.AudioOutputConfig(filename=f'audio/output/{threadID}_{audioNumber}.mp3')
            synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.__speechConfig, audio_config=audioConfig)
            synthesizer.speak_text(text=comment['text'])

            #threadAudioTime[comment['id']] = WAVE(f'audio/output/{threadID}_{audioNumber}.mp3').info.length        
            audioNumber += 1

        audioClips = [AudioFileClip(f'audio/output/{threadID}_0.mp3')]
        threadAudioTime[threadID] = audioClips[0].duration

        n = 1
        for comment in thread['comments']:
            audioClips.append(AudioFileClip(f'audio/output/{threadID}_{n}.mp3'))
            threadAudioTime[comment['id']] = audioClips[n].duration
            n += 1

            
        finalAudioClip = concatenate_audioclips(audioClips)
        finalAudioClip.write_audiofile(f'audio/output/{threadID}.mp3')

        return finalAudioClip.duration, threadAudioTime
