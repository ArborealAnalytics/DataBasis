from django.urls import path

from .views import (
    QuestionCreateView,
    QuestionDeleteView,
    QuestionDetailView,
    QuestionsListView,
    QuestionUpdateView,
)

urlpatterns = [
    path("add/", QuestionCreateView.as_view(), name="question_create"),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question_detail"),
    path("<int:pk>/update/", QuestionUpdateView.as_view(), name="question_update"),
    path("<int:pk>/delete/", QuestionDeleteView.as_view(), name="question_delete"),
    path("", QuestionsListView.as_view(), name="questions_index"),
]