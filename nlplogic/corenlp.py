
from textblob import TextBlob
import wikipedia

def search_wikipedia(name):
    """ search wikipedia """
    print(f"Searching for name: {name}")
    return wikipedia.search(name)

def summarize_wikipedia(name):
    """ Summarize Wikipedia"""
    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)

def get_text_blob(text):
    """ Gets txt blob objects and returns """
    blob = TextBlob(text)
    return blob

def get_phrases(name):
    """ Find Wikipedia name and return back phrases """
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases



