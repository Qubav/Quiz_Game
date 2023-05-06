class QuizBrain:

    def __init__(self, question_list: list) -> None:  
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        """Method shows user current question and ask for True or False answer. Object attribute question_number is increased by 1 
        and based on the correctness of the answer object attribute score can be increased by 1."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self) -> bool:
        """Method returns True if there are questions in objects attribute question list that were not answered yet, or False if all question were answered by user."""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: str):
        """Method compares user answer with correct answer to question and based on if they are the same user can get +1 score. 
        Method also gives user feedback whether answer was correct or not and show users current score."""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.\nYour current score is {self.score}/{self.question_number}.")
