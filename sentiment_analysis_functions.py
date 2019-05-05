import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import time
from langdetect import detect #language detection 

now = time.time()

from google.oauth2 import service_account
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import sys

######################################################################################

#Review clean up function 
def review_cleanup(df, reviews):
    '''
    This function will clean up reviews with no content, emoji, and languages that are not english will not be included
    the output of the function will be a clean dataframe with english only comments. 
    Note: This function will take some time to run if there is a lot of comments 
    '''
    # Drop NA 
    df = df.dropna()
    
    #Exclude comments with lenth less than 10 
    textlang = [detect(comment) if len(comment) > 10 else comment == 'bonju' for comment in df[reviews]]
    
    #add new variable to dataframe 
    df['language'] = textlang
    
    #dataframe filter 
    df = df[df['language'] == 'en']
    
    return df


######################################################################################

# Code from google cloud platform 
# Imports the Google Cloud client library
def language_sentiment_analysis(text):
    '''
    This function will take in words and give them a sentiment score. 
    '''
    #defind credentials for google cloud 
    credentials = service_account.Credentials.from_service_account_file('/Users/evelyn/Documents/DSI/capstone_project/googleapikey.json')
    
    #intiantiate google clinet project 
    client = language.LanguageServiceClient(credentials= credentials)
    
    #take in documents and perform sentiment analysis 
    
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
    sent_analysis = client.analyze_sentiment(document = document)
    sentiment = sent_analysis.document_sentiment
    
    return {'sent_score' : sentiment.score, 'sent_magnitude': sentiment.magnitude}


######################################################################################
def entity_sentiment_text(text):
    """Detects entity sentiment in the provided text."""
    credentials = service_account.Credentials.from_service_account_file('/Users/evelyn/Documents/DSI/capstone_project/googleapikey.json')
    client = language.LanguageServiceClient(credentials= credentials)

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    # Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16

    result = client.analyze_entity_sentiment(document, encoding)

    for entity in result.entities:
        print('Mentions: ')
        print(u'Name: "{}"'.format(entity.name))
        for mention in entity.mentions:
            print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
            print(u'  Content : {}'.format(mention.text.content))
            print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
            print(u'  Sentiment : {}'.format(mention.sentiment.score))
            print(u'  Type : {}'.format(mention.type))
            print(u'Salience: {}'.format(entity.salience))
            print(u'Sentiment: {}\n'.format(entity.sentiment))