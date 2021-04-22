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


def dec2bin(num, digit):
    zero = "000000000000"
    num = num.replace("x", "")
    num = int(num)
    if num >= 0:
        num = bin(int(num))
        num = num.replace("0b", "")
        num = zero[0:digit - len(num)] + num
        return num
    else:
        num = bin(int(num))
        num = num.replace("-", "")
        num = num.replace("0b", "")
        num = zero[0:digit - len(num)] + num
        num=findTwoscomplement(num)
        return num


# Function to find two's complement
def findTwoscomplement(str):
    n = len(str)

    # Traverse the string to get first
    # '1' from the last of string
    i = n - 1
    while (i >= 0):
        if (str[i] == '1'):
            break

        i -= 1

    # If there exists no '1' concatenate 1
    # at the starting of string
    if (i == -1):
        return '1' + str

    # Continue traversal after the
    # position of first '1'
    k = i - 1
    while (k >= 0):

        # Just flip the values
        if (str[k] == '1'):
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)

        k -= 1

    # return the modified string
    return str


def riscv2machine(opcode):
    # R_type,add,sub,sll,slt,sltu,xor,srl,sra,or,and,
    if (opcode[0] == "add") or (opcode[0] == "sub") or (opcode[0] == "sll") \
            or (opcode[0] == "slt") or (opcode[0] == "sltu") or (opcode[0] == "xor") \
            or (opcode[0] == "srl") or (opcode[0] == "sra") or (opcode[0] == "or") \
            or (opcode[0] == "and"):
        return r_type(opcode)

    # I_type,addi,slti,sltiu,xori,ori,andi,slli,srli,srai,
    elif (opcode[0] == "addi") or (opcode[0] == "slti") or (opcode[0] == "sltiu") \
            or (opcode[0] == "xori") or (opcode[0] == "ori") or (opcode[0] == "andi") \
            or (opcode[0] == "slli") or (opcode[0] == "srli") or (opcode[0] == "srai"):
        return i_type(opcode)

    # S_type,lb,lh,lw,lbu,lhu,sb,sh,sw
    elif (opcode[0] == "lb") or (opcode[0] == "lh") or (opcode[0] == "lw") \
            or (opcode[0] == "lbu") or (opcode[0] == "lhu") or (opcode[0] == "sb") \
            or (opcode[0] == "sh") or (opcode[0] == "sw"):
        return s_type(opcode)


def r_type(opcode):
    # R_type,add,sub,sll,slt,sltu,xor,srl,sra,or,and,
    if opcode[0] == "add":
        return "0000000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) \
               + "000" + dec2bin(opcode[1], 5) + "0110011"
    elif opcode[0] == "sub":
        return "0100000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) \
               + "000" + dec2bin(opcode[1], 5) + "0110011"
    elif opcode[0] == "sll":
        return "0000000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) \
               + "001" + dec2bin(opcode[1], 5) + "0110011"
    elif opcode[0] == "slt":
        return "0000000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) \
               + "010" + dec2bin(opcode[1], 5) + "0110011"
    elif opcode[0] == "sltu":
        return "0000000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) \
               + "011" + dec2bin(opcode[1], 5) + "0110011"
    elif opcode[0] == "xor":
        return "0000000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) \
               + "100" + dec2bin(opcode[1], 5) + "0110011"
    elif opcode[0] == "srl":
        return "0000000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) \
               + "101" + dec2bin(opcode[1], 5) + "0110011"
    elif opcode[0] == "sra":
        return "0100000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) \
               + "101" + dec2bin(opcode[1], 5) + "0110011"
    elif opcode[0] == "or":
        return "0000000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) \
               + "110" + dec2bin(opcode[1], 5) + "0110011"
    elif opcode[0] == "and":
        return "0000000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) \
               + "111" + dec2bin(opcode[1], 5) + "0110011"


def i_type(opcode):
    # I_type,addi,slti,sltiu,xori,ori,andi,slli,srli,srai,
    if opcode[0] == "addi":
        return dec2bin(opcode[3], 12) + dec2bin(opcode[2], 5) + "000" \
               + dec2bin(opcode[1], 5) + "0010011"
    elif opcode[0] == "slti":
        return dec2bin(opcode[3], 12) + dec2bin(opcode[2], 5) + "010" \
               + dec2bin(opcode[1], 5) + "0010011"
    elif opcode[0] == "sltiu":
        return dec2bin(opcode[3], 12) + dec2bin(opcode[2], 5) + "011" \
               + dec2bin(opcode[1], 5) + "0010011"
    elif opcode[0] == "xori":
        return dec2bin(opcode[3], 12) + dec2bin(opcode[2], 5) + "100" \
               + dec2bin(opcode[1], 5) + "0010011"
    elif opcode[0] == "ori":
        return dec2bin(opcode[3], 12) + dec2bin(opcode[2], 5) + "110" \
               + dec2bin(opcode[1], 5) + "0010011"
    elif opcode[0] == "andi":
        return dec2bin(opcode[3], 12) + dec2bin(opcode[2], 5) + "111" \
               + dec2bin(opcode[1], 5) + "0010011"
    elif opcode[0] == "slli":
        return "0000000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) + "001" \
               + dec2bin(opcode[1], 5) + "0010011"
    elif opcode[0] == "srli":
        return "0000000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) + "101" \
               + dec2bin(opcode[1], 5) + "0010011"
    elif opcode[0] == "srai":
        return "0100000" + dec2bin(opcode[3], 5) + dec2bin(opcode[2], 5) + "101" \
               + dec2bin(opcode[1], 5) + "0010011"


def s_type(opcode):
    # S_type,lb,lh,lw,lbu,lhu,sb,sh,sw
    if opcode[0] == "lb":
        return dec2bin(opcode[2], 12) + dec2bin(opcode[3], 5) \
               + "000" + dec2bin(opcode[1], 5) + "0000011"
    elif opcode[0] == "lh":
        return dec2bin(opcode[2], 12) + dec2bin(opcode[3], 5) \
               + "001" + dec2bin(opcode[1], 5) + "0000011"
    elif opcode[0] == "lw":
        return dec2bin(opcode[2], 12) + dec2bin(opcode[3], 5) \
               + "010" + dec2bin(opcode[1], 5) + "0000011"
    elif opcode[0] == "lbu":
        return dec2bin(opcode[2], 12) + dec2bin(opcode[3], 5) \
               + "100" + dec2bin(opcode[1], 5) + "0000011"
    elif opcode[0] == "lhu":
        return dec2bin(opcode[2], 12) + dec2bin(opcode[3], 5) \
               + "101" + dec2bin(opcode[1], 5) + "0000011"
    elif opcode[0] == "sb":
        return dec2bin(opcode[2], 12)[1:8] + dec2bin(opcode[1], 5) \
               + dec2bin(opcode[3], 5) + "000" + dec2bin(opcode[2], 12)[7:12] \
               + "0100011"
    elif opcode[0] == "sh":
        return dec2bin(opcode[2], 12)[1:8] + dec2bin(opcode[1], 5) \
               + dec2bin(opcode[3], 5) + "001" + dec2bin(opcode[2], 12)[7:12] \
               + "0100011"
    elif opcode[0] == "sw":
        return dec2bin(opcode[2], 12)[1:8] + dec2bin(opcode[1], 5) \
               + dec2bin(opcode[3], 5) + "010" + dec2bin(opcode[2], 12)[7:12] \
               + "0100011"


code = open("code.txt", "r")
list_of_code = get_code(code)  # get risc-v_code
for i in range(len(list_of_code)):
    machine_code = riscv2machine(list_of_code[i])
    if machine_code is not None:
        #print(list_of_code[i])
        print(machine_code)
    elif (len(list_of_code[i]) == 5) and (machine_code is None):
        temp = list_of_code[i][0]
        list_of_code[i][0] = list_of_code[i][1]
        list_of_code[i][1] = list_of_code[i][2]
        list_of_code[i][2] = list_of_code[i][3]
        list_of_code[i][3] = list_of_code[i][4]
        list_of_code[i][4] = temp
        machine_code = riscv2machine(list_of_code[i])
        #print(list_of_code[i])
        print(machine_code)
    elif (len(list_of_code[i]) is not 5) and (machine_code is None):
        print("Not supported!")
