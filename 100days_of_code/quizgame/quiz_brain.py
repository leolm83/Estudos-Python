class QuizBrain:
    def __init__(self,questions_list):
        self.question_number=0
        self.questions_list=questions_list
    
    def nextQuestion(self):
        if self.question_number<len(self.questions_list):
            self.question_number+=1
            return self.question_number
        else :
            return self.question_number
    def getQuestion(self):
        return self.questions_list[self.question_number]
    
    def getQuestionNumber(self):
        return self.question_number

