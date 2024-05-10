def print_state(row_array, start_index, end_index):
    print("".join(map(str, row_array[start_index:end_index+1])))

def get_on_switch(current_index_1, end_index_2):
    for current_index_2 in range(end_index_2 - 1, -1, -1):
        if switch_moves[current_index_1][current_index_2] != 0:
            return current_index_2
    return -1

def switch_sequence(total_moves):
    if total_moves == 0:
        return
    elif total_moves == row_switch_num:
        switch_moves[total_switch_num - 1][0] = total_moves
        total_moves -= 1
    elif total_moves == row_switch_num - 1:
        switch_moves[total_switch_num - 2][0] = total_moves
        total_moves -= 1
    elif 0 < total_moves < total_switch_num - 2:
        start = total_moves + 2
        current_index_2D = 0
        while start <= row_switch_num:
            on_switch2 = get_on_switch(start, moving_sequences_num)
            for on_switch2 in range(on_switch2, -1, -1):
                switch_moves[total_moves][current_index_2D] = switch_moves[start][on_switch2]
                current_index_2D += 1
            start += 1

        switch_moves[total_moves][current_index_2D] = total_moves
        for i in range(current_index_2D - 1, -1, -1):
            current_index_2D += 1
            switch_moves[total_moves][current_index_2D] = switch_moves[total_moves][i]
        total_moves -= 1
    switch_sequence(total_moves)

def turn_off_switches():
    global total_basic_operation
    for i in range(1, total_switch_num):
        for j in range(moving_sequences_num):
            if switch_moves[i][j] == 0:
                break
            moving_switch_index = switch_moves[i][j]
            row_switches[moving_switch_index - 1] = not row_switches[moving_switch_index - 1]
            print_state([int(x) for x in row_switches], 0, row_switch_num - 1)
            total_basic_operation += 1

row_switch_num = int(input("Enter the number of switches: "))

def initialize_switches(n):
    return [1] * n

row_switches = initialize_switches(row_switch_num)

total_switch_num = row_switch_num + 1
moving_sequences_num = total_switch_num * 330
switch_moves = [[0] * moving_sequences_num for _ in range(total_switch_num)]
start_index_1d_left_side_array = 1
end_index_1d_right_side_array = total_switch_num
total_basic_operation = 0

switch_sequence(row_switch_num)

print_state(row_switches, 0, row_switch_num - 1)
turn_off_switches()
print("Minimum number of moves:", total_basic_operation)
