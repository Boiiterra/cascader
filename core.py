from sys import argv


def err(code: int, msg: str):
    print(f"- [ERROR no.{code}]: {msg}")
    exit(code)


if not len(argv[1:]):
    err(7, "No file provided. Please do: python core.py <file to parse>\n"
        "File must have values like this:\n"
        "\t\t1 2 3 4\n\t\t4 3 2 9")

try:
    from module import parse
except ImportError:
    err(69, "No module.py with function `parse` found."
        "Function parse takes in whole parsed line, e.g `1 2 3 4`\n"
        "and returns single value for better display.")


filename = argv[1]
if not filename.endswith(".txt"):
    err(228, "Invalid file extension provided."
             "Expected `txt` got something else.")

with open(filename) as file:
    data = file.read().split("\n")[:-1]

for ind, line in enumerate(data):
    print(ind + 1, ") ", ", ".join(line.split()),
          ", result: ", parse(line), sep="")
