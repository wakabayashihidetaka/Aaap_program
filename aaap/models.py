from django.db import models

#Create your models here.

class User(models.Model):
    class Meta:
        db_table = 'user'
    user_id = models.IntegerField(blank=False, null=False, primary_key=True)
    user_name = models.CharField(blank=False, null=False, max_length=25)
    company_id = models.IntegerField(blank=False, null=False)
    department_id = models.IntegerField(blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    gender = models.IntegerField(blank=False, null=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

class AssessmentAnswer(models.Model):
    answer_id = models.IntegerField(blank=False, null=False, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    question1_answer = models.IntegerField(blank=False, null=False)
    question2_answer = models.IntegerField(blank=False, null=False)
    question3_answer = models.IntegerField(blank=False, null=False)
    question4_answer = models.IntegerField(blank=False, null=False)
    question5_answer = models.IntegerField(blank=False, null=False)
    question6_answer = models.IntegerField(blank=False, null=False)
    question7_answer = models.IntegerField(blank=False, null=False)
    question8_answer = models.IntegerField(blank=False, null=False)
    question9_answer = models.IntegerField(blank=False, null=False)
    question10_answer = models.IntegerField(blank=False, null=False)
    question11_answer = models.IntegerField(blank=False, null=False)
    question12_answer = models.IntegerField(blank=False, null=False)
    question13_answer = models.IntegerField(blank=False, null=False)
    question14_answer = models.IntegerField(blank=False, null=False)
    question15_answer = models.IntegerField(blank=False, null=False)
    question16_answer = models.IntegerField(blank=False, null=False)
    question17_answer = models.IntegerField(blank=False, null=False)
    question18_answer = models.IntegerField(blank=False, null=False)
    question19_answer = models.IntegerField(blank=False, null=False)
    question20_answer = models.IntegerField(blank=False, null=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer

class AssessmentOutput(models.Model):
    output_id = models.IntegerField(blank=False, null=False, primary_key=True)
    answer_id = models.ForeignKey(AssessmentAnswer, on_delete=models.PROTECT)
    type1_id = models.IntegerField(blank=False, null=False)
    type2_id = models.IntegerField(blank=False, null=False)
    type3_id = models.IntegerField(blank=False, null=False)
    type4_id = models.IntegerField(blank=False, null=False)
    type5_id = models.IntegerField(blank=False, null=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.output