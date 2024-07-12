#-------------------------------------------------------------------------
# AUTHOR: Dylan Monge
# FILENAME: indexing.py
# SPECIFICATION: This program reads a collection of documents from a CSV file, processes them by removing stopwords and applying stemming, identifies unique terms, and calculates the tf-idf weights for these terms across the documents. The program then prints the document-term matrix based on the tf-idf weights.
# FOR: CS 4250- Assignment #1
# TIME SPENT: 1.5hrs
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:        #ADJUSTED PATH TO WORK IN LOCAL ENVIRONMENT
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {'i','she','her','they','their','and'}

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {
    'cats': 'cat',
    'dogs': 'dog',
    'loves': 'love'
}

# Function to preprocess documents
def preprocess(doc):
    words = doc.lower().split()
    words = [word for word in words if word not in stopWords]
    words = [stemming.get(word, word) for word in words]
    return words

# Preprocessing documents
preprocessed_docs = [preprocess(doc) for doc in documents]

#Identifying the index terms.
#--> add your Python code here
terms = ['love', 'cat', 'dog']

# Calculating term frequency (tf)
def term_frequency(term, doc):
    term_count = doc.count(term)
    total_terms = len(doc)
    return term_count / total_terms if total_terms > 0 else 0

# Calculating document frequency (df)
def document_frequency(term, docs):
    return sum(1 for doc in docs if term in doc)

# Function to calculate logarithm base e manually
def ln(x):
    n = 100000.0  # large number for approximation
    return n * ((x ** (1/n)) - 1)

# Function to calculate log base 10 manually
def log10(x):
    return ln(x) / ln(10)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []
N = len(preprocessed_docs)
for doc in preprocessed_docs:
    doc_vector = []
    for term in terms:
        tf = term_frequency(term, doc)
        df = document_frequency(term, preprocessed_docs)
        idf = log10(N / df) if df != 0 else 0
        tfidf = tf * idf
        doc_vector.append(tfidf)
    docTermMatrix.append(doc_vector)

#Printing the document-term matrix.
#--> add your Python code here
print("Document-Term Matrix (tf-idf weights):")
print("Terms:", terms)
for i, doc_vector in enumerate(docTermMatrix):
    print(f"d{i + 1}: {doc_vector}")