from django.conf import settings
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.core.mail import send_mail

class RegisterUser(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('library:books_list')

    def form_valid(self, form):
        # 1. Сначала запускаем стандартное сохранение Django CreateView
        response = super().form_valid(form)

        # 2. Достаем созданного пользователя из self.object
        user = self.object

        # 3. Отправляем письмо, используя его реальный email
        self.send_welcome_mail(user.email)

        return response

    def send_welcome_mail(self, user_email):
        subject = 'Welcome to Django Service'
        message = f'Hi {user_email}, thank you for registering.'
        from_email = settings.DEFAULT_FROM_EMAIL  # Безопаснее использовать этот параметр
        recipient_list = [user_email]

        # Добавляем fail_silently=False, чтобы падать с ошибкой, если SMTP не сработает
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)


