# -*- coding: utf-8 -*-
"""BART Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18nWDU2DTu93eIGOYP8aS5scF5o5xF97C
"""

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/Project/csv_files/updated_text_analysis.csv')

df.head(5)

from sklearn.model_selection import train_test_split
from transformers import BartTokenizer, BartForConditionalGeneration, Trainer, TrainingArguments
import torch
import pandas as pd

# Step 1: Select a smaller subset of the dataset
subset_size = 5000  # Choose the size of your subset
subset_df = df.sample(n=subset_size, random_state=42)  # Randomly select records

# Step 2: Split the dataset into training and testing sets
train_df, test_df = train_test_split(subset_df, test_size=0.2, random_state=42)

# Step 3: Load the BART tokenizer
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

# Function to tokenize the text data
def tokenize_function(examples):
    # Convert the 'document' and 'summary' columns to lists of strings
    documents = examples['document'].astype(str).tolist()
    summaries = examples['summary'].astype(str).tolist()

    # Tokenize the documents and summaries
    model_inputs = tokenizer(documents, max_length=1024, truncation=True, padding=True)
    labels = tokenizer(summaries, max_length=150, truncation=True, padding=True)

    # Add the tokenized summaries as labels for training
    model_inputs['labels'] = labels['input_ids']
    return model_inputs

# Tokenize the training and test data
train_encodings = tokenize_function(train_df)
test_encodings = tokenize_function(test_df)

# Step 4: Prepare the data for the Trainer
class SummaryDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        return item

    def __len__(self):
        return len(self.encodings['input_ids'])

train_dataset = SummaryDataset(train_encodings)
test_dataset = SummaryDataset(test_encodings)

# Step 5: Load the BART model
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# Step 6: Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    learning_rate=5e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Step 7: Create Trainer instance
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Step 8: Train the model
trainer.train()

# Optional: Evaluate the model (if needed)
results = trainer.evaluate()
print(results)

"""### Training Loss vs. Validation Loss
- The training loss decreased consistently across the three epochs, indicating that the model is effectively learning from the training data:
  - **Epoch 1**: Training Loss: **1.0784**, Validation Loss: **0.9892**
  - **Epoch 2**: Training Loss: **0.7617**, Validation Loss: **0.9894**
  - **Epoch 3**: Training Loss: **0.5362**, Validation Loss: **1.0632**
  
- The validation loss exhibited an initial decrease but increased during the third epoch, suggesting a potential overfitting issue. This indicates that while the model learns well on the training data, it may struggle to generalize to unseen data.

"""

from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu
import nltk
import torch

# Download necessary NLTK data files
nltk.download('punkt')

# Initialize ROUGE scorer
rouge_scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

# Define device and move model to that device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to generate summaries
def generate_summary(text):
    # Move model to evaluation mode
    model.eval()

    # Tokenize the input and move to the correct device
    inputs = tokenizer(text, max_length=1024, truncation=True, return_tensors="pt").to(device)

    # Generate summary
    summary_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=4, length_penalty=2.0)

    # Decode the generated summary and return
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Calculate ROUGE and BLEU scores
rouge_scores = {'rouge1': [], 'rouge2': [], 'rougeL': []}
bleu_scores = []

for idx, row in test_df.iterrows():
    # Generate model summary
    generated_summary = generate_summary(row['document'])

    # Reference summary
    reference_summary = row['summary']

    # Calculate ROUGE scores
    scores = rouge_scorer.score(reference_summary, generated_summary)
    rouge_scores['rouge1'].append(scores['rouge1'].fmeasure)
    rouge_scores['rouge2'].append(scores['rouge2'].fmeasure)
    rouge_scores['rougeL'].append(scores['rougeL'].fmeasure)

    # Calculate BLEU score
    reference_tokens = nltk.word_tokenize(reference_summary)
    generated_tokens = nltk.word_tokenize(generated_summary)
    bleu_score = sentence_bleu([reference_tokens], generated_tokens)
    bleu_scores.append(bleu_score)

# Calculate average scores
avg_rouge1 = sum(rouge_scores['rouge1']) / len(rouge_scores['rouge1'])
avg_rouge2 = sum(rouge_scores['rouge2']) / len(rouge_scores['rouge2'])
avg_rougeL = sum(rouge_scores['rougeL']) / len(rouge_scores['rougeL'])
avg_bleu = sum(bleu_scores) / len(bleu_scores)

# Print evaluation results
print(f"Average ROUGE-1 Score: {avg_rouge1:.4f}")
print(f"Average ROUGE-2 Score: {avg_rouge2:.4f}")
print(f"Average ROUGE-L Score: {avg_rougeL:.4f}")
print(f"Average BLEU Score: {avg_bleu:.4f}")

"""### Evaluation Metrics
- The evaluation results show that the model's performance could be improved:
  - **Average ROUGE-1 Score**: **0.2541** — This score indicates that the generated summaries have some overlap with the original summaries, but there's still a lot of room for improvement.
  - **Average ROUGE-2 Score**: **0.0670** — This low score suggests that the generated summaries don't contain many of the same phrases or words as the original summaries, indicating they might lack detail.
  - **Average ROUGE-L Score**: **0.1668** — This score shows that while the generated summaries have some structure, they still need to be more coherent and fluent.
  - **Average BLEU Score**: **0.0211** — This very low score means that the generated summaries are quite different from the reference summaries, showing that the model needs to do a better job at matching the original text.
"""

