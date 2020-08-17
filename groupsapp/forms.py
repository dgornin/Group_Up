from django import forms
from groupsapp.models import Group, Available, Task


class GroupAddForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupAddForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name == 'uuid':
                field.widget = forms.HiddenInput()


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name == 'group' or field_name == 'is_done':
                field.widget = forms.HiddenInput()


class GroupEditForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupEditForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name == 'uuid':
                field.widget = forms.HiddenInput()
