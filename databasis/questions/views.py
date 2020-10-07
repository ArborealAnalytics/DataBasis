from django.shortcuts import render
from django.views.generic import ListView

from .models import Question

class QuestionsListView(ListView):
    model = Question
    context_object_name = "questions"
