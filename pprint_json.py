import json


def load_data(filepath):
    with open(filepath, "r", encoding="UTF-8") as path:
        return json.load(path)


def pretty_print_json(test):
    print(json.dumps(test, sort_keys=True,
                     indent=4, ensure_ascii=False, separators=(",", ": ")))


if __name__ == "__main__":
    result = load_data(input())
    pretty_print_json(result)



