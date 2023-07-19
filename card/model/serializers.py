from rest_framework import serializers
from model.models.card_model import Cards


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = "__all__"
