import json
from django.http import HttpRequest, JsonResponse
from django.views import View
from .models import Cards


class CardsView(View):

    def get(self, request: HttpRequest):
        cards = Cards.objects.all()
        return JsonResponse(
            {"cards": [{"pan": str(card.pan),
                        "expiry_date": str(card.expiry_date),
                        "cvv": str(card.cvv),
                        "owner_id": str(card.owner_id),
                        "status": str(card.status)} for card in cards]}
        )

    def post(self, request: HttpRequest):
        body = json.loads(request.body)
        card = Cards.objects.create(pan=body["pan"], expiry_date=body["expiry_date"],
                                    cvv=body["cvv"], status=body["status"])
        card.save()
        return JsonResponse({"id": str(card.id)})

    def digits_on(self, number: str) -> list:
        return [int(digit) for digit in str(number)]

    def is_valid(self, request: HttpRequest) -> bool:
        card_number = Cards.objects.get(pan="1234567890123456")
        digits = self.digits_on(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        check_sum = 0
        check_sum += sum(odd_digits)
        for even_numbers in even_digits:
            check_sum += sum(self.digits_on(even_numbers*2))
        return check_sum % 10 == 0
