# Inside Threads: Reddit Thread Summarizer

## 📜 Project Overview
**Inside Threads** is a comprehensive NLP project designed to summarize lengthy Reddit threads, identify trending topics, perform sentiment analysis, and generate hashtags. It addresses the challenges posed by unstructured, verbose content by transforming it into concise, meaningful summaries that enhance user engagement and accessibility.

This project integrates advanced machine learning techniques, including the **BART** transformer model, **Latent Dirichlet Allocation (LDA)** for topic modeling, and **VADER** for sentiment analysis. A user-friendly interface powered by **Streamlit** makes it easy for users to input data and access insights.

---

## 🚀 Objectives
The primary goal is to simplify the navigation of large volumes of user-generated Reddit content by:
- Summarizing long threads into concise, contextually relevant text.
- Identifying and highlighting trending topics using LDA.
- Conducting sentiment analysis to understand the tone of conversations.
- Generating meaningful hashtags for better content categorization.
- Providing a streamlined UI for non-technical users.

---

## 🔍 Problem Statement
Reddit, as a platform, generates massive amounts of data daily, with threads often exceeding thousands of comments. Key challenges include:
- **Long Threads**: Difficulty in navigating thousands of comments.
- **Repetitive Content**: Redundancy in discussions adds clutter.
- **Context Loss**: Tangential comments dilute the primary discussion focus.
- **Sentiment Understanding**: Limited tools to analyze the tone of conversations effectively.

This project tackles these challenges by providing efficient, AI-powered summarization and analysis tools tailored to Reddit's unique structure.

---

## 📊 Dataset and Preprocessing
### Dataset: TLDRHQ
This project uses the **TLDRHQ dataset**, a robust collection designed for summarization tasks. Key features of the dataset include:
- **Id**: Unique identifiers for posts and comments.
- **Document**: Segmented user posts with boundary markers.
- **Summary**: Concise, user-generated post summaries.
- **Ext_labels**: Extractive labels highlighting critical sentences.
- **Rg_labels**: Rouge scores for evaluating summarization quality.

### Preprocessing Steps
1. **Data Cleaning**: Removed URLs, usernames, and special characters using regex.
2. **Normalization**: Converted text to lowercase and preserved punctuation.
3. **Handling Slang**: Replaced informal terms (e.g., "lol" → "laughing out loud").
4. **Sentiment Scoring**: Used **VADER** to categorize content as positive, negative, or neutral.
5. **Topic Modeling**: Applied **LDA** to identify themes.
6. **Cosine Similarity**: Measured alignment between summaries and documents.

---

## 🛠️ Model System
### Why BART?
**BART (Bidirectional and Auto-Regressive Transformer)** was chosen for its dual capabilities:
- **Contextual Understanding**: Excels in abstractive summarization by processing both left and right contexts.
- **Fine-tuning Flexibility**: Easily adaptable for domain-specific tasks.

### Enhancements
- **LDA Integration**: Augments input with topic-specific keywords to improve summarization quality.
- **RAKE Integration**: Extracts critical keywords to refine model focus.

### Fine-Tuning Process
1. Experimented with freezing encoder/decoder layers to optimize learning.
2. Tested various learning rates to balance speed and accuracy.
3. Adjusted summary length to reduce neutral tones and improve relevance.

---

## 📈 Evaluation Metrics
The performance of the summarization model was assessed using:
- **ROUGE-1, ROUGE-2, ROUGE-L**: Measures overlap between generated summaries and references.
- **BLEU**: Evaluates the fluency of summaries.
- **BERT F1**: Analyzes semantic similarity to assess relevance.

### Results:
| Metric        | Score   |
|---------------|---------|
| ROUGE-1       | 0.2648 |
| ROUGE-2       | 0.0782 |
| ROUGE-L       | 0.1917 |
| BLEU          | 0.0217 |
| BERT F1       | 0.2416 |

---

## 📊 Visual Insights
1. **Sentiment Analysis**: Visualized tonal shifts introduced by summarization.
2. **Cosine Similarity**: Demonstrated semantic alignment of summaries with original content.
3. **Semantic Distance**: Highlighted variability in prediction quality.
4. **Jaccard Similarity**: Compared word overlap across texts.

---

## 🌟 Features
### Core Functionality:
- **Summarization**: Generates concise, context-aware summaries.
- **Topic Modeling**: Identifies and integrates key discussion themes.
- **Sentiment Analysis**: Evaluates the emotional tone of threads.
- **Hashtag Generation**: Extracts relevant entities and keywords.

### User Interface:
- Intuitive input for pasting Reddit threads or providing URLs.
- Outputs concise summaries, hashtags, and sentiment analysis results.
- Sharing option for direct content posting on Twitter.

---

## 🧩 Architecture
1. **Input Processing**: Text cleaning, slang normalization, and topic enrichment.
2. **Summarization**: BART model fine-tuned with LDA topics for context-rich summaries.
3. **Output**: Visualizations, hashtags, and summary export.

---

