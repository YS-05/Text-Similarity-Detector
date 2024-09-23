This project defines a Python program that models and classifies text data based on various linguistic features. The core of the project is a TextModel class that analyzes a given text and creates a model based on word usage, sentence lengths, stems, and punctuation patterns. By comparing these features across different text samples, the program can classify new pieces of text and determine which of two sources they are more likely to come from.

Functions and Methods:

clean_text(txt): Processes input text by converting it to lowercase and removing punctuation, returning a list of words.
TextModel Class:
__init__(self, model_name): Initializes a TextModel with the name and 5 dictionaries to store words, word lengths, stems, sentence lengths, and punctuation.
__repr__(self): Provides a string representation of the TextModel.
add_string(self, s): Processes a string and updates the model's dictionaries.
add_file(self, filename): Reads a text file and processes its contents, updating the model.
save_model(self): Saves the model's dictionaries to files.
read_model(self): Reads and loads previously saved dictionaries into the TextModel.
similarity_scores(self, other): Compares the TextModel to another model and calculates similarity scores for each feature.
classify(self, source1, source2): Compares a TextModel with two other models and classifies it based on which model it is more similar to.
stem(s): Returns the stem of a word by removing common prefixes and suffixes.

compare_dictionaries(d1, d2): Computes a similarity score between two dictionaries based on logarithmic probability.

The project includes an example testing function run_tests() that demonstrates the classification of text between two famous authors: Stephen King and JK Rowling. By creating a model for a third text (Rick Riordan), the program classifies the text based on its similarity to the two authors' models.

The texts for each can also be found using this link:

Rick Riordan Sample Text Link: https://www.penguin.com.au/books/percy-jackson-and-the-lightning-thief-book-1-9780141346809/extracts/1881-percy-jackson-and-the-lightning-thief
Stephen King Sample Text Link: https://www.penguinrandomhouse.ca/books/92992/the-stand-by-stephen-king/9780307947307/excerpt
JK Rowling Sample Text Link: https://www.bookbrowse.com/excerpts/index.cfm/book_number/452/page_number/1/harry-potter-and-the-sorcerers-stone#excerpt

