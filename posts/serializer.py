from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from posts.models import Post, Comment
from django.utils import timezone
from datetime import timedelta


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True, source='comment_set')

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        if not self.is_user_adult(user):
            raise serializers.ValidationError("Вы должны быть старше 18 лет, чтобы создавать посты.")
        return super().create(validated_data)

    def is_user_adult(self, user):
        return user.date_born <= (timezone.now() - timedelta(days=18*365)).date()

    def validate_title(self, value):
        # Проверяем, что заголовок не содержит запрещенные слова
        banned_words = ['ерунда', 'глупость', 'чепуха']
        if any(banned_word in value.lower() for banned_word in banned_words):
            raise serializers.ValidationError("Заголовок содержит запрещенные слова.")
        return value



