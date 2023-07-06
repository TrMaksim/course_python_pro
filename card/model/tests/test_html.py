from django.test import TestCase
from django.urls import reverse
from card.model.models import Cards


class CardsPageTest(TestCase):
    def test_cards_page_render(self):
        response = self.client.get(reverse('cards'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cards/cards_page.html')

    def test_cards_list_content(self):
        Cards.objects.create(
            pan="1234567890123456",
            expiry_date="12/25",
            cvv="123",
            owner_id="1",
            status="Active"
        )

        response = self.client.get(reverse('cards'))
        self.assertContains(response, "Card Pan")
        self.assertContains(response, "1234567890123456")
        self.assertContains(response, "Expiration date")
        self.assertContains(response, "12/25")
        self.assertContains(response, "Card CVV")
        self.assertContains(response, "123")
        self.assertContains(response, "Cardholder ID")
        self.assertContains(response, "1")
        self.assertContains(response, "Status Card")
        self.assertContains(response, "Active")

    def test_empty_cards_list(self):
        response = self.client.get(reverse('cards'))
        self.assertContains(response, "There's not a single card here")

    def test_create_card_page_render(self):
        response = self.client.get(reverse('create_card'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cards/create_card.html')

    def test_create_card_form(self):
        data = {
            'pan_card': '1234567890123456',
            'expiry_date_card': '12/25',
            'cvv_card': '123',
            'status_card': 'Active'
        }
        response = self.client.post(reverse('create_card'), data=data)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('cards'))

        self.assertEqual(Cards.objects.count(), 1)
        card = Cards.objects.first()
        self.assertEqual(card.pan, '1234567890123456')
        self.assertEqual(card.expiry_date, '12/25')
        self.assertEqual(card.cvv, '123')
        self.assertEqual(card.status, 'Active')
