import sys

class Lol:
    def __init__(a):
        pass
    def show(this):
        s = "Reciepe name: " + this.name + "\n"
        s += "Time: " + this.time + "\n"
        s += "Type of cuisine: " + this.cuisine + "\n"
        s += "Number of servings: " + str(this.servings) + "\n"
        s += "Ingredients:\n"
        for item in this.ingredients:
            s += "\t" + item + "\n"
        s += "Steps:\n"
        for i, item in enumerate(this.steps):
            s += "\t" + str(i + 1) + ": " + item + "\n"

        return s



    # make function to print pretty objects

f = open("../recipe_database.pl")

for i in range(73):
    f.readline()

recipes = []
buf = "lol"
while buf and f.readable():
    obj = Lol()
    f.readline()
    f.readline()
    obj.name = f.readline().split('\'')[3]
    f.readline()
    obj.time = f.readline().split(')')[0][-2:] #to fix time can be 3 digits
    obj.servings = int(f.readline().split(')')[0][-1:])
    obj.cuisine = f.readline().split('\'')[3]
    buf = f.readline()
    steps = []
    while "step" in buf:
        while ')' not in buf:
            buf += f.readline()
        steps.append(buf.split('\'')[3])
        buf = f.readline()
    obj.steps = steps
    while "Quantity" not in buf:
        buf = f.readline()
    ingr = []
    while buf and buf != "\n":
        ingr.append(buf.split('\'')[3])
        buf = f.readline()
    obj.ingredients = ingr
    recipes.append(obj)
    while buf and buf[0] != "%":
        buf = f.readline()

search = ""
sindex = -1
if len(sys.argv) > 1:
    search = sys.argv[1]
    if search.isdigit():
        sindex = int(search)
result = []
if sindex > -1:
    result.append(recipes[sindex])
else:
    for i, r in enumerate(recipes):
        if search in r.name or not search:
            result.append((i, r))

if len(result) == 1:
    print(result[0].show())
else:
    for i, r in result:
        print(i, ":", r.name)

f.close()
