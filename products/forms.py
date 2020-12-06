from django import forms
from .models import Category, Product, Variants, Images, Comment, Color, Size
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from django.forms import ModelForm


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductVariantForm(forms.ModelForm):

    class Meta:
        model = Variants
        fields = ['title', 'color', 'size', 'image_id', 'quantity', 'price']


class ProductColorForm(forms.ModelForm):

    class Meta:
        model = Variants
        fields = ['title', 'color', 'quantity', 'price', 'image_id']


class ProductSizeForm(forms.ModelForm):

    class Meta:
        model = Variants
        fields = ['title', 'size', 'quantity', 'price']


class ProductImageForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = ['title', 'image',]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']


class AddColorForm(ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'code']


class AddSizeForm(ModelForm):
    class Meta:
        model = Size
        fields = ['name', 'code']


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'code']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'name',
            'code': '#000000',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
