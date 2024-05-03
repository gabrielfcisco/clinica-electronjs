from django.test import TestCase
from core.models import CustomUser
from django.urls import reverse
from django.test import Client

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(nome="Gabriel", sobrenome="pereira", cep="13806064", cidade="mogi mirim", uf="SP",
                                            endereco="rua rachid ajub andare", numero="111", bairro="Conjunto Residencial Anselmo Lopes Bueno")

    def testUser(self):
        self.assertEqual(self.user.nome, "Gabriel")
        self.assertEqual(self.user.sobrenome, "pereira")
        self.assertEqual(self.user.cep, "13806064")
        self.assertEqual(self.user.cidade, "mogi mirim")
        self.assertEqual(self.user.uf, "SP")
        self.assertEqual(self.user.endereco, "rua rachid ajub andare")
        self.assertEqual(self.user.numero, "111")
        self.assertEqual(self.user.bairro, "Conjunto Residencial Anselmo Lopes Bueno")

    def testUserGet(self):
        c = Client()
        c.login(username="heitorscheidt", password="1234")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)

    def testUserCreate(self):
        c = Client()
        c.login(username="heitorscheidt", password="1234")
        data = {"nome": self.user.nome, "sobrenome": self.user.sobrenome, "cep":self.user.cep, "cidade": self.user.cidade, "uf":self.user.uf,
                "endereco":self.user.endereco, "numero":self.user.numero, "bairro":self.user.bairro}
        response = self.client.post(reverse('cadastrar'), data)
        self.assertEqual(response.status_code, 302)
<<<<<<< Updated upstream
        #self.assertRedirects(response, reverse('index'),status_code=302, target_status_code=200, fetch_redirect_response=True)
=======
        # self.assertRedirects(response, 'index',status_code=302, target_status_code=200, fetch_redirect_response=True)
>>>>>>> Stashed changes

    def testuserEdit(self):
        c = Client()
        c.login(username="heitorscheidt", password="1234")
        response = self.client.get(reverse('edit_user', args=[self.user.pk]))
        self.assertEqual(response.status_code, 302)
        novo_usuario = CustomUser.objects.get(nome=self.user.nome)
        self.assertIsNotNone(novo_usuario)

    def testUserDelete(self):
        c = Client()
        c.login(username="heitorscheidt", password="1234")
        print("Antes da exclusão:", CustomUser.objects.filter(pk=self.user.pk).exists())  # Verificar se o usuário existe antes da exclusão
        response = c.post(reverse('delete_user', args=[self.user.pk]))
        print("Depois da exclusão:", CustomUser.objects.filter(pk=self.user.pk).exists())  # Verificar se o usuário existe após a exclusão
        self.assertFalse(CustomUser.objects.filter(pk=self.user.pk).exists())
        self.assertRedirects(response, reverse('home'))


