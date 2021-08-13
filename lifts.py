import random

directions = ["", "U", "D"]

f = str(random.randint(0, 20)) + random.choice(directions)
lifts_current_position = []
for i in range(5):
    pos = random.randint(0, 20)
    if pos == 0:
        direction = ["U", ""]
        lifts_current_position.append(str(pos) + random.choice(direction))
    elif pos == 20:
        direction = ["D", ""]
        lifts_current_position.append(str(pos) + random.choice(direction))
    else:
        lifts_current_position.append(str(pos) + random.choice(directions))

print(lifts_current_position)

cur_pos = input("Enter a request? ")
cur_direction = cur_pos[-1]
cur_pos = cur_pos[:-1]

closest = None
diff = None
for i in range(len(lifts_current_position)):
    lift = lifts_current_position[i]
    if lift.isnumeric():
        if lift == cur_pos:
            closest = i + 1
            diff = 0
            break
        else:
            tmp = abs(int(lift) - int(cur_pos))
            if diff:
                if tmp < diff:
                    diff = tmp
                    closest = i + 1
            else:
                diff = tmp
                closest = i + 1
    else:
        lift_direction = lift[-1]
        if lift_direction == cur_direction:
            lift_pos = lift[:-1]
            if lift_pos == cur_pos:
                closest = i + 1
                diff = 0
                break
            elif lift_pos < cur_pos and lift_direction != "D":
                tmp = abs(int(lift_pos) - int(cur_pos))
                if diff:
                    if tmp < diff:
                        diff = tmp
                        closest = i + 1
                else:
                    diff = tmp
                    closest = i + 1

print(f'Lift #{closest} will be coming to receive you.')

