from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Zahra Nayla",
        "npm": "2506534163",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS student at Universitas Indonesia who keeps thinking when the next holiday will come."
            "Have wide interest from robotic to geography." 
            "Currently looking for future career prospects that match my interests."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Zahra Nayla",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)