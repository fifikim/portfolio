from django.shortcuts import render, get_object_or_404
from projects.models import Project

def home(request):
  projects = Project.objects.all()
  return render(request, 'projects/home.html', {'projects': projects})

def project_detail(request, pk):
  project = get_object_or_404(Project, pk=pk)
  return render(request, 'projects/project_detail.html', {'project': project})

