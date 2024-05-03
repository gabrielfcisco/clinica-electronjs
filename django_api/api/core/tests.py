from django.test import TestCase
from core.models import Aluno, Professor, Curso, Materia
from django.urls import reverse

class AlunoTestCase(TestCase):
    def setUp(self):
        self.aluno = Aluno.objects.create(nome="Gabriel Sousa", idade=19)

    def testAluno(self):
        self.assertEqual(self.aluno.nome, "Gabriel Sousa")
        self.assertEqual(self.aluno.idade, 19)

    def testAlunoGet(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def testAlunoCreate(self):
        data = {"nome": self.aluno.nome, "idade": self.aluno.idade}
        response = self.client.post(reverse('salvar_aluno'), data)
        self.assertRedirects(response, reverse('home'))

    def testAlunoEdit(self):
        response = self.client.get(reverse('editar_aluno', args=[self.aluno.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['aluno'], self.aluno)

    def testAlunoDelete(self):
        response = self.client.post(reverse('delete_aluno', args=[self.aluno.pk]))
        self.assertFalse(Aluno.objects.filter(pk=self.aluno.pk).exists())
        self.assertRedirects(response, reverse('home'))

class ProfessorTestCase(TestCase):
    def setUp(self):
        self.professor = Professor.objects.create(nome="Leonardo Simões", idade=35)

    def testProfessor(self):
        self.assertEqual(self.professor.nome, "Leonardo Simões")
        self.assertEqual(self.professor.idade, 35)

    def testProfessorGet(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def testProfessorCreate(self):
        data = {"nome": self.professor.nome, "idade": self.professor.idade}
        response = self.client.post(reverse('salvar_professor'), data)
        self.assertRedirects(response, reverse('home'))

    def testProfessorEdit(self):
        response = self.client.get(reverse('editar_professor', args=[self.professor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['professor'], self.professor)

    def testProfessorDelete(self):
        response = self.client.post(reverse('delete_professor', args=[self.professor.pk]))
        self.assertFalse(Professor.objects.filter(pk=self.professor.pk).exists())
        self.assertRedirects(response, reverse('home'))


class MateriaTestCase(TestCase):
    def setUp(self):
        self.materia = Materia.objects.create(nome="Análise de Algoritmos")

    def testMateria(self):
        self.assertEqual(self.materia.nome, "Análise de Algoritmos")

    def testMateriaCreate(self):
        data = {"nome": self.materia.nome}
        response = self.client.post(reverse('salvar_materia'), data)
        self.assertRedirects(response, reverse('home'))

    def testMateriaEdit(self):
        response = self.client.get(reverse('editar_materia', args=[self.materia.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['materia'], self.materia)

    def testMateriaDelete(self):
        response = self.client.post(reverse('delete_materia', args=[self.materia.pk]))
        self.assertFalse(Materia.objects.filter(pk=self.materia.pk).exists())
        self.assertRedirects(response, reverse('home'))

class CursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(nome="Engenharia de Alimentos")

    def testCurso(self):
        self.assertEqual(self.curso.nome, "Engenharia de Alimentos")

    def testCursoCreate(self):
        data = {"nome": self.curso.nome}
        response = self.client.post(reverse('salvar_curso'), data)
        self.assertRedirects(response, reverse('home'))

    def testCursoEdit(self):
        response = self.client.get(reverse('editar_curso', args=[self.curso.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['curso'], self.curso)

    def testCursoDelete(self):
        response = self.client.post(reverse('delete_curso', args=[self.curso.pk]))
        self.assertFalse(Curso.objects.filter(pk=self.curso.pk).exists())
        self.assertRedirects(response, reverse('home'))
