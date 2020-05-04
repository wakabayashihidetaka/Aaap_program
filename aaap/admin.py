from django.contrib import admin

# Register your models here.
from .models import User
from .models import AssessmentAnswer
from .models import AssessmentOutput

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'created_datetime', 'updated_datetime')
    list_display_links = ('user_id', 'user_name')

admin.site.register(User, UserAdmin)

class AssessmentAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_id', 'user_id', 'question1_answer', 'question2_answer')
    list_display_links = ('answer_id', 'user_id')

admin.site.register(AssessmentAnswer, AssessmentAnswerAdmin)

class AssessmentOutputAdmin(admin.ModelAdmin):
    list_display = ('output_id', 'answer_name', 'tyoe1_id', 'type2_id')
    list_display_links = ('output_id', 'answer_name')

admin.site.register(AssessmentAnswer, AssessmentAnswerAdmin)