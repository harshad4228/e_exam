from django.db import models

# Create your models here.
class Course(models.Model):
    #course = models.PositiveIntegerField(max_length=9)
    courseName = models.CharField(max_length=20)
    isActive = models.BooleanField()
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'course'
        
class Question(models.Model):
    #questionid = models.PositiveIntegerField(max_length=9)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question =  models.CharField(max_length=500)
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)
    correctAns = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'question'
        
class Exam(models.Model):
    #examid = models.PositiveIntegerField(max_length=9)
    course = models.ForeignKey(Course,on_delete=models.CASCADE) #for key
    title = models.CharField(max_length=100) 
    description = models.CharField(max_length=250)
    marksPerQuestion = models.PositiveIntegerField()
    isActive = models.PositiveIntegerField()
    totalNumOfQuestion = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'exam'
        
class Exam_question(models.Model):
    #exam_question_id = models.PositiveIntegerField(max_length=9)
    examid = models.PositiveIntegerField()
    questionid = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'exam_question'
        

class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class User_exam(models.Model):
    #user_exam_id = models.PositiveIntegerField(max_length=9)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE) #below all change for key
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    obtainMarks = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'user_exam'

class User_exam_answers(models.Model):
    #user_exam_ans_id = models.PositiveIntegerField(max_length=9)
    user = models.ForeignKey(User,on_delete=models.CASCADE) #below change for key
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    User_exam = models.ForeignKey(User_exam,on_delete=models.CASCADE)
    answersansStatus = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'user_exam_answers'
  