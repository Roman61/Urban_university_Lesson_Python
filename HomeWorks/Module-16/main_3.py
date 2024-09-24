from fastapi import FastAPI

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username, age) -> str:
    user_id = 1
    if len(users) != 0:
        user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id, username, age) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is update"


@app.delete("/user/{user_id}")
async def delete_user(user_id) -> str:
    delete = users.pop(user_id)
    return f"The user {delete} is delete"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="192.168.5.70", port=80)
