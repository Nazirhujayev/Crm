from django import forms
from .models import User, Order

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangizni kiriting'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Otaning ismi'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqami'}),
            'family_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Oilaning telefon raqami'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'brith': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'payment_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Toʻlov summasi'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['brith'].input_formats = ['%Y-%m-%d']

            if self.instance and self.instance.pk:
                self.fields['brith'].initial = self.instance.brith

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['amount']
        
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Toʻlov summasi'}),
        }