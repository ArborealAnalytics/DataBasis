from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Query

@method_decorator(login_required, name='dispatch')
class QueriesListView(ListView):
    model = Query
    context_object_name = "queries"

@method_decorator(login_required, name='dispatch')
class QueryDetailView(DetailView):
    model = Query
    context_object_name = "query"

@method_decorator(login_required, name='dispatch')
class QueryCreateView(CreateView):
    model = Query
    fields = ["title", "description", "keywords", "sql"]

@method_decorator(login_required, name='dispatch')
class QueryUpdateView(UpdateView):
    model = Query
    fields = ["title", "description", "keywords", "sql"]

@method_decorator(staff_member_required, name='dispatch')
class QueryDeleteView(DeleteView):
    model = Query
    context_object_name = "query"
    success_url = reverse_lazy("queries_index")
