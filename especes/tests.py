from django.test import TestCase
from especes.models import Especes
from django.contrib.auth.models import User, Permission

class especesTest(TestCase):


    def setUp(self):
        # Create a user
        user = User.objects.create_user(
            username='temporary',
            email='jacob@gmail.com',
            password='temporary'
            )

        # Get a permission
        permission_view = Permission.objects.get(codename='view_especes')
        permission_add = Permission.objects.get(codename='add_especes')
        permission_change = Permission.objects.get(codename='change_especes')
        permission_delete = Permission.objects.get(codename='delete_especes')

        # Add permissions for views
        user.user_permissions.add(permission_view)
        user.user_permissions.add(permission_add)
        user.user_permissions.add(permission_change)
        user.user_permissions.add(permission_delete)

        # Save the new user with his permission
        user.save()

        # création de l'objet espèce pour les tests
        self.espece = Especes(nom= 'rose')


    ###################
    ### Test modèle  ##
    ###################
       
    def test_nom(self):
        r"""
        Vérifie si la variable nom
        possède un label
        """
        verbose_name = "Nom de l'espèce"
        field_label = self.espece._meta.get_field('nom').verbose_name
        self.assertEqual(field_label, verbose_name)

    def test_nom_max_length(self):
        r"""
        Vérifie si la variable nom
        possède un max_length
        """
        max_length = self.espece._meta.get_field('nom').max_length
        self.assertEqual(max_length, 255)



    ####################################
    ### Test login & permissions user ##
    ####################################
    def test_login_user(self):
        r"""
        On veut vérifier que l'utilisateur est bien connecté
        avant de lancer les tests sur les vues et especes
        """
        login = self.client.login(username='temporary', password='temporary')
        self.assertEqual(login, True)

    def test_permission_user_view(self):
        r"""
        On veut vérifier que l'utilisateur a bien les permissions 'view'
        avant de lancer les tests sur les vues et especes
        """
        user = User.objects.get(username='temporary')
        self.assertEqual(user.has_perm('especes.view_especes'), True)

    def test_permission_user_add(self):
        r"""
        On veut vérifier que l'utilisateur a bien les permissions 'add'
        avant de lancer les tests sur les vues et especes
        """
        user = User.objects.get(username='temporary')
        self.assertEqual(user.has_perm('especes.add_especes'), True)

    def test_permission_user_change(self):
        r"""
        On veut vérifier que l'utilisateur a bien les permissions 'change'
        avant de lancer les tests sur les vues et especes
        """
        user = User.objects.get(username='temporary')
        self.assertEqual(user.has_perm('especes.change_especes'), True)

    def test_permission_user_delete(self):
        r"""
        On veut vérifier que l'utilisateur a bien les permissions 'delete'
        avant de lancer les tests sur les vues et especes
        """
        user = User.objects.get(username='temporary')
        self.assertEqual(user.has_perm('especes.delete_especes'), True)