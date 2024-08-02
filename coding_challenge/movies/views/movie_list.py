from rest_framework.generics import ListCreateAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.order_by("id")
    serializer_class = MovieSerializer

    def filter_queryset(self, queryset):
        q: str = self.request.GET.get("q")
        gte: str = self.request.GET.get("gte")

        if q and gte and q.isnumeric() and gte in ["0", "1"]:
            q = int(q)
            if gte == "1":
                return queryset.filter(runtime__gte=q)
            elif gte == "0":
                return queryset.filter(runtime__lt=q)

        return super().filter_queryset(queryset)
