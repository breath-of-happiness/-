import json

def task() -> float:
    filename = "input.json"
    with open(filename) as file:
        json_data = json.load(file)

    sum_ = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_, 3)

print(task())
