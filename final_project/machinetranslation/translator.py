import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

# language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    if english_text is None:
        return None
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    return translation.get("translations")[0].get('translation')


def french_to_english(french_text):
    if french_text is None:
        return None
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    return translation.get('translations')[0].get('translation')


# print(json.dumps(englishToFrench("Hello"), indent=2, ensure_ascii=False))
# print(json.dumps(frenchToEnglish("Bonjour®"), indent=2, ensure_ascii=False))
