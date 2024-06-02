from django import forms

from catalog.funcs import check_banned_words
from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ("title", "description", "image", "category", "price", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title')
        banned_word = check_banned_words(cleaned_data)
        if banned_word:
            raise forms.ValidationError(f'Отказано. В названии продукта содержится запрещенное слово: {banned_word}.')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        banned_word = check_banned_words(cleaned_data)
        if banned_word:
            raise forms.ValidationError(f'Отказано. В описании продукта содержится запрещенное слово: {banned_word}.')
        return cleaned_data
