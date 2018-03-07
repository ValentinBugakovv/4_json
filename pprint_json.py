import json
import argparse
import os


def input_user_arguments():
    parser = argparse.ArgumentParser(description="Path to json file")
    parser.add_argument("filepath",
                        nargs="+",
                        help="Path to json file",
                        )
    args = parser.parse_args()
    return args.filepath


def load_data(filepath):
    with open(filepath, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)


def pretty_print_json(json_content):
    print(json.dumps(json_content,
                     sort_keys=True,
                     indent=4,
                     ensure_ascii=False,
                     separators=(",", ": ")
                     )
          )


def main():
    input_result = input_user_arguments()
    if input_result.endswith(".json") and os.path.isfile(input_result):
        json_result = load_data(input_result)
        pretty_print_json(json_result)
    else:
        raise ("This is not a json file")


if __name__ == "__main__":
    main()
