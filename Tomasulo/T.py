import colorama
from colorama import Fore, Style


def get_code(code):
    list_of_code = []
    for line in code:
        stripped_line = line.strip()
        stripped_line = stripped_line.replace(",", " ")
        stripped_line = stripped_line.replace("(", " ")
        stripped_line = stripped_line.replace(")", " ")
        line_list = stripped_line.split()
        list_of_code.append(line_list)
    # print(list_of_code)
    return list_of_code


def print_cycle(cycle, print_add, print_mul):
    print()
    print(Fore.YELLOW + 'CYCLE: ' + Style.RESET_ALL, cycle, end='\n')
    print('    __ RF __')
    print('', RF[0][0], ' | ', RF[0][1], ' |')
    print('', RF[1][0], ' | ', RF[1][1], ' |')
    print('', RF[2][0], ' | ', RF[2][1], ' |')
    print('', RF[3][0], ' | ', RF[3][1], ' |')
    print('', RF[4][0], ' | ', RF[4][1], ' |')
    print('    --------', end='\n\n')
    print('    __ RAT __')
    print('', RAT[0][0], ' | ', RAT[0][1], ' |')
    print('', RAT[1][0], ' | ', RAT[1][1], ' |')
    print('', RAT[2][0], ' | ', RAT[2][1], ' |')
    print('', RAT[3][0], ' | ', RAT[3][1], ' |')
    print('', RAT[4][0], ' | ', RAT[4][1], ' |')
    print('    ---------', end='\n\n')
    print('    __ RS _________________')
    print('', RS[0][0], ' | ', RS[0][1], ' | ', RS[0][2], ' | ', RS[0][3], ' | ')
    print('', RS[1][0], ' | ', RS[1][1], ' | ', RS[1][2], ' | ', RS[1][3], ' | ')
    print('', RS[2][0], ' | ', RS[2][1], ' | ', RS[2][2], ' | ', RS[2][3], ' | ')
    print('    -----------------------', end='\n\n')
    print(Fore.GREEN + 'BUFFER:' + Style.RESET_ALL, '(', print_add[0], ') ', print_add[1], end='\n\n')
    print('    _______________________')
    print('', RS[3][0], ' | ', RS[3][1], ' | ', RS[3][2], ' | ', RS[3][3], ' | ')
    print('', RS[4][0], ' | ', RS[4][1], ' | ', RS[4][2], ' | ', RS[4][3], ' | ')
    print('    -----------------------', end='\n\n')
    print(Fore.GREEN + 'BUFFER:' + Style.RESET_ALL, '(', print_mul[0], ') ', print_mul[1], end='\n\n')


def To_main(list_of_code, RF, RAT, RS, buffer_add, buffer_mul):
    total_len = len(list_of_code)  # total execute times
    print_add = ['empty', '']
    print_mul = ['empty', '']
    if total_len == 0:
        print('No code!')
        return
    code_for_exe = list_of_code
    next_code = []
    finish = 0
    cycle = 1
    for i in range(total_len):  # renaming sign
        if code_for_exe[i][0] == "ADD":
            code_for_exe[i][0] = '+'
        elif code_for_exe[i][0] == "ADDI":
            code_for_exe[i][0] = '+'
            code_for_exe[i][3] = int(code_for_exe[i][3])
        elif code_for_exe[i][0] == "SUB":
            code_for_exe[i][0] = '-'
        elif code_for_exe[i][0] == "SUBI":
            code_for_exe[i][0] = '-'
            code_for_exe[i][3] = int(code_for_exe[i][3])
        elif code_for_exe[i][0] == "MUL":
            code_for_exe[i][0] = '*'
        elif code_for_exe[i][0] == "DIV":
            code_for_exe[i][0] = '/'
    print(code_for_exe)

    while finish != 1:

        next_code = []
        rs_use = -1
        if code_for_exe:
            if (code_for_exe[0][0] == '+') or (code_for_exe[0][0] == '-'):
                for v2 in range(3):
                    if RS[v2][1] == '':
                        rs_use = v2
                        next_code = code_for_exe[0]
                        del code_for_exe[0]
                        break
            elif (code_for_exe[0][0] == '*') or (code_for_exe[0][0] == '/'):
                for v3 in range(3, 5):
                    if RS[v3][1] == '':
                        rs_use = v3
                        next_code = code_for_exe[0]
                        del code_for_exe[0]
                        break
        print('code_for_exe: ', code_for_exe)
        # Dispatch

        # adder
        for v10 in range(3):
            if (type(RS[v10][2]) != str) and (type(RS[v10][3]) != str):
                if RS[v10][1] == '+':
                    buffer_add[0] = RS[v10][0]
                    buffer_add[1] = (RS[v10][2]) + (RS[v10][3])
                    RS[v10][1] = RS[v10][2] = RS[v10][3] = ''
                    break
                elif RS[v10][1] == '-':
                    buffer_add[0] = RS[v10][0]
                    buffer_add[1] = (RS[v10][2]) - (RS[v10][3])
                    RS[v10][1] = RS[v10][2] = RS[v10][3] = ''
                    break
        # mul
        for v11 in range(3, 5):
            if (type(RS[v11][2]) != str) and (type(RS[v11][3]) != str):
                if RS[v11][1] == '*':
                    buffer_mul[0] = RS[v11][0]
                    buffer_mul[1] = (RS[v11][2]) * (RS[v11][3])
                    RS[v11][1] = RS[v11][2] = RS[v11][3] = ''
                    break
                elif RS[v11][1] == '/':
                    buffer_mul[0] = RS[v11][0]
                    buffer_mul[1] = (RS[v11][2]) / (RS[v11][3])
                    RS[v11][1] = RS[v11][2] = RS[v11][3] = ''
                    break
        print_add[0] = buffer_add[0]
        print_mul[0] = buffer_mul[0]
        print_add[1] = buffer_add[1]
        print_mul[1] = buffer_mul[1]
        print('buffer_add:', buffer_add)
        print('buffer_mul: ', buffer_mul)

        # write_buffer,capture
        if buffer_add[0] != 'empty':
            for v4 in range(5):
                if RAT[v4][1] == buffer_add[0]:
                    RAT[v4][1] = ''
                    RF[v4][1] = buffer_add[1]
                    buffer_add[0] = 'empty'
                    buffer_add[1] = ''
                    break
            for v5 in range(3):
                for v6 in range(2, 4):
                    if buffer_add[0] == RS[v5][v6]:
                        RS[v5][v6] = buffer_add[1]
            buffer_add[0] = 'empty'
            buffer_add[1] = ''
        elif buffer_mul[0] != 'empty':
            for v7 in range(5):
                if RAT[v7][1] == buffer_mul[0]:
                    RAT[v7][1] = ''
                    RF[v7][1] = buffer_mul[1]
                    buffer_mul[0] = 'empty'
                    buffer_mul[1] = ''
                    break
            for v8 in range(3, 5):
                for v9 in range(2, 4):
                    if buffer_mul[0] == RS[v8][v9]:
                        RS[v8][v9] = buffer_mul[1]
            buffer_mul[0] = 'empty'
            buffer_mul[1] = ''

        # issue
        if next_code:
            for x in range(2, 4):
                for y in range(5):
                    if (type(next_code[x]) is str) and (next_code[x] == RAT[y][0]) and (RAT[y][1] != ''):
                        next_code[x] = RAT[y][1]
                        break
            for v in range(2, 4):
                for b in range(5):
                    if (type(next_code[v]) is str) and (next_code[v] == RF[b][0]) and (RF[b][1] != ''):
                        next_code[v] = RF[b][1]
                        break
            print(next_code)  # next_code in int
            # put into RS,update RAT
            RS[rs_use][1] = next_code[0]
            RS[rs_use][2] = next_code[2]
            RS[rs_use][3] = next_code[3]
            for v1 in range(5):
                if RAT[v1][0] == next_code[1]:
                    RAT[v1][1] = RS[rs_use][0]
                    break

        # print_cycle---------------------------------------------------------------------------------------------------
        # print_cycle(cycle, print_add, print_mul)
        # finish_check--------------------------------------------------------------------------------------------------
        if (RAT[0][1] == '') and (RAT[1][1] == '') and (RAT[2][1] == '') and (RAT[3][1] == '') and (RAT[4][1] == '') \
                and (RS[0][1] == '') and (RS[1][1] == '') and (RS[2][1] == '') and (RS[3][1] == '') and \
                (RS[4][1] == '') and (code_for_exe == []):
            finish = 1
        else:
            cycle += 1

        if finish == 0:
            cycle_print = cycle - 1
            print_cycle(cycle_print, print_add, print_mul)
        elif finish == 1:
            print_add = ['empty', '']
            print_mul = ['empty', '']
            print_cycle(cycle, print_add, print_mul)
            return
        # --------------------------------------------------------------------------------------------------------------


# main------------------------------------------------------------------------------------------------------------------
# setting
RF = [['F1', 0], ['F2', 2], ['F3', 4], ['F4', 6], ['F5', 8]]
RAT = [['F1', ''], ['F2', ''], ['F3', ''], ['F4', ''], ['F5', '']]
RS = [['RS1', '', '', ''], ['RS2', '', '', ''], ['RS3', '', '', ''], ['RS4', '', '', ''], ['RS5', '', '', '']]
buffer_add = ['empty', '']
buffer_mul = ['empty', '']
code = open("code.txt", "r")
list_of_code = get_code(code)  # get risc-v_code
# for i in range(len(list_of_code)):
#     print(list_of_code[i])

To_main(list_of_code, RF, RAT, RS, buffer_add, buffer_mul)
# print_cycle()
