import os
from django.core.validators import FileExtensionValidator
from django.db.models import (
    CharField, Model, DateField, DateTimeField, ForeignKey, TextField, IntegerField, DO_NOTHING, ImageField
)


def get_upload_path(instance, filename):
    return os.path.join(f"movies/movie_{instance.id}", filename)


class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=170)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    image = ImageField(null=True, blank=True,
                       upload_to=get_upload_path,
                       validators=[
                           FileExtensionValidator(
                               allowed_extensions=['bmp', 'jpg', 'jpeg', 'jpe', 'gif', 'tif', 'tiff', 'png']
                           )]
                       )
    created = DateTimeField(auto_now_add=True)
    # nieobowiazkowa = TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.released.year}) - {self.genre.name}"

    def __repr__(self):
        return f"{self.title} ({self.released.year}) - {self.genre.name}"

    # def save(self):
    #     self.nieobowiazkowa = "123"
    #     super(Movie, self).save()

    # def save(self):
    #     self.title = self.title.capitalize()
    #     super(Movie, self).save()
    #