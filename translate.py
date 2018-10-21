# Imports the Google Cloud client library
from google.cloud import translate

def translate_text(text, target):
    # Instantiates a client
    translate_client = translate.Client()

    # Translates some text into target language
    translation = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translation['translatedText']))
