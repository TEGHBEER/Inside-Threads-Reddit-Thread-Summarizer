# -*- coding: utf-8 -*-
"""Updated Text Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/173D2I6qEFl_Szn1ff-XBy0yn9717IOjZ
"""

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/Project/csv_files/updated_cleaned_data.csv')

df.head(5)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Function to calculate sentiment scores
def vader_sentiment(text):
    return sia.polarity_scores(text)

# Fill NaN values in columns with empty strings
df['document'] = df['document'].fillna('')
df['summary'] = df['summary'].fillna('')

# Apply VADER sentiment analysis
df['document_sentiment'] = df['document'].apply(lambda x: vader_sentiment(x)['compound'])
df['summary_sentiment'] = df['summary'].apply(lambda x: vader_sentiment(x)['compound'])

# Display the DataFrame with the sentiment scores
df[['document', 'document_sentiment', 'summary', 'summary_sentiment']].head(5)

def interpret_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['document_sentiment'] = df['document_sentiment'].apply(interpret_sentiment)
df['summary_sentiment'] = df['summary_sentiment'].apply(interpret_sentiment)

df[['document', 'document_sentiment', 'summary', 'summary_sentiment']].head(5)

from gensim import corpora
from gensim.models import LdaModel
import pandas as pd

# Ensure each entry in 'document' and 'summary' is a list of tokens
df['document_token'] = df['document'].apply(lambda x: x.split() if isinstance(x, str) else [])
df['summary_token'] = df['summary'].apply(lambda x: x.split() if isinstance(x, str) else [])

# Create a dictionary and corpus for the documents
dictionary_docs = corpora.Dictionary(df['document_token'])
corpus_docs = [dictionary_docs.doc2bow(text) for text in df['document_token'] if text]

# Create and fit the LDA model for the documents
lda_model_docs = LdaModel(corpus=corpus_docs, id2word=dictionary_docs, num_topics=10, random_state=42)

# Create a mapping of topic numbers to topic words
topic_words_docs = {i: ' + '.join([f'"{word}"' for word, _ in lda_model_docs.show_topic(i, topn=5)]) for i in range(lda_model_docs.num_topics)}

# Add topic words to the DataFrame instead of topic numbers
df['document_topics'] = [max(lda_model_docs[doc], key=lambda x: x[1])[0] if doc else -1 for doc in corpus_docs]
df['document_topics'] = df['document_topics'].map(topic_words_docs)

# Create a dictionary and corpus for the summaries
dictionary_summaries = corpora.Dictionary(df['summary_token'])
corpus_summaries = [dictionary_summaries.doc2bow(text) for text in df['summary_token'] if text]

# Create and fit the LDA model for the summaries
lda_model_summaries = LdaModel(corpus=corpus_summaries, id2word=dictionary_summaries, num_topics=10, random_state=42)

# Create a mapping of topic numbers to topic words for summaries
topic_words_summaries = {i: ' + '.join([f'"{word}"' for word, _ in lda_model_summaries.show_topic(i, topn=5)]) for i in range(lda_model_summaries.num_topics)}

# Initialize summary topics with NaN to ensure matching length
df['summary_topics'] = pd.NA

# Populate summary topics directly into the DataFrame
for index, row in df.iterrows():
    if row['summary_token']:  # Check if summary_token is not empty
        doc = dictionary_summaries.doc2bow(row['summary_token'])
        if doc:  # Ensure doc is not empty
            topic = max(lda_model_summaries[doc], key=lambda x: x[1])[0]
            df.at[index, 'summary_topics'] = topic_words_summaries[topic]
    else:
        df.at[index, 'summary_topics'] = 'No Topic'  # Placeholder for empty summaries

# Optionally fill remaining NaN values with a placeholder
df['summary_topics'].fillna('No Topic', inplace=True)

df[['document_token', 'document_topics', 'summary_token', 'summary_topics']].head(5)

df.head(5)

df.to_csv('/content/drive/MyDrive/Project/csv_files/updated_text_analysis.csv', index=False)

