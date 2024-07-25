import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB


data = pd.read_csv('MovieReviews.csv')

x = data['review']
y = data['sentiment']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=50)

vectorizer = CountVectorizer()

X_train_vectorized = vectorizer.fit_transform(x_train)

X_test_vectorized = vectorizer.transform(x_test)

model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

y_pred = model.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, y_pred)
print(f"accuracy:{accuracy:.2f}")

print("\nclassification report:")
print(classification_report(y_test, y_pred))

def predict_sentiment(review):
    vectorized_review = vectorizer.transform([review])
    prediction = model.predict(vectorized_review)
    return "positive" if prediction[0] == 1 else "negative"

new_review =[
    "above average",
    "Terrible film, wosrt experience",
    "Not too good and not too bad either",
]

for review in new_review:
    print(f"review:{review}")
    print(f"predicted sentiment:{predict_sentiment(review)}\n")

print("now you can enter your own reviews")
while True:
    user_review = input("enter your (or say quit to stop):")
    if user_review.lower()== "quit":
        break
    print(f"predicted sentiment:{predict_sentiment(user_review)}\n")
print("thanks guys")







