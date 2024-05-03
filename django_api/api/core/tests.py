from django.test import TestCase
from core.models import CustomUser
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client

class CustomUserTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='teste.user',
            email='teste@example.com',
            password='1234'
        )
        self.client = Client()
        self.client.force_login(user=self.user)
        self.data = CustomUser.objects.create(nome="Gabriel",
                                              sobrenome="Pereira",
                                              cep="13806064",
                                              cidade="Mogi Mirim",
                                              uf="SP",
                                              endereco="Rua Rachid Ajub Andare",
                                              numero="111",
                                              bairro="Conjunto Residencial Anselmo Lopes Bueno")

    def testUser(self):
        self.assertEqual(self.data.nome, "Gabriel")
        self.assertEqual(self.data.sobrenome, "Pereira")
        self.assertEqual(self.data.cep, "13806064")
        self.assertEqual(self.data.cidade, "Mogi Mirim")
        self.assertEqual(self.data.uf, "SP")
        self.assertEqual(self.data.endereco, "Rua Rachid Ajub Andare")
        self.assertEqual(self.data.numero, "111")
        self.assertEqual(self.data.bairro, "Conjunto Residencial Anselmo Lopes Bueno")

    def testUserGet(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def testUserCreate(self):
        data = {"nome": self.data.nome,
                "sobrenome": self.data.sobrenome,
                "cep":self.data.cep,
                "cidade": self.data.cidade,
                "uf":self.data.uf,
                "endereco":self.data.endereco,
                "numero":self.data.numero,
                "bairro":self.data.bairro}
        response = self.client.post(reverse('cadastrar'), data)
        self.assertEqual(response.status_code, 302)

    def testUserEdit(self):
        response = self.client.get(reverse('edit_user', args=[self.data.pk]))
        self.assertEqual(response.status_code, 200)
        novo_usuario = CustomUser.objects.get(nome=self.data.nome)
        self.assertIsNotNone(novo_usuario)

    def testUserDelete(self):
        response = self.client.post(reverse('delete_user', args=[self.data.pk]))
        self.assertFalse(CustomUser.objects.filter(pk=self.data.pk).exists())
        self.assertRedirects(response, reverse('index'))


