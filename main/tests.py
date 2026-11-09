from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            started_at=timezone.localdate(),
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        data = self.client.get(reverse("main:get_experience_json")).json()
        self.assertEqual(data[0]["fields"]["title"], self.experience.title)
        self.assertEqual(data[0]["fields"]["description"], self.experience.description)
        self.assertEqual(data[0]["fields"]["category_display"], "Part-Time")
        self.assertTrue(data[0]["fields"]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertEqual(response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertFalse(self.experience.is_ongoing)
        data = response.json()
        self.assertEqual(data[0]["fields"]["is_ongoing"], False)

class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title = "Tugas 2",
            description = "Membuat halaman baru dengan MVT concept",
            technology = "Python, Django, HTML"
        )

    def test_project_model(self):
        self.assertEqual(str(self.project), "Tugas 2")
        self.assertEqual(self.project.technology, "Python, Django, HTML")

    def test_project_url_and_template(self):
        response = self.client.get(reverse("main:show_project"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")

    def test_project_page_shows_data(self):
        response = self.client.get(reverse("main:show_project"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        data = self.client.get(reverse("main:get_project_json")).json()
        self.assertEqual(data[0]["fields"]["title"], self.project.title)
        self.assertEqual(data[0]["fields"]["description"], self.project.description)

    def test_project_page(self):
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        data = self.client.get(reverse("api:project-list")).json()
        self.assertEqual(data[0]["title"], self.project.title)
        self.assertEqual(data[0]["description"], self.project.description)

    def test_empty_experience_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:get_project_json"))

        self.assertEqual(response.json(), [])