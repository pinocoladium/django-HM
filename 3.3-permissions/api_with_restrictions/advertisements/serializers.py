from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        len_objects = len(Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN'))
        post = self.context["request"].method == 'POST' and len_objects > 9
        patch = self.context["request"].method == 'PATCH' and self.initial_data['status'] == 'OPEN' and len_objects > 9
        if post or patch:
            raise ValidationError('Превышен лимит открытых объявлений')
        return data
