import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
with open('intents.json', encoding="utf-8") as f:
    intents = json.load(f)
patterns = []
tags = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern.lower())
        tags.append(intent['tag'])
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)
model = MultinomialNB()
model.fit(X, tags)
print("Model trained successfully!")
def get_bot_response(message):
    X_test = vectorizer.transform([message.lower()])
    proba = model.predict_proba(X_test)[0]
    max_index = proba.argmax()
    confidence = proba[max_index]
    predicted_tag = model.classes_[max_index]
    if confidence < 0.1:
        for intent in intents['intents']:
            if intent['tag'] == "fallback":
                return random.choice(intent['responses'])
    for intent in intents['intents']:
        if intent['tag'] == predicted_tag:
            return random.choice(intent['responses'])
    return "Sorry, I didn’t understand that."
