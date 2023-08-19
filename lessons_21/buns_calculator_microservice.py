from fastapi import FastAPI, HTTPException
import httpx

app_buns = FastAPI()


ingredients_service_url = "http://127.0.0.1:8000"


async def calculate_available_buns():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ingredients_service_url}/ingredients/flour")
        flour_balance = response.json().get("balance", 0)

        response = await client.get(f"{ingredients_service_url}/ingredients/sugar")
        sugar_balance = response.json().get("balance", 0)

        response = await client.get(f"{ingredients_service_url}/ingredients/yeast")
        yeast_balance = response.json().get("balance", 0)

        response = await client.get(f"{ingredients_service_url}/ingredients/eggs")
        eggs_balance = response.json().get("balance", 0)

    available_buns = min(
        flour_balance // 50, sugar_balance // 10, yeast_balance // 1, eggs_balance // 2
    )
    return available_buns


@app_buns.get("/calculate_buns")
async def get_available_buns():
    available_buns = await calculate_available_buns()
    return {"available_buns": available_buns}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app_buns, host="127.0.0.1", port=8001)
