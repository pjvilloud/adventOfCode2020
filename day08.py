"""
--- Day 8: Handheld Halting ---
Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
For example, consider the following program:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
These instructions are visited in this order:

nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |
First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?

Your puzzle answer was 1675.

--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?

Your puzzle answer was 1532.
"""
input = """acc +14
acc +11
nop +422
acc +14
jmp +443
acc +21
nop +524
acc -2
jmp +279
jmp +1
acc +28
acc +11
jmp +576
acc +32
acc -12
acc -8
jmp +291
nop +542
acc +41
jmp +320
acc +40
jmp +96
jmp +85
acc +38
acc +8
jmp +333
acc +44
nop +231
acc +40
jmp +323
acc +18
jmp +251
acc -1
jmp +385
acc -9
acc +48
acc +20
acc +34
jmp +150
nop +203
acc +4
acc +32
acc +44
jmp +168
acc +26
acc +46
acc +40
jmp -30
jmp +182
acc +18
jmp +404
nop +142
jmp +84
acc +30
acc +10
jmp +1
acc +40
jmp +370
jmp +381
jmp +239
acc -2
acc +47
acc -4
jmp +295
jmp -38
acc +40
acc +44
acc +4
acc +4
jmp +156
acc +31
acc +20
acc +0
acc -12
jmp -48
acc +32
acc +38
jmp +1
acc -6
jmp +375
acc +33
acc +27
acc +28
jmp +107
acc +1
acc +6
nop +136
jmp +85
acc +31
acc +49
acc +46
jmp +167
acc +5
acc -5
jmp +148
acc +22
acc +44
acc -8
acc -2
jmp -60
nop +354
jmp +59
acc +48
nop +473
acc -7
acc +4
jmp +105
jmp +456
acc +16
acc +33
acc +24
jmp -4
acc +36
acc +10
nop +441
jmp +268
jmp +388
acc +0
acc +27
acc -1
jmp -60
nop +90
jmp -90
acc +48
acc +30
jmp +284
acc +4
acc +6
acc +1
acc -10
jmp +95
acc +35
jmp +235
acc +31
acc -19
jmp -96
jmp +326
acc -7
acc +0
acc -1
jmp +53
acc +15
acc -14
jmp +450
nop +8
acc -2
acc -1
acc +17
jmp -25
nop +444
jmp +65
jmp -86
acc +44
acc +16
acc +32
acc -11
jmp +32
acc +14
acc +28
jmp +123
jmp +127
jmp -44
acc +42
acc +24
acc -3
acc +4
jmp +219
acc +28
acc +30
acc -14
acc -11
jmp +67
acc +5
acc +43
acc +23
nop +73
jmp +176
acc +28
acc +8
acc +42
acc +44
jmp +278
acc +9
acc +46
acc +0
acc +30
jmp +72
jmp +317
jmp +352
jmp +273
jmp +137
nop +364
jmp +249
nop +79
jmp +1
jmp -147
acc -10
acc -1
acc +12
acc +27
jmp +147
acc -5
acc +7
jmp +63
acc +33
acc +32
nop +81
jmp -185
acc +44
jmp +215
jmp +187
acc +14
acc +38
jmp -113
jmp +267
acc -9
acc +21
acc -5
jmp +143
nop -57
nop +281
jmp -170
jmp +267
nop -131
jmp -83
acc -6
jmp -95
acc -9
acc -8
jmp +184
acc +32
acc -16
jmp +171
acc +5
acc +22
acc -7
acc +20
jmp +45
acc +48
jmp +239
acc -4
jmp +75
acc -18
jmp -178
nop +349
acc -12
nop +313
jmp -57
acc +7
acc +6
jmp -241
acc +19
jmp +320
acc +13
jmp -61
acc +0
nop +337
jmp +66
acc +27
acc -11
acc -7
jmp +315
acc +23
acc +26
acc -5
jmp +132
acc +45
acc +21
acc -12
jmp +158
acc +19
jmp +176
acc +43
jmp +124
nop +227
nop -236
acc +11
jmp +1
jmp -67
acc +21
jmp +161
jmp +86
acc +26
acc +7
jmp +246
acc +0
jmp +215
jmp +1
acc +16
jmp -257
acc +2
jmp +281
nop -10
acc +46
jmp +124
acc +13
acc +24
jmp +204
jmp +1
acc +23
jmp +225
nop -243
jmp +167
jmp +1
jmp -142
acc -15
jmp -113
acc +27
acc -18
acc +12
jmp -259
nop +74
acc +35
acc +42
acc -4
jmp -166
nop +87
nop +86
acc +18
acc -2
jmp +212
acc -8
jmp -313
acc +36
acc -11
jmp -233
jmp +237
nop +67
acc +16
nop -57
jmp -92
acc +48
acc +2
acc +21
jmp +33
acc -15
jmp +145
acc +26
jmp -254
acc +30
acc +4
acc -1
acc -14
jmp -64
acc +32
acc +8
jmp -131
acc -13
jmp +138
acc +5
acc +4
jmp -4
acc +37
nop -278
acc +28
acc +17
jmp -215
jmp -104
nop -241
jmp -43
jmp -2
acc +5
acc -1
jmp +151
jmp +1
acc +21
jmp +19
acc +40
jmp +91
acc +50
nop +202
acc -12
jmp -333
nop -66
acc +42
acc +7
jmp +1
jmp +47
acc +32
acc +29
acc +42
nop -8
jmp +52
jmp -299
jmp +40
acc +36
acc -5
acc +39
jmp -116
acc +19
acc +30
acc +39
acc -1
jmp -276
jmp -245
acc +6
jmp -185
acc +50
acc +14
acc -7
jmp -325
acc +33
jmp -279
nop +173
acc +15
acc -17
jmp -33
acc +20
jmp -101
acc -17
jmp -335
nop -8
jmp +22
acc +0
acc +4
jmp -133
nop -81
jmp +64
jmp -306
acc -19
acc +31
acc +47
acc +26
jmp +55
jmp -402
acc +13
jmp -375
acc +6
acc -1
acc -6
acc +49
jmp -28
acc -7
jmp -203
jmp -395
acc +5
acc +38
acc +10
jmp +130
jmp +161
jmp -382
acc +45
jmp +113
acc +38
acc +48
acc +46
jmp +126
acc -1
acc -10
acc +4
acc +2
jmp -425
acc +0
jmp -80
acc +4
jmp -202
acc +25
acc +8
jmp -398
jmp -307
acc +3
jmp +17
acc +13
acc +33
acc +7
jmp -381
acc +5
acc +12
jmp -308
jmp +1
acc +3
acc -14
acc +46
jmp -415
acc +31
acc +7
acc +28
jmp -419
jmp -175
jmp +1
jmp -141
acc +20
nop -35
jmp -36
acc -6
jmp +108
nop +1
jmp +8
jmp -49
jmp -389
acc +24
nop -482
acc +41
acc +25
jmp -167
nop -26
jmp -198
nop -199
acc +23
acc -19
jmp -202
jmp +58
acc +3
jmp -237
acc +44
acc +42
acc +22
acc +5
jmp -307
acc +45
nop -418
acc +41
nop -88
jmp +63
acc +12
nop -56
acc -19
jmp +55
acc -13
acc -7
jmp -213
acc +42
jmp -88
acc +20
jmp -115
acc +6
jmp -57
acc +25
acc +49
jmp -43
jmp -322
jmp -456
acc +7
acc +40
acc +35
jmp -518
nop -461
acc +43
acc +33
jmp +7
acc +27
jmp +5
acc -15
acc -19
acc -2
jmp -238
acc +49
acc +48
acc -16
jmp +34
acc -6
acc +49
acc -4
acc +4
jmp +1
acc +35
nop -264
jmp -234
jmp -365
jmp -436
acc +20
acc +36
jmp -426
acc +39
acc +20
jmp -343
nop -443
jmp -325
jmp -127
nop -560
acc +10
jmp -511
jmp -455
acc -16
acc +18
jmp -61
acc +26
jmp -285
jmp +1
nop -397
acc +12
nop -67
jmp -371
acc +27
acc +13
jmp -395
acc +44
jmp -565
acc +1
jmp -21
nop -428
acc -4
jmp -265
acc +48
acc +10
acc +46
jmp -202
acc -4
acc -10
jmp -152
acc +17
acc -10
acc +22
acc +10
jmp +1"""

input_test = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

instructions = input.split("\n")

success = 0


def execute_program():
    global success
    position_of_executed_instruction = list()
    position = 0
    accumulator = 0
    while 1:
        if position >= len(instructions):
            print "Program successfully ended"
            success = 1
            return accumulator
        instruction = instructions[position][0:3]
        argument = instructions[position][4:len(instructions[position])]
        if instruction == "acc":
            accumulator += int(argument)
            position += 1
        elif instruction == "jmp":
            position += int(argument)
        else:
            position += 1
        if position in position_of_executed_instruction:
            print "Infinite loop detected"
            break
        position_of_executed_instruction.append(position)
    return accumulator


accumulator_before_infinite_loop = execute_program()
print "The value in the accumulator before the infinite loop is", accumulator_before_infinite_loop

i = len(instructions) - 2

while 1:
    instr = instructions[i][0:3]
    arg = instructions[i][4:len(instructions[i])]
    if instr == "jmp":
        print "Replacing", instr, arg, "with nop", arg
        instructions[i] = "nop " + arg

    elif instr == "nop":
        print "Replacing", instr, arg, "with jmp", arg
        instructions[i] = "jmp " + arg
    execute_program()
    if success:
        break
    else:
        instructions[i] = instr + " " + arg
    i -= 1

# Replacing second to last jump instruction with no op

accumulator_after_completion = execute_program()

print "The value in the accumulator after program completion is", accumulator_after_completion

