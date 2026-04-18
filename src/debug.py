import json
import sys

if __name__ == "__main__":
    test_dict = {1:1, 2:2, 3:3}

    for item in test_dict:
        print(f"{item}: {test_dict[item]}")

    json_dict = json.dumps(test_dict, ensure_ascii=False, indent=4)
    print(json_dict)

    sys.exit(0)

