from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_root():
    return {"message": "Главная страница"}


@app.get("/user/{user_id}")
async def get_user_by_id(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=1)):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def get_user(
        username: str = Path(min_lenght=5, max_lenght=20, description="Enter username"),
        age: int = Path(ge=18, le=120, description="Enter age")) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username} Возраст: {age}"}


@app.get("/user/admin")
async def get_admin():
    return {"message": "Вы вошли как администратор"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="192.168.5.70", port=80)
