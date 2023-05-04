name = input()


def normalize(name):
    replacements = {
        "é": "e",
        "ë": "e",
        "á": "a",
        "å": "aa",
        "œ": "oe",
        "æ": "ae"
    }

    for char, replacement in replacements.items():
        name = name.replace(char, replacement)

    return name


print(normalize(name))
