from deep_translator import GoogleTranslator
import requests as re
from loguru import logger

URL = 'https://api.adviceslip.com/advice'

def get_advice_api():
    try:
        result = re.get(URL)
        id_ad = result.json()['slip']['id']
        ad_txt = result.json()['slip']['advice']
        return id_ad ,ad_txt

    except Exception as e:
        logger.exception(e)
        return None,None


def get_translated_api(txt_adv):
    try:
        return GoogleTranslator(source='en', target='pt').translate(txt_adv)
    except Exception as e:
        logger.exception(e)
        return None

def get_original_api(txt_adv):
    try:
        return GoogleTranslator(source='pt', target='en').translate(txt_adv)
    except Exception as e:
        logger.exception(e)
        return None