import unittest
from src.spelling_quiz.game import SpellingQuiz

class TestSpellingQuiz(unittest.TestCase):

    def setUp(self):
        self.quiz = SpellingQuiz()

    def test_start_game(self):
        self.quiz.start_game()
        self.assertTrue(self.quiz.is_running)

    def test_ask_question(self):
        question = self.quiz.ask_question()
        self.assertIn(question, self.quiz.words)

    def test_check_answer_correct(self):
        self.quiz.current_word = "example"
        result = self.quiz.check_answer("example")
        self.assertTrue(result)

    def test_check_answer_incorrect(self):
        self.quiz.current_word = "example"
        result = self.quiz.check_answer("wrong")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()