# Plagiarism Detection Using NLP

## Overview

The Plagiarism Detection project aims to identify and measure similarities between textual content, allowing for the detection of potential plagiarism. Leveraging Natural Language Processing (NLP) techniques and open source large language models, the system analyzes a dataset of 126,000 documented articles to determine instances of content similarity.

## Development Process

### 1. Data Preprocessing

The first step involved the collection of a diverse dataset of 126,000 articles. This dataset was then preprocessed, which included tasks such as text cleaning, stemming, and removing stop words. The goal was to transform raw textual data into a format suitable for NLP analysis.

### 2. Vectorization

To enable machine learning algorithms to work with the textual data, the articles were vectorized using the Sentence Transformer model. This advanced model transforms sentences into high-dimensional vectors, capturing semantic relationships between words and phrases.

### 3. Front-end Development

The project includes a user-friendly front-end developed using HTML, CSS, and JavaScript. Users can interact with the system through a web interface, where they can input text for plagiarism analysis.

### 4. Back-end Development

The back-end of the system is powered by Flask, a Python web framework. It handles the communication between the front-end and the machine learning model. The Flask app receives user input, processes it through the transformer model, and returns the plagiarism analysis results.

### 6. Performance Evaluation

The performance of the plagiarism detection model was evaluated using various metrics such as accuracy, precision, recall, and F1-score. This step ensured the model's effectiveness in identifying instances of plagiarism while minimizing false positives and false negatives.


## Working:
A custom query function was built to retreive the results from the database. All the articles are stored in a vector format on the vector database PINECONE. Whenever a user inputs a block of text, it is then preprocessed (like stop words removal, punctuations etc.) and then the transformer model encodes the text into a vector. Through the custom query function topK articles are pulled based on the metric COSINE-SIMILARITY and their details along with the percentage similarity is displayed to the user.
