from .models import Projects
from django.forms import ModelForm
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'slug', 'description', 'demo_link', 'source_link']
        labels = {
            'title': 'Название проекта',
            'slug': 'Слаг',
            'image': 'Скриншот проекта',
            'tags': 'Теги',
            'description': 'Описание',
            'demo_link': 'Демо-версия',
            'source_link': 'Исходная версия'
        }

        widgets ={'tags': forms.CheckboxSelectMultiple(),}

        def __int__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})