import numpy as np 
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer
from flask import Flask, render_template, request, jsonify
import pinecone
import json

pinecone_environment = "pinecone-environment_name"
pinecone_api = "your_API_key"
index_name = "your_index_name"

def initialize_pinecone():
    pinecone.init(api_key=pinecone_api, environment=pinecone_environment)

def initialize_index():
    index = pinecone.Index(index_name=index_name)
    return index

def initialize_model(model_name='average_word_embeddings_glove.6B.300d'):
    model = SentenceTransformer(model_name)
    return model

def preprocess_doc(doc):
    # Convert to lowercase
    doc = doc.lower()
    # Remove numbers and punctuation
    doc = re.sub(r'\d+', '', doc)
    doc = doc.translate(str.maketrans('', '', string.punctuation))
    # Tokenize the document
    tokens = nltk.word_tokenize(doc)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if not token in stop_words]
    # Lemmatize the tokens
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(token) for token in tokens]
    # Join the tokens back into a string
    preprocessed_doc = ' '.join(tokens)
    return preprocessed_doc

def query_topk(input_sentence, topk = 10):
    preprocessed_Sent = preprocess_doc(input_sentence)
    encoded_query = model.encode(preprocessed_Sent).tolist()
    results = index.query(encoded_query, top_k = topk, include_metadata=True)
    id, titles, authors, publications, scores = [], [], [], [], []
    for res in  results["matches"]:
        id.append(res['id'])
        titles.append(res['metadata']['title'])
        publications.append(res['metadata']['publication'])
        authors.append(res['metadata']['author'])
        scores.append(str(np.round(res['score']*100,2)) + " %")
    query_results = {'ID' : id, 'Titles': titles, 'Publications': publications, "Authors" : authors, "Scores" : scores}
    return query_results

initialize_pinecone()
index = initialize_index()
model = initialize_model()

app = Flask(__name__)

# route for base page
@app.route('/')
def home():
    return render_template("index.html")

# route for search query
@app.route('/query', methods=['POST', 'GET'])
def query():
    # Extract input data from form submission
    if request.method == "POST":
        input_text = request.form.get('text')
    if request.method == "GET":
        input_text = request.args.get("text")
    # print(input_text)
    results = query_topk(input_text) # Call the pre-defined query function with the input data
    return json.dumps(results)
    
if __name__ == '__main__':
    app.run(debug=True)
