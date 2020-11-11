from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Question


class QuestionsListView(ListView):
    model = Question
    context_object_name = "questions"

class QuestionDetailView(DetailView):
    model = Question
    context_object_name = "question"

class QuestionCreateView(CreateView):
    model = Question
    fields = ["title", "description", "keywords"]


class QuestionUpdateView(UpdateView):
    model = Question
    fields = ["title", "description", "keywords"]


class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy("questions_index")