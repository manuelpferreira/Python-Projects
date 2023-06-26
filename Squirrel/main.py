import pandas

data = pandas.read_csv("info_squirrel.csv")

# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Grey"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

fur_color_list = data["Primary Fur Color"]
gray = 0
red = 0
black = 0

for item in fur_color_list:
    if item == "Gray":
        gray += 1
    elif item == "Cinnamon":
        red += 1
    elif item == "Black":
        black += 1

new_dict = {
    "Fur Colour": ["gray", "cinnamon", "black"],
    "Count": [gray, red, black]
}

df = pandas.DataFrame(new_dict)
df.to_csv("squirrel_count")
