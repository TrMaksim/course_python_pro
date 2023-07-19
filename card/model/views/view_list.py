from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from model.models.card_model import Cards
from model.serializers import CardsSerializer


class CardsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cards = Cards.objects.filter(owner=request.user)
        serializer = CardsSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
