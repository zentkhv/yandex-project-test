"""Модуль для отладки."""
import json
import sys

if __name__ == "__main__":
    test_dict = {1:1, 2:2, 3:3}

    for key, value in test_dict.items():

        print(f"{key}: {value}")

    json_dict = json.dumps(test_dict, ensure_ascii=False, indent=4)
    print(json_dict)

    sys.exit(0)
