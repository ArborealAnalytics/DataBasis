from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Question

@method_decorator(login_required, name='dispatch')
class QuestionsListView(ListView):
    model = Question
    context_object_name = "questions"

@method_decorator(login_required, name='dispatch')
class QuestionDetailView(DetailView):
    model = Question
    context_object_name = "question"

@method_decorator(login_required, name='dispatch')
class QuestionCreateView(CreateView):
    model = Question
    fields = ["title", "description", "keywords"]

@method_decorator(login_required, name='dispatch')
class QuestionUpdateView(UpdateView):
    model = Question
    fields = ["title", "description", "keywords"]

@method_decorator(staff_member_required, name='dispatch')
class QuestionDeleteView(DeleteView):
    model = Question
    context_object_name = "question"
    success_url = reverse_lazy("questions_index")
