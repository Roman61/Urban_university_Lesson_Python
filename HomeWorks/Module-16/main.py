from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_root():
    return {"message": "Главная страница"}


@app.get("/user/{user_id}")
async def get_user_by_id(user_id):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def get_user(username, age):
    return {"message": f"Информация о пользователе. Имя: {username} Возраст: {age}"}


@app.get("/user/admin")
async def get_admin():
    return {"message": "Вы вошли как администратор"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
