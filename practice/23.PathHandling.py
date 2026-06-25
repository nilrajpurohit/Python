from pathlib import Path
path = Path("../content/demo.csv")

# filename = "demo.txt"
# path = "../content/" + filename

# path = Path("../content") / "demo.csv"
# if path.exists():
#     print("File Found")
# else:
#     print("File Not Found")

print(path.name)
print(path.suffix)
print(path.parent)

# Path("../logs").mkdir(exist_ok=True)
path = Path("../content/fruits.txt")
print(path.read_text())

# path = Path("../content/fruits.txt")
# path.write_text("Mango")

