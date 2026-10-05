from django import forms
from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Project, Experience
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "technology",
            "project_url",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "technology": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "thumbnail": "Path Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "technology": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/zahranayla901/myportofolio",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=FILE_ID&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["technology"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Experience Title",
            "description": "Description",
            "category": "Choose Category",
            "thumbnail": "Exp Image Path",
            "started_at": "Started at",
            "ended_at": "Ended at",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "COMPFEST 18 Creative Staff",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "I Sketch",
                    "rows": 3,
                }
            ),
            "category": forms.Select(
                choices=Experience.EXPERIENCE_CHOICES,
            ),
            "thumbnail": TextInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=FILE_ID&sz=w1000",
                }
            ),
            "started_at": forms.DateInput(
                attrs={"type": "date"}, format="%y-%m-%d"
            ),
            
            "ended_at": forms.DateInput(
                attrs={"type": "date"}, format="%y-%m-%d"
            ),
        }

    def clean_title(self):
            title = strip_tags(self.cleaned_data["title"]).strip()
            if not title:
                raise ValidationError("Nama experience tidak boleh hanya berisi tag HTML.")
            return title
    
    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()