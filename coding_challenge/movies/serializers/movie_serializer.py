from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from reviews.models import Review
from reviews.serializers.review_serializer import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):
    runtime_formatted = serializers.SerializerMethodField(read_only=True)
    avg_rating = serializers.SerializerMethodField(read_only=True)
    reviewers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "runtime_formatted",
            "release_date",
            "avg_rating",
            "reviewers",
        )

    def get_runtime_formatted(self, obj):
        minutes = obj.runtime
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours}:{mins:02d}"

    def get_avg_rating(self, obj):
        reviews = self.get_reviews(obj)
        avg_rating = reviews.aggregate(Avg("rating"))["rating__avg"]
        if avg_rating is None:
            return 0
        return avg_rating

    def get_reviewers(self, obj):
        reviews = self.get_reviews(obj)
        return ReviewSerializer(reviews, many=True).data

    def get_reviews(self, obj):
        if not hasattr(self, "_reviews_cache"):
            self._reviews_cache = Review.objects.filter(movie=obj)

        return self._reviews_cache
