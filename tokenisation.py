#Zero Shot Classification is the task of predicting a class that wasn't seen by the model during training. 
#This method, which leverages a pre-trained language model, can be thought of as an 
#instance of transfer learning which generally refers to using a model trained for 
#one task in a different application than what it was originally trained for. 
#This is particularly useful for situations where the amount of labeled data is small.

from transformers import pipeline

major_labels = []
with open("degrees_majors.txt") as file:
    for line in file:
        major_labels.append(line.rstrip())
print(major_labels)

# Load a zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")

# Example input and candidate classes
user_input = "Biology"
candidate_labels = major_labels

# Perform zero-shot classification
result = classifier(user_input, candidate_labels)
print(result['labels'][0])

