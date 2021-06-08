from os import system

files = [
]


def check_format():
    for i in files:
        system(f"pycodestyle --show-source --show-pep8 --format=default {i}")


if __name__ == "__main__":
    check_format()
    print("All done!")
