from fastapi import FastAPI, HTTPException
import uvicorn
from utils.caesar import *
from utils.rail_fence import *

USERS_PATH = "data/names.txt"

app = FastAPI()


@app.get("/test")
def hi_from() -> dict:
    return {"msg": "hi from test"}


@app.get("/test/{name}")
def add_name(name: str):

    with open(USERS_PATH, "a") as f:
        f.write(name + "\n")
    return {"msg": "saved user"}


@app.post("/caesar/")
def manipulate_text(text_manipulate: Caesar.Message):
    match text_manipulate.mode:
        case "encrypt":
            return {"encrypted_text": Caesar.encrypt(text_manipulate.text, text_manipulate.offset)}
        case "decrypt":
            return {"decrypted_text": Caesar.decrypt(text_manipulate.text, text_manipulate.offset)}
        case _:
            raise HTTPException(status_code=409, detail="invalid mode!!!")


@app.get("/fence/encrypt")
def encrypt_text(text: str):
    return {"encrypted_text": RailFence.encrypt(text)}


@app.post("/fence/decrypt")
def decrypt_text(text: RailFence.Message):
    return {"decrypted_text": RailFence.decrypt(text.text)}


if __name__ == "__main__":
    uvicorn.run(app)
