from django.contrib.auth import get_user_model
from django.test import TestCase
from posts.models import Group, Post

User = get_user_model()

class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
                title= 'Тестовая группа',
                slug='Тестовый слаг',
                description='Тестовое описание',
        )
        cls.post = Post.objects.create(
                author=cls.user,
                text='Тестовая группа',
                )

    def test_models_have_correct_object_names(self):
        post = GroupModelTest.post
        field_verboses = {
                'text': 'Текст поста',
                'pub_date': 'Дата публикации',
                'author': 'Автор',
                'group': 'Группа',
                }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                        post._meta.get_field(value).verbose_name, expected)

            
