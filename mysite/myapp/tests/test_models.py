from django.test import TestCase
from myapp.models import Food

class FoodModelTest(TestCase):

    def setUp(self):
        self.food = Food.objects.create(
            name="Apple",
            carbs=25.0,
            protein=0.5,
            fats=0.3,
            calories=95
        )

    def test_food_creation(self):
        """Test if food object is created successfully"""
        self.assertEqual(self.food.name, "Apple")
        self.assertEqual(self.food.carbs, 25.0)
        self.assertEqual(self.food.protein, 0.5)
        self.assertEqual(self.food.fats, 0.3)
        self.assertEqual(self.food.calories, 95)

    def test_food_str_method(self):
        """Test the string representation of Food model"""
        self.assertEqual(str(self.food), "Apple")
