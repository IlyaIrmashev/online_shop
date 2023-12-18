from django import forms

from catalog.models import Product, Version


def words_ban(text):
    words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    for word in words:
        if word in text:
            raise forms.ValidationError(f'Недопустимое слово \'{word}\'')


class StyleForfMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForfMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        words_ban(cleaned_data)
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        words_ban(cleaned_data)
        return cleaned_data


class VersionForm(StyleForfMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('is_published', 'category', 'description')
