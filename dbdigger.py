import sys

class Lol:
    def __init__(a):
        pass
    def show(this):
        s = "Reciepe name: " + this.name + "\n"
        s += "Time: " + this.time + "\n"
        s += "Cuisine: " + this.cuisine + "\n"
        s += "Type of meal: " + this.type + "\n"
        s += "Number of servings: " + str(this.servings) + "\n"
        s += "Ingredients:\n"
        for item in this.ingredients:
            s += "\t" + item + "\n"
        s += "Steps:\n"
        for i, item in enumerate(this.steps):
            s += "\t" + str(i + 1) + ": " + item + "\n"

        return s

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
    obj.time = f.readline().split(' ')[1].split(')')[0]
    obj.servings = int(f.readline().split(')')[0][-1:])
    buf = f.readline()
    cuisine = ""
    while "cuisine" in buf:
        cuisine += buf.split('\'')[3] + ', '
        buf = f.readline()
    obj.cuisine = cuisine.rstrip(", ")
    cuisine = ""
    while "mealType" in buf:
        cuisine += buf.split('\'')[3] + ', '
        buf = f.readline()
    obj.type = cuisine.rstrip(", ")
    while "step" not in buf:
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
    first = False
    for arg in sys.argv:
        if not first:
            first = True
            continue
        search += arg + " "
    search = search.rstrip()
    if search.isdigit():
        sindex = int(search)
result = []
if sindex > -1:
    result.append((0, recipes[sindex]))
else:
    for i, r in enumerate(recipes):
        if search in r.name or search in r.cuisine or search in r.type or not search:
            result.append((i, r))

if len(result) == 1:
    i, r = result[0]
    print(r.show())
else:
    for i, r in result:
        print(i, ":", r.name)

f.close()
