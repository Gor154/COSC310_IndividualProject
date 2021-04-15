import Preprocessor
import Processor
import norm_punc
import sys, os


import unittest

class TestingPOSTagging(unittest.TestCase):
    #an example of a noun
    def test_POS1(self):
        self.assertEqual(Preprocessor.token_postagging(["Star"]), [('Star', 'NN')])
    #an example of a verb
    def test_POS2(self):
        self.assertEqual(Preprocessor.token_postagging(["Go"]), [('Go', 'VB')])
    #an example of an adjective
    def test_POS3(self):
        self.assertEqual(Preprocessor.token_postagging(["Big"]), [('Big', 'JJ')])

class TestingSpellingCorrection(unittest.TestCase):
    #an example of an extra letter
    def test_Spelling1(self):
        self.assertEqual(Preprocessor.token_spellchecker(["capitall"]), ['capital'])
    #an example of a missing letter
    def test_Spelling2(self):
        self.assertEqual(Preprocessor.token_spellchecker(["rusia"]), ['russia'])
    #an example of writing a wrong letter
    def test_Spelling3(self):
        self.assertEqual(Preprocessor.token_spellchecker(["quazar"]), ['quasar'])

class TestingResponses(unittest.TestCase):
    def test_Response(self):
        questions, responses = Preprocessor.load_corpus()
        question_list = Processor.vectorizer(questions)
        self.assertEqual(Processor.process("what is a star?",question_list, responses), "Stars are mostly made of hydrogen and helium\n" )
        self.assertEqual(Processor.process("Hello",question_list, responses), "Hello! I am Nova.\n" )
        self.assertEqual(Processor.process("What is your job?",question_list, responses), "I teach you about astronomy and geography!\n" )


if __name__ == '__main__':
    unittest.main()