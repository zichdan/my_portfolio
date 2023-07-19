from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from myproject.models import *
import os
from django.http import HttpResponse, Http404

# Create your views here.



def portfolio(request):
    projects = Portfolio.objects.all() # select * from projects
    context = {
        "projects": projects
    }
    return render(request, 'portfolio.html', context)



def project_detail(request, project_id):
    projects = Portfolio.objects.get(pk=project_id) # query projects one after another
    
    context = {"projects": projects}
    return render(request, "project_detail.html",context)


'''
RESUME SECTION
'''

def resume(request):
    resumes = Resume.objects.all() # select * from resumes
    context = {
        "resumes": resumes
    }
    return render(request, 'resume.html', context)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/resume")
            response['content-Disposition'] = 'inline;filename'+os.path.basename(file_path)
            return response
    raise Http404
    