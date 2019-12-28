from django import forms

from .models import Product

#Ch.24 Raw HTML Form (Understanding the concept of GET and POST)
#class ProductForm(forms.ModelForm):
#    class Meta:
#        model = Product
#        fields = [
#                'title',
#                'description',
#                'price',
#                'summary'
#                ]

#Ch.27 Form Validation Methods
class ProductForm(forms.ModelForm):
    title       = forms.CharField(label = '', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(
            required=False,
            widget=forms.Textarea(
                attrs={
                    "placeholder":"Your Description",
                    "class":"new-class-name two",
                    "id": "my-id-for-textareas",
                    "rows": 20,
                    "cols": 120
                    }
                )
            )
    class Meta:
        model = Product
        fields = [
                'title',
                'description',
                'price',
                'summary'
                ]


#Ch.27 End

#Ch.25 Pure Django Form
#class RawProductForm(forms.Form):
#    title       = forms.CharField()
#    description = forms.CharField()
#    price       = forms.DecimalField()

#Ch.26 Form Widgets
class RawProductForm(forms.Form):
    title       = forms.CharField(label = '', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(
            required=False,
            widget=forms.Textarea(
                attrs={
                    "placeholder":"Your Description",
                    "class":"new-class-name two",
                    "id": "my-id-for-textareas",
                    "rows": 20,
                    "cols": 120
                    }
                )
            )
    price       = forms.DecimalField(initial = 199.99)

