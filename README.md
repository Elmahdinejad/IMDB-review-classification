# IMDB Review Classification Project


## Overview

In this project, I developed a sentiment analysis model to classify movie reviews from the IMDB dataset as either positive or negative. The goal was to identify the sentiment expressed in reviews based on the text content, providing insights into public opinion about various films.

## Dataset

The dataset used for this project consists of 50,000 movie reviews from IMDB, which are evenly divided into 25,000 training and 25,000 testing samples. Each review is labeled as positive (1) or negative (0).

## Data Preprocessing

Tokenization: I tokenized the review texts, converting them into sequences of integers where each integer represents a particular word in the review.

Padding: To ensure uniformity in input size, I padded the sequences to a maximum length of 200 words, allowing the model to process each review effectively.

Encoding: I limited the vocabulary to the top 10,000 most frequent words, simplifying the input data while retaining essential information.

## Model Building

I constructed a Sequential neural network model using Keras:

Embedding Layer: This layer transforms the integer-encoded words into dense vector representations, allowing the model to learn semantic relationships between words.

LSTM Layer: I incorporated a Long Short-Term Memory (LSTM) layer to effectively capture temporal dependencies in text data, making it suitable for sequence prediction problems.

Dense Layer: A final dense layer with a sigmoid activation function was added to produce the binary output indicating the sentiment.

## Model Training

The model was compiled using the binary cross-entropy loss function, and the Adam optimizer was employed for efficient optimization. I trained the model on the training dataset for 5 epochs with a batch size of 64, and monitored validation loss to prevent overfitting.

## Evaluation

After training, I evaluated the model's performance on the test set, achieving an accuracy of approximately 88%. This metric indicates the model's effectiveness in correctly classifying the sentiments of unseen reviews.

## Conclusion

This project successfully demonstrates the application of neural networks in natural language processing, specifically for sentiment analysis. The implementation of the IMDB review classification model has provided valuable insights into handling text data and building robust classification models. The skills developed during this project can be extended to similar applications in the field of NLP.
