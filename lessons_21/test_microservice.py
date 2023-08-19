import unittest
import httpx
import asyncio


ingredients_service_url = "http://127.0.0.1:8000"


buns_service_url = "http://127.0.0.1:8001"


class TestIngredientsMicroservice(unittest.TestCase):
    async def fetch_ingredient_balance(self, ingredient):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{ingredients_service_url}/ingredients/{ingredient}"
            )
            return response

    def test_get_flour_balance(self):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self.fetch_ingredient_balance("flour"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["ingredient"], "flour")

    def test_get_nonexistent_ingredient(self):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self.fetch_ingredient_balance("nonexistent"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("error"), "Ingredient not found")


class TestBunsCalculatorMicroservice(unittest.TestCase):
    async def fetch_available_buns(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{buns_service_url}/calculate_buns")
            return response

    def test_calculate_available_buns(self):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self.fetch_available_buns())
        self.assertEqual(response.status_code, 200)
        self.assertIn("available_buns", response.json())


if __name__ == "__main__":
    unittest.main()
