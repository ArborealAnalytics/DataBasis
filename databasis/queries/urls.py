from django.urls import path

from .views import (
    QueryCreateView,
    QueryDeleteView,
    QueryDetailView,
    QueriesListView,
    QueryUpdateView,
)

urlpatterns = [
    path("add/", QueryCreateView.as_view(), name="query_create"),
    path("<int:pk>/", QueryDetailView.as_view(), name="query_detail"),
    path("<int:pk>/update/", QueryUpdateView.as_view(), name="query_update"),
    path("<int:pk>/delete/", QueryDeleteView.as_view(), name="query_delete"),
    path("", QueriesListView.as_view(), name="queries_index"),
]