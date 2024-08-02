from rest_framework.generics import RetrieveAPIView
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.order_by("id")
    serializer_class = MovieSerializer
