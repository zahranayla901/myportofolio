from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm, ExperienceForm
from main.models import Experience, Project


def show_main(request):
    context = {
        "name": "Zahra Nayla",
        "npm": "2506534163",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS student at Universitas Indonesia who keeps thinking when the next holiday will come."
            " Have wide interest from robotic to geography." 
            " Currently looking for future career prospects that match my interests."
        ),
    }
    return render(request, "index.html", context)

def show_project(request):
    json_response = get_project_json(request)

    project = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    project = [project.object for project in project]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Zahra Nayla",
        "project_list": project,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "A new project has been successfully added!")
        return redirect("main:show_project")

    context = {
        "name": "Zahra Nayla",
        "form": form,
    }
    return render(request, "project_form.html", context)

def get_project_json(request):
    title_query = request.GET.get("title", "").strip()
    project = Project.objects.all()

    if title_query:
        project = project.filter(title__icontains=title_query)

    project_json = serializers.serialize("json", project)
    return HttpResponse(project_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_project")

    return redirect("main:show_project")

# experience section
def show_experience(request):
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience = [experience.object for experience in experience]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Zahra Nayla",
        "experience_list": experience,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

# func to create new experience (C from CRUD)
def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "A new experience has been successfully added!")
        return redirect("main:show_experience")

    context = {
        "name": "Zahra Nayla",
        "form": form,
    }
    return render(request, "experience_form.html", context)

# func to get certain experience by search feature (R from CRUD)
def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

# func to delete existing experience from db (D from CRUD)
def delete_Experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")