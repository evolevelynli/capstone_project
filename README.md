# Data Science Immersive Capstone Project: Airbnb Host Reviews Analysis


### Contributors: 
* Evelyn Li


---
## Table of Contents 

This Notebook is broken down into different sections for analysis purpose. The following links are connected to differenct section within the Notebook for simple navigation. 

---

## Notebooks:
- [0. Custom_stop_words](https://git.generalassemb.ly/billyu/Project-4-Disaster-Classification/blob/master/code/0.%20Custom_stop_words.ipynb)
- [1. NewAPI_exploration_Finalized](https://git.generalassemb.ly/billyu/Project-4-Disaster-Classification/blob/master/code/1.%20NewAPI_exploration_Finalized%20.ipynb)
- [2.a EDA Cleaning and Baseline Model](https://git.generalassemb.ly/billyu/Project-4-Disaster-Classification/blob/master/code/2.a%20EDA%20Cleaning%20and%20Baseline%20Model.ipynb)
- [2.b EDA Cleaning and Baseline Model](https://git.generalassemb.ly/billyu/Project-4-Disaster-Classification/blob/master/code/2.b%20EDA%20%26%20Visualization%20.ipynb)
- [2.c Doc2vevc_Model_Tryout](https://git.generalassemb.ly/billyu/Project-4-Disaster-Classification/blob/master/code/2.c%20Doc2vevc_Model_Tryout.ipynb)
- [2.d LDA Tryout](https://git.generalassemb.ly/billyu/Project-4-Disaster-Classification/blob/master/code/2.d%20LDA%20Tryout.ipynb)
- [3a. CountVectorizer + TFIDF for EDA modeling](https://git.generalassemb.ly/billyu/Project-4-Disaster-Classification/blob/master/code/3a.%20CountVectorizer%20%2B%20TFIDF%20for%20EDA%20modeling%20.ipynb)
- [3b. TFIDF Final Model and Tunings](https://git.generalassemb.ly/billyu/Project-4-Disaster-Classification/blob/master/code/3b.%20TFIDF%20Final%20Model%20and%20Tunings.ipynb)
- [4. Model_Testing](https://git.generalassemb.ly/billyu/Project-4-Disaster-Classification/blob/master/code/4.%20Model_Testing%20.ipynb)

---

## Problem Statement: 

---

As an active Airbnb user, I appreciate the star rating of each listing which has provided me a general understanding of how people feel about this particular listing. As an experienced Airbnb user, I know that by looking at the star rating is not enough to evaluate the details of the home. To gain a full understanding of what people like/dislike about the particular listing, reading the comments under each listing is a step you cannot miss. Comments are not only crucial to guests, but they also contain valuable insights and suggestions for hosts regarding future improvements. However, it depends on the amount of time the listing has existed; the number of comments can be overwhelming to read through one by one. With this understanding in mind, in this project, I focus on using comments to provide insights that can be quickly understood by people without reading through all comments. This project is broken down into two main parts. First is to use unsupervised learning model to extract subtopics that people tend to talk about in comments from the most and least well-performing listings. While we are trying to make the content of the comments a bit more straightforward, this also allows us to understand if there is a difference between good listing reviews and bad listing reviews. Second, we build a model using all the words in the comments to predict the overall rating for each listing. Through understanding these topics, we then can apply these topics to each listing and give both guests and hosts insight into how well the listing is doing to others in San Francisco. 

---


## Datasets: 

- data collected from `Inside Airbnb`

|     Column Name       |                          Description                          |
|:---------------------:|:-------------------------------------------------------------:|
|  listing_id           |                    listing id for each listing                |
|    comment            |                  content for each listing                     |
| review_scores_rating  |                rating for each listing                        |
|      compound         |           sentiment score from sentiment analysis             |

---



## Model Summary 
---

regression estimators: 

4 different models deployed, 3 vectorization methods, 1 sets of features (Comments) 
 
Hyperparameter Tuning:

1. Stop words and customized stop words (remove locations names, like countries, regions, states, cities)
2. Tokenize and Lemmatize
3. Features (content only, and content + description)
4. Grid Search
 
Final model selection: 

1. TFIDF + custom location stop words + Logistic Regression
2. Pull out key parameters (top feature words & coefficients)
3. Compare the coefficients and feature name before and after the customized stop words


---

## Conclusion & Recommendation 
---

Overall, there seems to be an underlying theme of all comments regardless of housing types and location. However, due to the amount of time given to this project and the long process of learning about the relationship between comment and rating, the baseline model built for the prediction purpose did not give us a satisfying result. However, the lack of connection between comments and rating score has provided us with a new perspective which is to think about the reliability of the rating and ask if Airbnb can come up with a more realistic, and honest rating scale for evaluation purpose. The work of research does not stop here. There is more to find and more method to try out.


## References 
---

1. L. Susan. “Multi-Class Text Classification with LSTM” Medium. 9 April, 2019.
2. D. Blei, A. Ng, and M. Jordan. ”Latent Dirichlet Allocation.” Journal of Machine Learning Research, 3:9931022, January 2003.
3. D. Cai, Q. Mei, et all. ”Modeling Hidden Topics on Document Manifold.” Department of Computer Science, University of Illinois. CIKM 2008.
4. B. Sanjai, M. Fenna, et all. ” Sentiment Analysis with Long Short-Term Memory networks.” Semantic Scholar, 2018.