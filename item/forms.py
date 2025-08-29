
from .models import Item
from django import forms

STYLE_CLASS = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'name',
            'category',
            'description',
            'price',
            'image',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': STYLE_CLASS}),
            'category': forms.Select(attrs={'class': STYLE_CLASS}),
            'description': forms.Textarea(attrs={'class': STYLE_CLASS}),
            'price': forms.TextInput(attrs={'class': STYLE_CLASS}),
            'image': forms.FileInput(attrs={'class': STYLE_CLASS})
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'name',
            'category',
            'description',
            'price',
            'image',
            'is_sold',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': STYLE_CLASS}),
            'category': forms.Select(attrs={'class': STYLE_CLASS}),
            'description': forms.Textarea(attrs={'class': STYLE_CLASS}),
            'price': forms.TextInput(attrs={'class': STYLE_CLASS}),
            'image': forms.FileInput(attrs={'class': STYLE_CLASS})
        }