a = input()
b = input()


def contains(text, pattern):
    exist = False

    if pattern in text:
        exist = True

    return exist


print(contains(a, b))
