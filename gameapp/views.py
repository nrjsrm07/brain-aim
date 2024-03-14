# views.py

from django.shortcuts import render
from django.contrib import messages
from .forms import AddingQuestion
from .models import Questions
import random


def randomQuestionFromDB(level, truth):
    # Query for fetching a random question based on level and truth
    questions = Questions.objects.filter(level=level, truth_dare=truth)
    # Check if there are any questions matching the criteria
    if questions:
        # Select a random question from the queryset
        random_question = random.choice(questions)
        return random_question.question
    else:
        return "No question found for the given level and truth"

# Create your views here.
def home_view(request):
    return render(request, 'gameapp/welcome_page.html')

def question_view(request):
    return render(request, 'gameapp/question_page.html')

def add_question_view(request):
    return render(request, 'gameapp/add_question.html')

def add_question(request):
    form = AddingQuestion(request.POST)
    if form.is_valid():
        form.save()
    context= {'form': form }
    messages.info(request,'Congratulations!! Question has been added successfully...')
    return render(request, 'gameapp/added_question.html', context)

def truth_dare_view(request):
    if request.method == 'POST':
        level = request.POST['level']
        truth = request.POST['truth_dare']
        truth = truth.lower()
        question = randomQuestionFromDB(level, truth)
        messages.info(request, question)
        dataValues = {'level':level,'type':truth }
        return render(request, 'gameapp/question.html',dataValues) 
