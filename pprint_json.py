import os
import json




def load_data(filepath):
    filepath = os.path.abspath(filepath)
    with open(filepath, 'r', encoding="UTF-8") as f:
        return json.load(f)


def pretty_print_json(data, sort=True, indents=4):
    if type(data) is str:
        print(json.dumps(json.loads(data), sort_keys=sort, indent=indents, ))
    else:
        print(json.dumps(data, sort_keys=sort, indent=indents))
    return None


if __name__ == '__main__':
    pretty_print_json(load_data(str(input())))


