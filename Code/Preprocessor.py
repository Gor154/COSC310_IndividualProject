import string
from spellchecker import SpellChecker
import norm_punc #this imports from our norm_punc file
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')


# Preprocessor has functions to load the corpus questions and responses, as well as to format the user input so it can be used by the Processor file.

def load_corpus():  # Loads questions and responses from corpus.txt
    questions = []
    responses = []
    with open('Corpus.txt') as corpus:  # open corpus.txt
        for line in corpus.readlines():
            split = line.split("||")  # split lines into questions and responses then add to respective list
            questions.append(split[0])
            responses.append(split[1])
    return questions, responses

#our application of phrasal, we used the normalizer function from phrasal.
def sentence_normalizer(sentence):
    standard_char_list = "abcdefghijklmnopqrstuvwsyz- "
    temp_sentence = ""
    normalized_sentence = norm_punc.normalize_text(str(sentence.lower()),fix_encoding=True,strip_emojis=True)
    for char in normalized_sentence:
        for standardChar in standard_char_list:
            if standardChar == char:
                temp_sentence += char
                break
    return temp_sentence


def sentence_formatter(sentence):  # Removes punctuation from sentence
    formatted_sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    formatted_sentence = formatted_sentence.lower()
    return formatted_sentence


def sentence_lemmatizer(sentence):  # Changes words in the sentence to their root form
    lemmatized_word_bank = []
    lemmatizer = WordNetLemmatizer()
    split = sentence.split()
    for word in split:
        lemmatized_word_bank.append(lemmatizer.lemmatize(word))  # add lemmatized words to list
    lemmatized_sentence = ' '.join(lemmatized_word_bank)  # rejoin words into a sentence format
    print(lemmatized_sentence)
    return lemmatized_sentence


def sentence_cleaner(sentence):  # Removes stop words such as 'the', 'a' and 'in' from sentence
    tokens = word_tokenize(sentence)
    cleaned_tokens = [word for word in tokens if not word in stopwords.words()]  # Only add words that are not stopwords
    cleaned_tokens = token_spellchecker(cleaned_tokens)
    token_postagging(cleaned_tokens)
    cleaned_sentence = ' '.join(cleaned_tokens)  # rejoin words into sentence format
    return cleaned_sentence

#spell checking application to correct minor errors
def token_spellchecker(tokens):
    spell = SpellChecker()
    correct_spelling = [spell.correction(word) for word in tokens]
    return correct_spelling


def token_postagging(tokens):
    print("Parts of Speech: ", nltk.pos_tag(tokens))
    return nltk.pos_tag(tokens)