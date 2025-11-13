import json


class JsonHandler:
    @staticmethod
    def load_data(json_file_path: str) -> list[dict]:
        with open(json_file_path, "r") as f:
            data = json.load(f)
        return data

    @staticmethod
    def save_data(data: list[dict], json_file_path: str):
        with open(json_file_path,"w") as f:
            json.dump(data, f)

