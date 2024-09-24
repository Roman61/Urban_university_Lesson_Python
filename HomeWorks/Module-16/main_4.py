from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int = None  # - номер пользователя
    username: str = ""  # - имя пользователя
    age: int = None  # - возраст пользователя


users = []
app = FastAPI()


@app.get("/users")
async def get_users() -> list:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username, age) -> User:
    try:
        user_id = 1
        if len(users) != 0:
            user_id = users[0].id
            for _user in users:
                if _user.id > user_id:
                    user_id = _user.id
            user_id += 1
        user = User()
        user.username = username
        user.age = int(age)
        user.id = user_id
        users.append(user)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id, username, age) -> User:
    for key, _user in enumerate(users):
        if _user.id == int(user_id):
            _user.username = username
            _user.age = int(age)
            users[key] = _user
            return _user
    raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id) -> User:
    for key, _user in enumerate(users):
        if _user.id == int(user_id):
            users.pop(key)
            return _user
    raise HTTPException(status_code=404, detail="Message not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="192.168.5.70", port=80)
