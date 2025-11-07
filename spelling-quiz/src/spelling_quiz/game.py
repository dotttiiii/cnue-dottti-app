class SpellingQuiz:
    def __init__(self, words):
        self.words = words
        self.score = 0
        self.current_question = 0

    def start_game(self):
        print("Welcome to the Spelling Quiz!")
        print("You will be asked to spell a series of words.")
        print("Type 'exit' to quit the game at any time.")
        self.ask_questions()

    def ask_questions(self):
        while self.current_question < len(self.words):
            word = self.words[self.current_question]
            answer = input(f"Spell the word: {word} ")

            if answer.lower() == 'exit':
                print("Thanks for playing!")
                break

            self.check_answer(answer, word)

    def check_answer(self, answer, word):
        if answer.lower() == word.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect! The correct spelling is: {word}")
        
        self.current_question += 1

    def get_score(self):
        return self.score

    def reset_game(self):
        self.score = 0
        self.current_question = 0