# Text Similarity Detection

## Table of Contents
Introduction
Features
How It Works
Usage
Classes and Methods
Demo Example
Future Improvements
License

## Introduction

This project demonstrates a basic text classification model using the TextModel class. The program analyzes and compares text files based on various linguistic features like word frequency, word length, sentence length, punctuation use, and word stems. This is useful for author identification, content categorization, or stylistic comparison between different bodies of text.

The model compares an unknown text against two known texts, calculating a similarity score based on statistical analysis of linguistic patterns. The final result shows which source the unknown text is more likely to have originated from.

## Features
Text Cleaning: Cleans text by removing punctuation and converting to lowercase.
Linguistic Features: Analyzes word frequency, word length distribution, sentence length, punctuation, and stems.
Model Saving and Loading: Saves and loads models to/from files, allowing reuse without recomputation.
Text Comparison: Compares text models based on their linguistic features and returns similarity scores.
Classification: Classifies an unknown text by comparing it against two known sources.

## How It Works

The TextModel class processes a given text by:

Breaking the text into individual words and sentences.
Cleaning the words by removing punctuation and converting them to lowercase.
Collecting information such as:
Frequency of words
Word length distribution
Stemming patterns (basic root word extraction)
Sentence length
Use of punctuation
The text model then compares the collected information with other text models, calculating a similarity score for each feature.

## Usage

Define a Text Model: Create a TextModel object for the text you want to analyze.
Add Text: You can add text either by calling add_string (for a string) or add_file (for a file).
Save the Model: Save the model's data to files using save_model.
Load a Model: Load a previously saved model using read_model.
Compare Models: Use the classify method to compare models and classify unknown text based on two sources.

An example will be shown in the demo section as well.

## Classes and Methods

TextModel Class
Represents a model of a text. It contains various dictionaries that store linguistic data about the text.

__init__(self, model_name): Initializes the text model.
__repr__(self): Returns a string representation of the model.
add_string(self, s): Analyzes a string and adds it to the model.
add_file(self, filename): Reads and analyzes a text file, adding the data to the model.
save_model(self): Saves the model’s data to files.
read_model(self): Reads the saved model data from files.
similarity_scores(self, other): Compares the current model with another and returns a list of similarity scores.
classify(self, source1, source2): Classifies an unknown text by comparing it with two known sources.

Helper Functions
clean_text(txt): Cleans the text by removing punctuation and converting it to lowercase.
stem(s): Reduces words to their stems by removing common suffixes and prefixes.
compare_dictionaries(d1, d2): Compares two dictionaries using a logarithmic scoring system to calculate similarity.

stem(s) Function
This function is used to reduce words to their stems by removing common suffixes and prefixes. For example, "running" would become "run," and "quickly" would become "quick."

## Demo Example

First, you want to get our 3 text files in the .txt format and in the same folder as the classification code. Then, replace the text names with the ones you have saved them as. Then we can simply do this:

<img width="586" alt="image" src="https://github.com/user-attachments/assets/87e99952-4cea-4ef8-98ea-845aa2a95d33">


## Further Improvements

Using more sophisticated classifiers to classify the meanings of the texts, too, other than just exact words and structures.
Perhaps leveraging LLMs and transformer models to perform these tasks with higher accuracy and reliability.

## License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
