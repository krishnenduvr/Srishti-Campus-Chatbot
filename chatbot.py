import json
import random
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

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


def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def get_intent_by_tag(tag):
    for intent in a['intents']:
        if intent['tag'] == tag:
            return intent
    return None


def match_intent_directly(message):
    normalized_message = normalize_text(message)
    compact_message = normalized_message.replace(" ", "")

    greeting_aliases = {"hlo", "helo", "helloo", "hy", "hii"}
    if normalized_message in greeting_aliases:
        return get_intent_by_tag("greeting")

    for intent in a['intents']:
        for pattern in intent['patterns']:
            normalized_pattern = normalize_text(pattern)
            compact_pattern = normalized_pattern.replace(" ", "")

            if normalized_message == normalized_pattern:
                return intent

            if normalized_message and normalized_message in normalized_pattern:
                return intent

            if compact_message and compact_message == compact_pattern:
                return intent

    return None


def get_response(message):
    direct_intent = match_intent_directly(message)
    if direct_intent is not None:
        return random.choice(direct_intent['responses'])

    normalized_message = normalize_text(message)
    X_test = d.transform([normalized_message])
    predicted_tag = model.predict(X_test)[0]
    confidence = max(model.predict_proba(X_test)[0])

    if confidence < 0.2:
        fallback_intent = get_intent_by_tag("fallback")
        if fallback_intent is not None:
            return random.choice(fallback_intent['responses'])

    predicted_intent = get_intent_by_tag(predicted_tag)
    if predicted_intent is not None:
        return random.choice(predicted_intent['responses'])

    return "I'm sorry, I didn't understand that. Could you please rephrase?"


def chat(message):
    return {"response": get_response(message)}


if __name__ == '__main__':
    while True:
        user_message = input("You: ").strip()
        if user_message.lower() in {"exit", "quit"}:
            print("Bot: Goodbye! Have a great day!")
            break
        print(f"Bot: {get_response(user_message)}")
