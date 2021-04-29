from rest_framework import viewsets, permissions
from api.serializers import MovieSerializer
from viewer.models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
