import turtle
import pandas
correct = 0
screen = turtle.Screen()
screen.title("Guess Nepali Districts")
screen.addshape("nepal77.gif")
turtle.shape("nepal77.gif")
screen.setup(width=1050, height=600)
data = pandas.read_csv("new_districts.csv")


# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)


guessed_set = set()
all_districts = data.Districts.to_list()
while correct <= 76:
    answer_district = screen.textinput(title=f"{correct}/77 Districts Correct",
                                       prompt="Whats the next district of Nepal?").lower()
    if answer_district == "exit":
        not_got = [district for district in all_districts if district not in guessed_set]
        break
    if answer_district in all_districts and answer_district not in guessed_set:
        guessed_set.add(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.speed("fastest")
        t.penup()
        t.goto(200,200)
        t.speed("slow")
        t.pendown()
        district_data = data[data.Districts == answer_district]
        t.goto(int(district_data.X_COR), int(district_data.Y_COR))
        t.write(answer_district)
        correct += 1


dict_helper = {
    "Districts You Missed": not_got
}
dict_to_csv = pandas.DataFrame(dict_helper)
dict_to_csv.to_csv("Districts_to_read.csv")
