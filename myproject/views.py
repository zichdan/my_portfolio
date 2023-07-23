from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from myproject.models import *
import os
from django.http import HttpResponse, Http404

# Create your views here.

def projects(request):
    projects = Project.objects.all() # select * from projects
    
    category = Category.objects.all()  # select * from Category
    
    # proj_img1 = Project.objects.first()
    # if proj_img1:
    #     proj_img1 = proj_img1
    # else :
    #     None
        
    context = {
        "projects": projects,
        'category': category,
    }
    return render(request, 'projects.html', context)



def proj_details(request, pk):
    
    project = Project.objects.get(id=pk) # query projects one after another
    
    context = {"project": project}
    return render(request, "proj_details.html",context)


def download_cv(request):
    
    resumes = Resume.objects.all() # select * from resumes
    context = {
        "resumes": resumes
    }
    return render(request, "download_cv.html", context)



'''
RESUME SECTION
'''

def resume(request):
    resumes = Resume.objects.all() # select * from resumes
    context = {
        "resumes": resumes
    }
    return render(request, 'resume.html', context)



# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/resume")
#             response['content-Disposition'] = 'inline;filename'+os.path.basename(file_path)
#             return response
#     raise Http404
    
    
import mimetypes
from django.http import FileResponse

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = FileResponse(fh, content_type=mimetypes.guess_type(file_path)[0])
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    raise Http404

    
    