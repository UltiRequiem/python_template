from os import system

files = []


def format():
    for i in files:
        system(f"autopep8 --in-place --aggressive {i}")


if __name__ == "__main__":
    format()
    print("All done!")
