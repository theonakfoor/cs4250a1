#-------------------------------------------------------------------------
# AUTHOR: Theo Nakfoor
# FILENAME: indexing.py
# SPECIFICATION: A program to take a list of documents, perform tf-idf calcualations and print the results in a pretty matrix.
# FOR: CS 4250- Assignment #1
# TIME SPENT: 1h 30m
#-----------------------------------------------------------*/

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0].lower())

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
stopWords = {"their", "and", "she", "they", "i"}

for idx, d in enumerate(documents):
    temp = []
    for term in d.split(" "):
        if term not in stopWords:
            temp.append(term)
    documents[idx] = " ".join(temp)

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
stemming = {
    "love": ["love", "loves"],
    "cat": ["cat", "cats"],
    "dog": ["dog", "dogs"]
}

for idx, d in enumerate(documents):
    temp = []
    for term in d.split(" "):
        for stem, variations in stemming.items():
            if term in variations:
                temp.append(stem)
    documents[idx] = " ".join(temp)

#Identifying the index terms.
terms = []
for doc in documents:
    for term in doc.split(" "):
        if term not in terms:
            terms.append(term)

docTermMatrix = {}

for term in terms:
    for doc in documents:
        tf = doc.count(term) / len(doc.split(" "))
        
        df = 0
        for d in documents:
            if term in d:
                df += 1

        idf = math.log(len(documents)/df, 10)

        tfidf = round(tf * idf, 2)

        if term in docTermMatrix:
            docTermMatrix[term].append(tfidf)
        else:
            docTermMatrix[term] = []
            docTermMatrix[term].append(tfidf)

print("DocTerm Matrix\t" + "\t".join(terms))
for idx, doc in enumerate(documents):
    vals = ""
    for term in terms:
        vals += str(docTermMatrix[term][idx]) + "\t"
    print(f"Document {idx+1}" + "\t" + vals)


