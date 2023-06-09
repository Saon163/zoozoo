from django import forms
from Zoo.models import Animal, Zone, CheckLog

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


class CheckLogForm(forms.ModelForm):
    class Meta:
        model = CheckLog
        fields = '__all__'
        widgets = {
            'clog_items': forms.Textarea(attrs={'rows': 5}),  # 체크리스트 항목을 입력할 수 있는 Textarea 위젯
        }

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')