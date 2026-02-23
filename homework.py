from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

users = [
    {'id': 1, 'name': "Ali Valiyev", 'age': 25, 'address': "Toshkent"},
    {'id': 2, 'name': "Vali Aliyev", 'age': 30, 'address': "Samarqand"},
    {'id': 3, 'name': "Hasan Husanov", 'age': 22, 'address': "Buxoro"},
    {'id': 4, 'name': "Husan Hasanov", 'age': 28, 'address': "Andijon"},
    {'id': 5, 'name': "Karim Karimov", 'age': 35, 'address': "Farg'ona"},
]


@app.get("/")
def hello() -> dict:
    return {'message': "Salom"}


@app.get("/users/")
def view_users() -> list[dict]:
    return users


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int) -> dict:
    for user in users:
        if user['id'] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")


@app.get("/users/address/{user_address}")
def get_user_by_address(user_address: str) -> dict:
    for user in users:
        if user['address'].lower() == user_address.lower():
            return user
    raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")


if __name__ == '__main__':
    uvicorn.run(app, port=8001)
