import string

from pydantic import BaseModel

LOWER_LETTERS = string.ascii_lowercase
SIZE = len(LOWER_LETTERS)


class Caesar:
    class Message(BaseModel):
        text: str
        offset: int
        mode: str

    @staticmethod
    def encrypt(text: str, offset: int):
        lower_text = text.lower()
        offset %= SIZE
        return ''.join(
            [LOWER_LETTERS[(ord(char) % 97 + offset) % SIZE] if char.isalpha() else char for char in lower_text])

    @staticmethod
    def decrypt(text: str, offset: int):
        lower_text = text.lower()
        offset %= SIZE
        return ''.join(
            LOWER_LETTERS[(ord(char) % 97 - offset) % SIZE] if char.isalpha() else char for char in lower_text)
