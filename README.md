# Inside Threads: Reddit Thread Summarizer

## 📜 Project Overview
**Inside Threads** is a comprehensive NLP-based project designed to transform lengthy Reddit threads into concise and actionable summaries. By utilizing cutting-edge machine learning techniques such as **BART**, **Latent Dirichlet Allocation (LDA)**, and **VADER**, this project simplifies user interactions with vast amounts of Reddit data. It provides key insights by summarizing discussions, detecting trends, and analyzing sentiment while ensuring user-friendly functionality through an intuitive **Streamlit** interface.

This project was undertaken as part of a capstone initiative, demonstrating the power of **data-driven decision-making** and **natural language processing** in solving real-world challenges.

---

## 🚀 Objectives
- Summarize extensive Reddit threads into contextually relevant, concise summaries.
- Detect and highlight trending topics using LDA.
- Perform sentiment analysis to evaluate discussion tone.
- Generate meaningful hashtags for effective content categorization.
- Provide an interactive UI for users to access insights effortlessly.

---

## 🔍 Problem Statement
Reddit generates approximately **469 million posts annually**, with daily comment volumes exceeding **7.5 million**. Extracting meaningful information from this data presents challenges:
- **Long Threads**: Thousands of comments make navigation difficult.
- **Repetitive Content**: Similar opinions are repeated, cluttering discussions.
- **Context Loss**: Key details are often lost as discussions veer off-topic.
- **Sentiment Understanding**: Limited tools exist to analyze the tone of Reddit threads effectively.

**Inside Threads** addresses these issues by employing advanced summarization techniques to distill critical insights while preserving the richness of the original conversations.

---

## 📊 Dataset and Preprocessing
### Dataset: TLDRHQ
The **TLDRHQ dataset** was chosen for its robustness in supporting text summarization tasks. Key dataset components include:
- **Id**: Unique identifiers for posts and comments.
- **Document**: Segmented user posts with special tokens marking sentence boundaries.
- **Summary**: Concise user-generated summaries (TL;DR).
- **Extractive Labels**: Highlights critical sentences within documents.
- **Rouge Scores**: Metrics for evaluating summarization quality.

### Preprocessing Pipeline
1. **Text Cleaning**: Removed noise (e.g., URLs, HTML tags, usernames).
2. **Normalization**: Converted text to lowercase while retaining punctuation.
3. **Slang Handling**: Replaced informal terms (e.g., "u" → "you", "lol" → "laughing out loud").
4. **Sentiment Analysis**: Used **VADER** to classify content as positive, negative, or neutral.
5. **Topic Modeling**: Applied **LDA** to identify recurring themes.
6. **Cosine Similarity**: Measured semantic alignment between summaries and original content.

---

## 🛠️ Model System
### Why BART?
**BART (Bidirectional and Auto-Regressive Transformer)** was selected for its exceptional performance in abstractive summarization tasks. Its dual architecture—combining a bidirectional encoder and an autoregressive decoder—makes it highly effective for handling lengthy, unstructured Reddit threads.

### Enhancements
- **RAKE Integration**: Extracts critical keywords from threads to improve summarization focus.
- **LDA Augmentation**: Enriches input documents with topic-specific keywords to enhance contextual understanding.

### Fine-Tuning Configurations
To maximize performance, multiple configurations of BART were tested by freezing encoder and decoder layers:
1. **5 Encoders, 5 Decoders (5E-5D)**:
   - Best **ROUGE-L** scores but limited precision (**BLEU**).
2. **6 Encoders, 6 Decoders (6E-6D)**:
   - Improved generalization with stable validation loss.
3. **11 Encoders, 11 Decoders (11E-11D)**:
   - **Final Configuration**: Achieved the best balance of fluency, precision, and computational efficiency.
   - **Performance Highlights**:
     - Training loss: 0.9384
     - Validation loss: 0.9853
     - Superior **ROUGE**, **BLEU**, and **BERT F1** metrics.

The **11E-11D configuration** was finalized for its ability to deliver context-rich summaries while maintaining computational efficiency.

---

## 📈 Evaluation Metrics
The model's performance was evaluated using industry-standard metrics:
- **ROUGE-1, ROUGE-2, ROUGE-L**: Measure overlap with reference summaries.
- **BLEU**: Evaluates fluency and precision in text generation.
- **BERT F1**: Assesses semantic similarity and relevance.

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
The following visualizations were developed to analyze the model’s output:
1. **Sentiment Analysis**: Highlights tonal shifts in summaries versus original documents.
2. **Cosine Similarity**: Demonstrates alignment of generated summaries with source content.
3. **Semantic Distance**: Evaluates divergence in meaning between documents and summaries.
4. **Jaccard Similarity**: Measures word overlap between text pairs.

---

## 🌟 Features
### Core Functionality:
- **Text Summarization**: Generates concise summaries preserving contextual relevance.
- **Topic Modeling**: Integrates LDA to highlight recurring themes.
- **Sentiment Analysis**: Evaluates and visualizes emotional tone.
- **Hashtag Generation**: Extracts relevant keywords and entities.

### User Interface:
- Paste Reddit threads or URLs to generate summaries and hashtags.
- Share summaries directly on social platforms like Twitter.

---


