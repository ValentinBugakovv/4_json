import json
import argparse
import os


def arguments():
    parser = argparse.ArgumentParser(description='Path to json file')
    parser.add_argument("filepath", type=str, help="Path to json file")
    args = parser.parse_args()
    return args.filepath


def load_data(filepath):
    with open(filepath, "r", encoding="UTF-8") as path:
        return json.load(path)


def pretty_print_json(json_content):
    print(json.dumps(json_content,
                     sort_keys=True,
                     indent=4,
                     ensure_ascii=False,
                     separators=(",", ": ")
     ))


def main():
    fact = arguments()
    if fact.endswith('.json') and os.path.isfile(fact) == True:
        data_result = load_data(fact)
        pretty_print_json(data_result)
    else:
        raise ("This is not a json file")


if __name__ == "__main__":
    main()
