from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from model.models.card_model import Cards


class CardsListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse("cards-list")

    def test_get_cards_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_card(self):
        data = {
            "pan": "1234567890123456",
            "expiry_date": "12/25",
            "cvv": "123",
            "status": "new",
            "owner": self.user.id,  # Set the owner field here
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cards.objects.count(), 1)
        self.assertEqual(Cards.objects.get().pan, "1234567890123456")


class CardDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.card = Cards.objects.create(
            pan="1234567890123456",
            expiry_date="12/25",
            cvv="123",
            status="new",
            owner=self.user,
        )  # Set the owner field here
        self.url = reverse("card-detail", kwargs={"card_id": self.card.id})

    def test_get_card(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_card_not_found(self):
        invalid_url = reverse(
            "card-detail", kwargs={"card_id": "00000000-0000-0000-0000-000000000000"}
        )
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_card(self):
        data = {
            "cvv": "456",
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_other_user_card_frozen(self):
        # Create a new user who is not the owner of the card
        other_user = User.objects.create_user(
            username="otheruser", password="testpassword"
        )

        # Log in as the new user
        self.client.login(username="otheruser", password="testpassword")

        data = {
            # Update the necessary fields here
            "cvv": "456",
            "pan": "9876543210987654",
        }
        response = self.client.put(self.url, data)

        # The response should now return 403 instead of 404
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
