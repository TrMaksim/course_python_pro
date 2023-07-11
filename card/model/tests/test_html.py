from django.test import TestCase
from card.model.models import Cards


class CardsPageTest(TestCase):
    def test_cards_list_template(self):
        expected_template = """
        {% if cards %}
        <table>
            <tr>
                <th>Card Pan</th>
                <th>Expiration date</th>
                <th>Card CVV</th>
                <th>Cardholder ID</th>
                <th>Status Card</th>
            </tr>
            {% for card in cards %}
            <tr>
                <td>{{ card.pan }}</td>
                <td>{{ card.expiry_date }}</td>
                <td>{{ card.cvv }}</td>
                <td>{{ card.owner_id }}</td>
                <td>{{ card.status }}</td>
            </tr>
            {% endfor %}
        </table>
        <a href="{% url 'create_card' %}">Add new Card</a>
        {% else %}
        <p>There's not a single card here</p>
        {% endif %}
        """

        self.assertMultiLineEqual(str(Cards.objects.get(pk=1)), expected_template)

    def test_create_card_template(self):
        expected_template = """
        <h2>Create Card</h2>
        <form method="POST" action="{% url 'create_card' %}">
            {% csrf_token %}
            <label for="pan_card">PAN Card:</label>
            <input type="text" name="pan_card" required>
            <label for="expiry_date_card">Expiry Date:</label>
            <input type="text" name="expiry_date_card" required>
            <label for="cvv_card">CVV:</label>
            <input type="text" name="cvv_card" required>
            <label for="status_card">Status:</label>
            <input type="text" name="status_card" required>
            <button type="submit">Create</button>
        </form>
        """

        self.assertMultiLineEqual(str(Cards.objects.get(pk=1)), expected_template)
