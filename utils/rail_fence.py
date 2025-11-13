from pydantic import BaseModel


class RailFence:
    class Message(BaseModel):
        text: str

    @staticmethod
    def encrypt(text: str):
        lower_text = text.lower().replace(" ", "")
        even = lower_text[::2]
        odd = lower_text[1::2]
        return even + odd

    @staticmethod
    def decrypt(text: str):
        lower_text = text.lower().replace(" ", "")
        size = len(lower_text)
        half_size = size / 2 if size % 2 == 0 else size // 2 + 1
        even = lower_text[:half_size]
        odd = lower_text[half_size:]
        decrypted_text = ""
        for i in range(size // 2):
            decrypted_text += even[i] + odd[i]
        if size % 2:
            decrypted_text += even[size // 2]

        return decrypted_text
