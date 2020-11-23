from django import forms
from .models import Category, Product, Variants


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
        fields = ['title', 'color', 'size', 'quantity', 'price']


class ProductColorForm(forms.ModelForm):

    class Meta:
        model = Variants
        fields = ['title', 'color', 'quantity', 'price']


class ProductSizeForm(forms.ModelForm):

    class Meta:
        model = Variants
        fields = ['title', 'size', 'quantity', 'price']
