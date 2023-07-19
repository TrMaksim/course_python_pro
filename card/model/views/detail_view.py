from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from model.models.card_model import Cards
from model.permissions import IsOwner
from model.serializers import CardsSerializer


class CardDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_card(self, card_id):
        try:
            return Cards.objects.get(pk=card_id, owner=self.request.user)
        except Cards.DoesNotExist:
            return None

    def get(self, request, card_id):
        card = self.get_card(card_id)
        if card:
            serializer = CardsSerializer(card)
            return Response(serializer.data)
        return Response({"detail": "Card not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, card_id):
        card = self.get_card(card_id)
        if not card:
            return Response(
                {"detail": "Card not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = CardsSerializer(card, data=request.data, partial=True)
        if serializer.is_valid():
            if card.status == "frozen" or card.owner != request.user:
                return Response(
                    {"detail": "You can only modify your own active cards."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            updatable_fields = ["cvv", "pan", "status"]
            for field in updatable_fields:
                if field in request.data and not request.user.is_staff:
                    return Response(
                        {
                            "detail": "You do not have permission to update '{}'.".format(
                                field
                            )
                        },
                        status=status.HTTP_403_FORBIDDEN,
                    )

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, card_id):
        card = self.get_card(card_id)
        if not card:
            return Response(
                {"detail": "Card not found."}, status=status.HTTP_404_NOT_FOUND
            )

        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
