from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "year",
            "email",
            "enrollment_date",
        ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        self.fields["first_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter your first name",
            }
        )

        self.fields["last_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter your last name",
            }
        )

        self.fields["year"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter your email address",
            }
        )

        self.fields["enrollment_date"].widget.attrs.update(
            {
                "class": "form-control",
                "type": "date",
            }
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("@example.com"):
            raise forms.ValidationError("Email address must end with '@example.com'")
        return email

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name and first_name == last_name:
            self.add_error(
                "last_name", "Имя и фамилия не могут иметь одинаковые значения"
            )
