import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import time
from langdetect import detect #language detection 

from google.oauth2 import service_account
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

now = time.time()


# Code from google cloud platform 
# Imports the Google Cloud client library
def language_sentiment_analysis(text):
    '''
    This function will take in words and give them a sentiment score. 
    '''
    #defind credentials for google cloud 
    credentials = service_account.Credentials.from_service_account_file('/home/jovyan/capstone_project/googleapikey.json')
    
    #intiantiate google clinet project 
    client = language.LanguageServiceClient(credentials= credentials)
    
    #take in documents and perform sentiment analysis 
    
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
    sent_analysis = client.analyze_sentiment(document = document)
    sentiment = sent_analysis.document_sentiment
    
    return {'sent_score' : sentiment.score, 'sent_magnitude': sentiment.magnitude}

#import english_review
english_review = pd.read_csv('data/english_comments_only.csv')


#run the function with a for loop 

sent_analysis_ggl = []
for num, reviews in enumerate(english_review['comments']): 
    if num % 1000 == 0: 
        print(num)
        pd.DataFrame(sent_analysis_ggl).to_csv('sentiment_analysis_score.csv')
    sent = language_sentiment_analysis(reviews)
    sent_analysis_ggl.append(sent)
    time.sleep(1)

pd.DataFrame(sent_analysis_ggl).to_csv('sentiment_analysis_score_final.csv')
    