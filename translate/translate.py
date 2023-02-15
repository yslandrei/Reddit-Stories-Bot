from google.cloud import translate


def translateThread(thread, sourceLang, targetLang):
    translatedThread = thread
    
    translatedThread['title'] = translateText(text=translatedThread['title'], sourceLang=sourceLang, targetLang=targetLang)
    translatedThread['text'] = translateText(text=translatedThread['text'], sourceLang=sourceLang, targetLang=targetLang)
    for comment in translatedThread['comments']:
        comment['text'] = translateText(text=comment['text'], sourceLang=sourceLang, targetLang=targetLang)

    return translatedThread

def translateText(text, sourceLang, targetLang):
    '''
    Language IDs:
        English = en-Us
        Romanian = ro
    '''

    PROJECT_ID = 'tiktokbot-377721'
    LOCATION = 'global'

    if text == '':
        return text

    client = translate.TranslationServiceClient()
    parent = f'projects/{PROJECT_ID}/locations/{LOCATION}'

    response = client.translate_text(
        request={
            'parent': parent,
            'contents': [text],
            'mime_type': 'text/plain',
            'source_language_code': sourceLang,
            'target_language_code': targetLang,
        }
    )

    return response.translations[0].translated_text
