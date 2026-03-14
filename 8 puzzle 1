import time

start = [2,3,0,1,6,4,8,7,5]
goal  = [1,2,3,8,0,4,7,6,5]

# Heuristic function (misplaced tiles)
def h(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count = count + 1
    return count

# Print puzzle
def print_state(state):
    for i in range(9):
        print(state[i], end=" ")
        if (i+1) % 3 == 0:
            print()
    print()

open_list = []
closed_list = []

g = 0
open_list.append((start,g))

while len(open_list) > 0:

    best_index = 0
    best_f = open_list[0][1] + h(open_list[0][0])

    # find state with minimum f(n)
    for i in range(len(open_list)):
        state, cost = open_list[i]
        f = cost + h(state)

        if f < best_f:
            best_f = f
            best_index = i

    current, g = open_list.pop(best_index)

    print("Current State")
    print_state(current)
    time.sleep(1)

    if current == goal:
        print("Goal Reached")
        break

    closed_list.append(current)

    blank = current.index(0)

    moves = [-3,3,-1,1]

    for m in moves:

        new_pos = blank + m

        if new_pos >= 0 and new_pos < 9:

            new = current.copy()

            temp = new[blank]
            new[blank] = new[new_pos]
            new[new_pos] = temp

            if new not in closed_list:

                open_list.append((new, g+1))
