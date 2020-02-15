from django.test import TestCase, Client

from shop.models import Category, Product


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name="Test", slug="test")
        Product.objects.create(
            category_id=1,
            title="Product-test",
            description="Desc",
            slug="product-test")

    def test_category(self):
        category = Category.objects.get(slug="test")
        self.assertEqual(category.name, "Test")

    def test_category_exists(self):
        category = Category.objects.filter(slug="test")
        self.assertTrue(category.exists())

    def test_my(self):
        product = Product.objects.get(category__name__icontains="Test")
        self.assertEqual(product.title, 'Product-test')

    def test_details(self):
        response = self.client.get('/category-vue/')
        self.assertEqual(response.status_code, 200)

    def test_cat_get(self):
        response = self.client.get('/category/test/')
        self.assertEqual(response.status_code, 200)
        product = Product.objects.get(category__name__icontains="Test")
        # print(response.context)
        self.assertTrue(product in response.context["object_list"])

