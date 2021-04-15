import Preprocessor
import en_core_web_lg
import random


# Takes in the user input, as formated by the Preprocessor file, and analyzes the input to determine what the best response would be.

def preprocess(sentence):  # Uses functions in Preprocessor.py to format sentence, including accounting for spelling errors
    normalized_sentence = Preprocessor.sentence_normalizer(sentence)
    formatted_sentence = Preprocessor.sentence_formatter(normalized_sentence)  # remove punctuation
    lemmatized_sentence = Preprocessor.sentence_lemmatizer(formatted_sentence)  # lemmatize words
    cleaned_sentence = Preprocessor.sentence_cleaner(lemmatized_sentence)  # remove stopwords
    preprocessed_sentence = cleaned_sentence
    #print(preprocessed_sentence)
    return preprocessed_sentence


def vectorizer(question):  # Turns questions into a vectorized list
    question_list = []
    nlp = en_core_web_lg.load()
    for index in range(len(question)):
        vectorized_question = nlp(preprocess(question[index]))
        question_list.append(vectorized_question)
    return question_list


def process(sentence, doc_2, answer):  # Processes user input and outputs the correct response
    invalid_responses = ["I do not understand the question", "That question is not in my database", "I cannot answer "
                                                                                                    "that question",
                         "I am not familiar with that question", "I am sorry. Could you please ask another question?"]
    similarity_index = 0
    index = 0
    nlp = en_core_web_lg.load()
    doc_1 = nlp(preprocess(sentence))
    similarity = 0

    for i in range(len(doc_2)):
        if doc_2[i].vector_norm and doc_1.vector_norm:
            similarity = doc_1.similarity(doc_2[i])

        if similarity > similarity_index:
            similarity_index = similarity
            index = i
    if similarity_index > 0.60:
        return answer[index]

    else:
        return random.choice(invalid_responses)


