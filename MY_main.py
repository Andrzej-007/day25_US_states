
import turtle
import pandas as pd
from states import States


data = pd.read_csv("./50_states.csv")

screen = turtle.Screen()
screen.title("US State Game")

image = 'blank_states_img.gif'  # this is not really gif file
screen.addshape('blank_states_img.gif') # this is not really gif file  that's why it doesn't work
screen.bgpic(image)



# guess_state = screen.textinput(title="Guess the State", prompt="what's another state's name",)

data_csv = pd.read_csv("./50_states.csv")
list_all_states = data_csv['state'].to_list()
answers_no = 1

# data = pandas.read_csv("./50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []

while answers_no < len(list_all_states):

    for one_state in list_all_states:
        guess_state = screen.textinput(title=f"Guess the State{answers_no} out of {len(list_all_states)}",
                                       prompt="what's another state's name in America")

        if one_state.lower() == guess_state.lower():
            print('oke doki')
            check_data = data_csv[data_csv['state'] == one_state]
            coordinate_x = int(check_data['x'])  # the same is : int(check_data.x)
            coordinate_y = int(check_data['y'])  # the same is : int(check_data.y)
            coordinates = (coordinate_x, coordinate_y)
            print(f'one_state : {one_state}')
            print(f'coordinates: {coordinates}')
            # states.enter_state(one_state, one_state )
            states = States(one_state, coordinates)
            answers_no += 1
        else:
            print(f'there is no state: {guess_state}')

'''below there is method how to get coordinates for mouse cliking'''
# def get_mouse_coordinates(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_coordinates)


turtle.mainloop()
# screen.exitonclick()