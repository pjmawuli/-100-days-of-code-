import turtle
import data_csv
import writer

# Creating all needed objects
screen = turtle.Screen()

# making the background of the screen the states image
image = "blank_states_img.gif"
turtle.addshape(image)
us_map = turtle.Turtle()
us_map.shape(image)

# The writer object to handle placing texts
writer = writer.Writer()

count = 0   # count to keep track of the correct answers
correct_answers = []
while len(correct_answers) < 50:

    answer_state = screen.textinput(f"{count}/{len(data_csv.states)} Correct Answers", "Guess another state? ")
    answer_state = answer_state.title()

    if answer_state in data_csv.states:
        correct_answers.append(answer_state)
        count += 1

        answer_position = data_csv.states[answer_state]
        writer.write_text(answer_position, answer_state)


screen.exitonclick()
