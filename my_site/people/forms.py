from django.forms import ModelForm, Textarea, ModelChoiceField, TextInput, IntegerField, NumberInput, Select, Form, \
    ChoiceField
from people.models import Person, Country


class CreatePersonForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].empty_label = None

    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            'first_name': TextInput(attrs={"class": "form-control"}),
            'second_name': TextInput(attrs={"class": "form-control"}),
            'biography': TextInput(attrs={"class": "form-control"}),
            'age': NumberInput(attrs={"class": "form-control"}),
            "country": Select(attrs={'class': "form-control"})
        }


class DeletePersonForm(Form):
    persons = [(p.id, f"{p.first_name} {p.second_name}") for p in Person.objects.all()]
    persons += [("", "Выберите человека")]
    person = ChoiceField(choices=persons, widget=Select(attrs={'class': "form-control"}))

