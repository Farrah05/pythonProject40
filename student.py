from user import User

from essay import Essay


class Student(User):
    result = 0

    def type(self):

        student_essay = input("Hello,\n please type your essay here")

        self.calculate(student_essay)

    def calculate(self, student_essay):

        e1 = Essay()

        e1.sentence = len(student_essay.split(" . ")) - 1

        e1.word = len(student_essay.split(" "))

        self.result = e1.word/ e1.sentence

    def see(self):

        print("Average number of words:"+ str(self.result))
