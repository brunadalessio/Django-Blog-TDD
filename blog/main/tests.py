from django.test import TestCase
from .models import Postagem
from http import HTTPStatus

class PostModelTest(TestCase):
    def test_model_exists(self):
        posts = Postagem.objects.count()
        self.assertEqual(posts, 0)

    def test_string_representation(self):
        post = Postagem.objects.create(
            titulo = "Teste Titulo",
            conteudo = "Teste Conteúdo"
        )
        self.assertEqual(str(post), post.titulo)


class HomePageTest(TestCase):
    def setUp(self):
        Postagem.objects.create(
            titulo = "Titulo Teste da Primeira Postagem",
            conteudo = "Lorem ipsum dolor sit amet."
        )

        Postagem.objects.create(
            titulo = "Titulo Teste da Segunda Postagem",
            conteudo = "At repellendus deleniti et."
        )

    def test_homepage_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'main/home.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_post_list(self):
        response = self.client.get('/')

        primeiro_post = Postagem.objects.get(titulo="Titulo Teste da Primeira Postagem")
        segundo_post = Postagem.objects.get(titulo="Titulo Teste da Segunda Postagem")

        self.assertContains(response, primeiro_post)
        self.assertContains(response, segundo_post)