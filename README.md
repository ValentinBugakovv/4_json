# Prettify JSON

Программа форматирует json файл, красиво печатая его 

# Quickstart

```python
# для работы программы необходимо импортировать модуль json
import json

# Функция def load_data принимет на вход путь до файла и декодирует json в строку
def load_data(filepath):
return json.load(path)

# Функция def pretty_print_json получает на вход результат функции def load_data 
# и преобразует строку и возращает красиво отформатированый json файл

def pretty_print_json(result)

```

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>

```
```json
# пример вывода
[
    {
        "name": "<< БУРУНДУКИ 13 SHOP>>",
        "gid": 55697921,
        "members_count": 97
    },
    {
        "name": "Проект SweetieBot",
        "gid": 118486414,
        "members_count": 1592
    },
    ]

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
