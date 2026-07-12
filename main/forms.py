from django import forms
from .models import *




class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class ATForm(forms.ModelForm):
    class Meta:
        model = Article_Type
        fields = '__all__'

class GenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = '__all__'

class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'


class SKUForm(forms.ModelForm):
    class Meta:
        model = SKU
        exclude = ['gender', 'article_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'design_pattern' in self.fields:   # 🔥 IMPORTANT SAFETY CHECK
            self.fields['design_pattern'].widget = forms.Select(
                attrs={
                    "class": "form-select",
                    "id": "inputDesignPattern"
                }
            )
    