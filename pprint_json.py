import json
import argparse

parser = argparse.ArgumentParser(description='Path to json file')
parser.add_argument("filepath", type=str, help="Path to json file")
args = parser.parse_args()


def load_data(filepath):
    with open(filepath, "r", encoding="UTF-8") as path:
        return json.load(path)


def pretty_print_json(data_result):
    print(json.dumps(data_result, sort_keys=True,
                     indent=4, ensure_ascii=False, separators=(",", ": ")))


if __name__ == "__main__":
    data_result = load_data(args.filepath)
    pretty_print_json(data_result)



