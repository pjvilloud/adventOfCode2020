"""
--- Day 12: Rain Risk ---
Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?

Your puzzle answer was 1294.

--- Part Two ---
Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

For example, using the same instructions as above:

F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?

Your puzzle answer was 20592.
"""
input_test = """F10
N3
F7
R90
F11"""

input = """W1
F91
W3
F82
N1
E2
N4
R90
F25
N2
F75
E4
R90
F91
R90
F64
L90
E1
L90
S2
L180
S2
E3
N2
E5
L90
N2
R90
F30
L90
N1
F37
S1
E5
F3
E2
F59
W3
L270
S5
W5
S4
F84
N5
R180
E4
F31
L90
E2
F77
L90
N5
F17
N4
N4
W2
F45
S1
F92
E1
F33
L270
F21
L90
E1
F81
N5
F20
E2
R90
N4
W3
L180
S2
F33
E5
F87
R90
N2
F29
E3
S4
L90
E4
R90
S2
F65
L90
F69
W2
N4
F73
R180
S3
R90
N3
R90
W1
L180
F96
N3
W2
L180
S5
F29
E3
S4
W1
F53
E1
L90
E5
F26
E3
R270
E2
S2
W2
F43
W2
F53
F74
R180
N5
W3
S4
F70
R90
W4
F56
L90
S5
R180
E4
S4
F80
S1
F91
R90
S4
F88
L90
S5
R90
E2
S1
F37
N1
R90
F92
W5
F14
N2
E5
S2
F89
L180
N4
E4
L90
F32
E4
R90
F99
N3
L180
F78
S1
R270
W1
F11
S4
F47
N4
L90
F17
R90
E4
S3
F14
S1
R90
N3
F52
W3
S5
L180
F41
R90
F62
W1
R90
E4
F1
W5
F86
W1
N5
F5
S1
E5
F67
W3
F97
E1
L90
S2
E1
R90
F82
E3
N2
F16
L90
W2
F35
R180
N2
E3
N4
W4
F13
S5
E1
S5
L90
E5
F65
E5
L90
S4
E3
W4
N1
R90
N5
F93
R90
S5
R90
L90
F86
E3
F90
E4
N2
E4
R180
W5
R90
E3
F98
F56
L90
F68
L90
N3
F35
S1
W5
F25
L180
F7
R270
F84
R90
S4
E5
S3
L270
F33
W3
R90
W5
N3
E4
R90
W2
F100
E5
S2
L90
F6
E1
L90
S1
F17
N3
E1
S3
F78
R90
W5
N4
L90
F13
W5
R90
F7
F74
R90
E4
F28
L90
S5
R90
F77
S2
E2
N3
F30
E1
R90
W2
S2
F62
E2
L90
E2
F56
L90
F61
S1
F14
W3
F23
L90
E3
S3
L270
S5
F97
E5
S1
F96
W2
F61
L180
F25
L90
W4
F100
W4
F14
W4
S5
R90
F67
E1
R90
F89
W5
S3
W2
N2
F64
L180
S4
R270
F47
E1
S1
E4
N1
R90
N2
E5
F97
N3
E5
S5
R180
E5
F34
L90
W1
W1
N3
R90
F17
N1
F75
S4
W5
N2
W1
N2
L90
W3
N2
F1
N1
W3
R90
F18
E4
N4
F18
N4
F73
W4
F61
W3
R90
N5
L90
N4
F70
E4
F10
L90
F33
N5
L90
W4
L180
E2
F41
E1
S4
E4
L90
F28
N2
W4
S2
F86
R180
S3
W3
S3
W2
F55
W1
F18
W2
F18
L90
S4
W1
L90
F47
L90
S4
F39
N5
L180
S3
W5
F95
W1
R90
E2
N3
L90
S4
F77
S1
W4
S5
E4
R90
W1
R90
W3
W2
N4
F1
W1
N5
F55
E4
N4
W5
L90
F90
E4
R90
E2
R90
S5
F44
N2
E3
R90
F64
W1
L180
L180
F55
L90
F15
S2
E1
R270
F10
R90
W4
F43
E1
F7
N2
W3
F10
N1
L270
N2
L90
E2
R90
F28
W2
N5
F70
R90
E3
E3
F75
W4
L90
S2
R90
F83
L270
E1
F87
R180
N3
L90
F30
L90
E1
N5
F87
N4
R90
F51
W5
N3
R90
S5
F98
W4
N2
E2
L90
E4
S1
E5
F60
N1
L180
E1
F10
R90
W5
F90
W5
F9
S1
W3
F9
E2
S4
L180
F61
W2
N3
F35
R90
E4
N3
W4
L90
E1
L90
S1
F62
S5
W1
N5
L180
F76
W3
L90
W4
L90
N2
E3
N5
E1
N2
F13
S1
F20
W5
L90
S1
F89
S3
L90
W2
L90
F48
W5
N1
R90
F93
L90
E4
L90
N2
F100
W5
S5
W1
S1
E2
S1
W4
R90
S2
F99
W2
F80
L90
F78
N4
L90
F67
S1
L90
F23
W3
N1
W5
F76
R270
F51
L90
W2
N1
E3
S3
L90
F83
L90
F46
S5
L180
N3
E3
F49
E5
N4
W5
L90
E3
R90
S4
F54
E1
F49
N4
L180
E3
L90
R90
F95
W2
N2
F12
R180
E4
R90
N5
L180
S3
W3
S1
F22
W1
F18
L90
F35
R90
F3
S4
L90
F53
W5
F58
L90
S2
F48
S5
R180
F67
L180
W1
S3
L90
F33
F34
R90
F54
W2
L180
S5
W4
R90
F80
W4
S1
W4
F35
E1
F48
N3
L270
F78
N4
S4
F11
S1
W3
L90
W1
F26
R180
E3
F43
S4
R180
W3
N2
F80
W4
F29
W5
W1
R270
N3
L90
F17
W4
F49
S4
S1
F47"""

ordered_cardinals = ["N", "E", "S", "W"]

face = "E"

position_v1 = {
    "N": 0,
    "E": 0,
    "S": 0,
    "W": 0
}

position = {
    "N": 0,
    "E": 0,
    "S": 0,
    "W": 0
}
waypoint_position = {
    "N": 1,
    "E": 10,
    "S": 0,
    "W": 0
}

for instruction in input.splitlines():
    action = instruction[0:1]
    value = int(instruction[1:len(instruction)])
    if action == "L":
        # V1
        face = ordered_cardinals[(ordered_cardinals.index(face) - value / 90) % 4]
        # V2
        ordered_waypoint_position = [waypoint_position["N"], waypoint_position["E"], waypoint_position["S"], waypoint_position["W"]]
        shift_nb = value / 90
        for i in range(shift_nb):
            tmp = ordered_waypoint_position.pop(0)
            ordered_waypoint_position.append(tmp)
        waypoint_position.update({
            "N": ordered_waypoint_position[0],
            "E": ordered_waypoint_position[1],
            "S": ordered_waypoint_position[2],
            "W": ordered_waypoint_position[3],
        })
    elif action == "R":
        # V1
        face = ordered_cardinals[(ordered_cardinals.index(face) + value / 90) % 4]

        # V2
        ordered_waypoint_position = [waypoint_position["N"], waypoint_position["E"], waypoint_position["S"],
                                     waypoint_position["W"]]
        shift_nb = value / 90
        for i in range(shift_nb):
            tmp = ordered_waypoint_position.pop()
            ordered_waypoint_position.insert(0, tmp)
        waypoint_position.update({
            "N": ordered_waypoint_position[0],
            "E": ordered_waypoint_position[1],
            "S": ordered_waypoint_position[2],
            "W": ordered_waypoint_position[3],
        })
    elif action in position.keys():
        opposite_direction = ordered_cardinals[(ordered_cardinals.index(action) + 2) % 4]
        # V1
        value_v1 = value
        opposite_value_v1 = position_v1[opposite_direction]
        if opposite_value_v1 > 0:
            position_v1[opposite_direction] = max(0, opposite_value_v1 - value_v1)
            if position_v1[opposite_direction] == 0:
                value_v1 = abs(opposite_value_v1 - value_v1)
            else:
                value_v1 = 0
        position_v1[action] += value_v1

        # V2
        opposite_value = waypoint_position[opposite_direction]
        if opposite_value > 0:
            waypoint_position[opposite_direction] = max(0, opposite_value - value)
            if waypoint_position[opposite_direction] == 0:
                value = abs(opposite_value - value)
            else:
                value = 0
        waypoint_position[action] += value
    elif action == "F":
        opposite_direction = ordered_cardinals[(ordered_cardinals.index(face) + 2) % 4]
        # V1
        value_v1 = value
        opposite_value_v1 = position_v1[opposite_direction]
        if opposite_value_v1 > 0:
            position_v1[opposite_direction] = max(0, opposite_value_v1 - value_v1)
            if position_v1[opposite_direction] == 0:
                value_v1 = abs(opposite_value_v1 - value_v1)
            else:
                value_v1 = 0
        position_v1[face] += value_v1
        # V2
        for card in waypoint_position.keys():
            value_to_add = value
            waypoint_value = waypoint_position[card]
            if waypoint_value == 0:
                continue
            opposite_direction = ordered_cardinals[(ordered_cardinals.index(card) + 2) % 4]
            opposite_value = position[opposite_direction]
            if opposite_value > 0:
                position[opposite_direction] = max(0, opposite_value - value*waypoint_value)
                if position[opposite_direction] == 0:
                    value_to_add = abs(opposite_value - value*waypoint_value)
                else:
                    value_to_add = 0
            else:
                value_to_add *= waypoint_value
            position[card] += value_to_add

print "The Manhattan Distance for v1 is ", sum(position_v1.values())
print "The Manhattan Distance for v2 is ", sum(position.values())
