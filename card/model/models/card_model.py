import uuid
import asyncio
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User


class Cards(models.Model):
    STATUS_CHOICES = (
        ("new", "New"),
        ("active", "Active"),
        ("frozen", "Frozen"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pan = models.CharField(max_length=20)
    expiry_date = models.CharField(max_length=20)
    cvv = models.CharField(max_length=4)
    issue_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="new")

    def __str__(self):
        return f"{self.owner}-{self.name}"

    def digits_on(self, number: str) -> list:
        return [int(digit) for digit in str(number) if digit.isdigit()]

    def is_valid(self) -> bool:
        digits = self.digits_on(self.pan)

        if len(digits) != 16:
            return False

        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        check_sum = sum(odd_digits)

        for even_number in even_digits:
            double_even = even_number * 2
            if double_even > 9:
                double_even -= 9
            check_sum += double_even

        return check_sum % 10 == 0

    async def activate(self) -> str:
        if self.status == "new":
            await asyncio.sleep(120)
            self.status = "active"
            self.save()
            return "activate"
        elif self.status == "frozen":
            return "Frozen card, cannot be activated"

    def block(self) -> str:
        if self.status == "active":
            self.status = "frozen"
            self.save()
            return "frozen"
