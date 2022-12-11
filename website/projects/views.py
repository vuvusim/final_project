from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import searchProjects, paginateProjects
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm


def projects(request):
    projects, search_text = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 3)
    context = {'projects': projects, 'search_text': search_text, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm() # label does not apply, need checking (ReviewForm, and single-project.html <form></form>)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount

        messages.success(request, 'Your review was successfuly submitted')
        return redirect('project', pk=projectObj.id)

    return render(request, 'projects/single-project.html', {'project': projectObj, 'form': form})

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    context = {'object': project}

    if request.method == 'POST':
        project.delete()
        return redirect('account')
    
    return render(request, 'projects/delete_template.html', context)