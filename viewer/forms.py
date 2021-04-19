import re
from datetime import date
from django.core.exceptions import ValidationError
from django.forms import (Form,
                          CharField,
                          ModelChoiceField,
                          IntegerField, DateField, Textarea, ModelForm)
from viewer.models import Genre, Movie


# class MojaKlasaPola(IntegerField):
#     def clean(self):
#         pass

# wtedy przy polu rating zamiast IntegerField trzeba dać MojaKlasaPola


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized!')


# jeśli chcemy zdefiniować walidator to wszystkich pól tego samego typu to tworzymy klasę pola i tam dajemy walidator
class PastDateField(DateField):

    def validate(self, value):
        super().validate(value)
        if value > date.today():
            raise ValidationError("Future dates not allowed!!!")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__" # ==> exclude = []

    title = CharField(validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=9)
    released = PastDateField()

    # title = CharField(max_length=170, validators=[capitalized_validator])
    # genre = ModelChoiceField(queryset=Genre.objects)
    # rating = IntegerField(min_value=1, max_value=9)
    # released = PastDateField()
    # description = CharField(widget=Textarea, required=False)

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)
        # cleaned_data['description'] = clean_description()

    def clean(self):
        result = super().clean()
        if result['genre'].name == "Komedia" and result['rating'] > 5:
            # self.add_error('genre', 'to błąd - genre')
            # self.add_error('rating', 'to błąd - rating')
            raise ValidationError("Commedies are not so good to be rated over 5!")
        return result
