from django.db import models
import random


# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.

class student(models.Model):
    sid=models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password=models.CharField(max_length=20,null=True)
   # desc = models.TextField()
    date = models.DateField()

    def str(self):
        return self.name


class quiz_topic(models.Model):
    qid=models.IntegerField(primary_key=True)  #qid-->quizid
    topic=models.CharField(max_length=50)

    def str(self):
        return self.topic

class questions(models.Model):
    qid=models.ForeignKey(quiz_topic,related_name='category',on_delete=models.CASCADE)
    qno=models.CharField(max_length=10,primary_key=True)
    question=models.TextField()
    difficulty_level=models.CharField(max_length=10)

    def str(self):
        return self.qid +self.qno +self.difficulty_level

    def get_answers(self):
        answer_objs= list(answers.objects.filter(qno=self))
        random.shuffle(answer_objs)
        data=[]
        for answer_obj in answer_objs:
            data.append({
                'answer':answer_obj.answer,
                'is_correct':answer_obj.is_correct
            })
        return data


class answers(models.Model):
    uid=models.AutoField(primary_key=True)
    qno=models.ForeignKey(questions,related_name='question_answer',on_delete=models.CASCADE)
    answer=models.CharField(max_length=10)
    is_correct=models.BooleanField(default=False)

class feedback(models.Model):
    fid=models.AutoField(primary_key=True)
    #sid=models.ForeignKey(student,on_delete=models.CASCADE)
    feedback=models.TextField()