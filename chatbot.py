import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
with open('intents.json') as f:
    a = json.load(f)
b = []
c = []
for intent in a['intents']:
    for pattern in intent['patterns']:
        b.append(pattern.lower())
        c.append(intent['tag'])
d = CountVectorizer()
e = d.fit_transform(b)
model = MultinomialNB()
model.fit(e, c)
print(f"Model trained successfully with {len(a['intents'])} categories!")
def get_bot_response(message):
    X_test = d.transform([message.lower()])
    predicted_tag = model.predict(X_test)[0]
    confidence = max(model.predict_proba(X_test)[0])

    if confidence < 0.1:
        for intent in a['intents']:
            if intent['tag'] == "fallback":
                return random.choice(intent['responses'])
    else:
        for intent in a['intents']:
            if intent['tag'] == predicted_tag:
                return random.choice(intent['responses'])


