import json
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Path to json file"
    )
    parser.add_argument(
        "filepath",
        help="Path to json file",
    )
    args = parser.parse_args()
    return args


def load_data(filepath):
    with open(filepath, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)


def pretty_print_json(json_content):
    print(json.dumps(
        json_content,
        sort_keys=True,
        indent=4,
        ensure_ascii=False,
        separators=(",", ": ")
    ))


def main():
    file_path = get_arguments().filepath
    data_result = load_data(file_path)
    pretty_print_json(data_result)


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("This is not a json file")
