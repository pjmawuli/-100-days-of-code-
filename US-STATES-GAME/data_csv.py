# this module handles the data needed by the game
import turtle
import pandas

# changing the csv file to a dataframe object
data = pandas.read_csv("50_states.csv")
# print(data)

print(data["x"][0])

# here's a dictionary that works
states = {}
for index in range(len(data)):
    state = data["state"][index]
    state_x = data["x"][index]
    state_y = data["y"][index]
    states[state] = (state_x, state_y)

print(states)
