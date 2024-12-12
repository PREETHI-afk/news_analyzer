import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# Example data (for demonstration only)
texts = [
    "Fake news!", 
    "Vaccines are safe.", 
    "Aliens landed!", 
    "Earth is flat.",
    "Vaccines are safe and effective.",
    "Breaking: Scientists discover a new cure for cancer!",
    "Aliens have landed on Earth.",
    "Climate change is a hoax according to some sources.",
    
]

labels = ["fake", "real", "fake", "fake", "real", "real", "fake", "fake"]
# Convert text data to numerical using TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train a simple Naive Bayes model
model = MultinomialNB()
model.fit(X, labels)

# Save model and vectorizer
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved!")