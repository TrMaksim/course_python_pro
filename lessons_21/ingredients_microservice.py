from fastapi import FastAPI

app_ingredients = FastAPI()


ingredients_data = {
    "flour": 1500,
    "sugar": 250,
    "yeast": 175,
    "eggs": 12,
}


@app_ingredients.get("/ingredients/{ingredient}")
async def get_ingredient_balance(ingredient: str):
    if ingredient in ingredients_data:
        return {"ingredient": ingredient, "balance": ingredients_data[ingredient]}
    else:
        return {"error": "Ingredient not found"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app_ingredients, host="127.0.0.1", port=8000)
