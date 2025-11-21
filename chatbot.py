import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from flask import Flask, request, jsonify
with open('intents.json') as f:
    a = json.load(f)
print(f"Intents file loaded successfully with {len(a['intents'])} categories!")
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
app = Flask(__name__)
@app.route('/chat', methods=['POST'])
def chat():
    p = request.json['message']
    X_test = d.transform([p.lower()])
    predicted_tag = model.predict(X_test)[0]
    confidence = max(model.predict_proba(X_test)[0])
    if confidence < 0.1:
        for intent in a['intents']:
            if intent['tag'] == "fallback":
                response = random.choice(intent['responses'])
                break
    else:
        for intent in a['intents']:
            if intent['tag'] == predicted_tag:
                response = random.choice(intent['responses'])
                break

    return jsonify({"response": response})
if __name__ == '__main__':
    app.run(debug=True)

