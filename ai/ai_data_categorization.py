import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import numpy as np

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample categorized dataset (to be expanded with real data)
data = [
    ("Quantum mechanics explores the behavior of particles at a subatomic level.", "Science"),
    ("The Renaissance was a period of great cultural and artistic achievement.", "History"),
    ("Artificial Intelligence is transforming industries worldwide.", "Technology"),
    ("The theory of relativity changed our understanding of space and time.", "Science"),
    ("Philosophy seeks to understand the fundamental nature of reality and existence.", "Philosophy")
]

# Prepare training data
texts, labels = zip(*data)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(labels)

# Train classification model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(texts, y)

def categorize_text(text):
    prediction = model.predict([text])[0]
    return prediction

# Example usage
sample_text = "Neural networks are a subset of machine learning techniques."
print(f"Category: {categorize_text(sample_text)}")
