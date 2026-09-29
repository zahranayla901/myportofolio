from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import datetime
from main.forms import *
from main.models import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import *
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def user_is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Zahra Nayla",
        "npm": "2506534163",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS student at Universitas Indonesia who keeps thinking when the next holiday will come."
            " Have wide interest from robotic to geography." 
            " Currently looking for future career prospects that match my interests."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_project(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Zahra Nayla",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

def get_project_json(request):
    title_query = request.GET.get("title", "").strip()
    project = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        project = project.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for p in project:
        starred_users = p.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(p.id),
            "fields": {
                "title": p.title,
                "description": p.description,
                "tech_stack": p.technology,
                "project_url": p.project_url,
                "project_thumbnail": p.thumbnail,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

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
        "is_editor": user_is_editor(request.user),
    }
    return render(request, "experience.html", context)

# func to create new experience (C from CRUD)
# login required to create, Edit, and Delete
@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser: # Only superuser can create and delete
        raise PermissionDenied
    
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

    experience_json = serializers.serialize(
        "json", experience, use_natural_foreign_keys=True
    )
    return HttpResponse(experience_json, content_type="application/json")

# func to edit existing experience (U from CRUD)
# editor can edit experience
@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not (request.user.is_superuser or user_is_editor(request.user)):
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
 
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience successfully updated!")
        return redirect("main:show_experience")
 
    context = {
        "name": "Zahra Nayla",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

# func to delete existing experience from db (D from CRUD)
@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account has been created. Please Log in.")
        return redirect("main:login")

    context = {
        "name": "Zahra Nayla",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Zahra Nayla",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")

# toggle star untuk page experience, di restrict dengan login
@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")