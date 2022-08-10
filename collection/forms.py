from django import forms
from .models import Collection



class CollectionCreateForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "collection",
            "brand",
        ]

    
