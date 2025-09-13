from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', args=(4,))
        self.assertEqual(url, '/recipes/category/4/')
    
    def test_recipe_recipe_url_is_connect(self):
        url = reverse('recipes:recipe', args=(1,))
        self.assertEqual(url, '/recipes/1/')