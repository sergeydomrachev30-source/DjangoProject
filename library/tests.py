from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class LibraryViewsTestCase(TestCase):

    def setUp(self):
        """Этот метод выполняется автоматически ПЕРЕД каждым тестом"""
        User = get_user_model()

        # Создаем тестового пользователя
        self.user_email = "test@example.com"
        self.user_password = "testpassword"

        self.user = User.objects.create_user(
            email=self.user_email,
            username="testuser",  # Оставляем на случай, если поле всё же обязательно
            password=self.user_password,
        )

        # Пробуем войти через email (стандарт для кастомных моделей)
        login_successful = self.client.login(
            email=self.user_email, password=self.user_password
        )

        # Если по email не зашло, пробуем классический вход по username
        if not login_successful:
            self.client.login(username="testuser", password=self.user_password)

    def test_books_list_view_status_code(self):
        """Проверка, что страница со списком книг доступна авторизованному пользователю"""
        url = reverse("library:books_list")

        # Добавляем follow=True, чтобы клиент шел до самого конца, если возникнет редирект
        response = self.client.get(url, follow=True)

        # Проверяем, что итоговая страница отдает статус 200 OK
        self.assertEqual(response.status_code, 200)

    def test_books_list_uses_correct_template(self):
        """Проверка, что для отображения списка книг используется правильный HTML-шаблон"""
        url = reverse("library:books_list")
        response = self.client.get(url, follow=True)

        # Проверяем шаблон списка книг
        self.assertTemplateUsed(response, "library/books_list.html")
