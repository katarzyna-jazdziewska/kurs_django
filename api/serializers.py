from viewer.models import Movie, Genre
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genre', 'rating', 'released']

    def create(self, validated_data):
        # data = validated_data
        # genre = Genre.objects.filter(id=validated_data['genre'])
        # data['genre'] = genre
        movie = Movie(**validated_data)
        movie.save()
        return movie
