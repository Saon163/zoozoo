from django import forms
from Zoo.models import Animal, Zone

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = '__all__'

class AnimalSearchForm(forms.Form):
    query = forms.CharField(label='검색어', max_length=100)