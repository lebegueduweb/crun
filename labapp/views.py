from django.shortcuts import render
from .models import Examen, Archivage
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django. urls import reverse
import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView

def examen_view(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_examens = Examen.objects.all().count()
    num_archivages = Archivage.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'examen_view.html',
        context={'num_examens': num_examens, 
                 'num_archivages': num_archivages
                 },
    )
class ExamenListView(generic.ListView):
    model = Examen
    paginate_by = 10
class ExamenDetailView(generic.DetailView):
    model = Examen
class ArchivageListView(generic.ListView):
    model = Archivage
    paginate_by = 10

class ArchivageDetailView(generic.DetailView):
    model = Archivage
class ExamenCreate(CreateView):
    model = Examen
    fields = '__all__'
    initial={'Id_projet':'NA00',}
class ArchivageCreate(CreateView):
    model = Archivage
    fields = '__all__'


