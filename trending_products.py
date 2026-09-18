filename = "trending_p.txt"
try:
    with open(filename, "x") as file:
        pass
except FileExistsError:
    pass
def trend_p():
    with open(filename, "r") as file:
        file.read()
    