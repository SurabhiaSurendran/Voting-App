from django.contrib import admin
# Register your models here.
from .models import Question, Choice
 
admin.site.site_header = "Voting Admin"
admin.site.site_title = "Voting Admin Area"
admin.site.index_title = "Welcome to the Voting Admin Area"
 
 
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3 # to add the option column in admin panel default number will as in extra field
 
 
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question', {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date']}), ]
    inlines = [ChoiceInLine]
    
admin.site.register(Question, QuestionAdmin)
