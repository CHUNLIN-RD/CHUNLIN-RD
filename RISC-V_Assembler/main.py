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
    zero = "00000000000000000000000000000000"
    if type(num) is not int:
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
        num = findTwoscomplement(num)
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


def riscv2machine(opcode, list_of_label):
    # R_type,add,sub,sll,slt,sltu,xor,srl,sra,or,and,
    if (opcode[0] == "add") or (opcode[0] == "sub") or (opcode[0] == "sll") \
            or (opcode[0] == "slt") or (opcode[0] == "sltu") or (opcode[0] == "xor") \
            or (opcode[0] == "srl") or (opcode[0] == "sra") or (opcode[0] == "or") \
            or (opcode[0] == "and"):
        return r_type(opcode)

    # I_type,addi,slti,sltiu,xori,ori,andi,slli,srli,srai,
    elif (opcode[0] == "addi") or (opcode[0] == "slti") or (opcode[0] == "sltiu") \
            or (opcode[0] == "xori") or (opcode[0] == "ori") or (opcode[0] == "andi") \
            or (opcode[0] == "slli") or (opcode[0] == "srli") or (opcode[0] == "srai") \
            or (opcode[0] == "lui"):
        return i_type(opcode)

    # S_type,lb,lh,lw,lbu,lhu,sb,sh,sw
    elif (opcode[0] == "lb") or (opcode[0] == "lh") or (opcode[0] == "lw") \
            or (opcode[0] == "lbu") or (opcode[0] == "lhu") or (opcode[0] == "sb") \
            or (opcode[0] == "sh") or (opcode[0] == "sw"):
        return s_type(opcode)

    # beq,bne,blt,bge,bltu,bgeu
    elif (opcode[0] == "beq") or (opcode[0] == "bne") \
            or (opcode[0] == "blt") or (opcode[0] == "bge") or (opcode[0] == "bltu") \
            or (opcode[0] == "bgeu"):
        return b_type(opcode, list_of_label)
    # jal, jalr, auipc
    elif (opcode[0] == "jal") or (opcode[0] == "jalr") or (opcode[0] == "auipc"):
        return j_type(opcode)

    elif len(opcode) == 5:
        temp = opcode[0]
        opcode[0] = opcode[1]
        opcode[1] = opcode[2]
        opcode[2] = opcode[3]
        opcode[3] = opcode[4]
        opcode[4] = temp
        return riscv2machine(opcode, list_of_label)

    elif len(opcode) == 4:
        temp = opcode[0]
        opcode[0] = opcode[1]
        opcode[1] = opcode[2]
        opcode[2] = opcode[3]
        opcode[3] = temp
        return riscv2machine(opcode, list_of_label)
    # elif len(opcode) is not 5:
    #     return "Not supported!"


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
    # I_type,addi,slti,sltiu,xori,ori,andi,slli,srli,srai,lui
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
    elif opcode[0] == "lui":
        return dec2bin(opcode[2], 20)[0:20] + dec2bin(opcode[1], 5) \
               + "0110111"


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


def j_type(opcode):
    # jal, jalr, auipc
    if opcode[0] == "jal":
        imm = dec2bin(opcode[2], 20)
        return imm[0] + imm[9:19] + imm[9] + imm[1:8] + dec2bin(opcode[1], 5) + "1101111"
    elif opcode[0] == "jalr":
        imm = dec2bin(opcode[2], 12)
        return imm + dec2bin(opcode[2], 5) + "000" + dec2bin(opcode[1], 5) + "1100111"
    elif opcode[0] == "auipc":
        imm = dec2bin(opcode[2], 32)
        return imm[0:20] + dec2bin(opcode[1], 5) + "0010111"


def b_type(opcode, list_of_label):
    offset = 0
    for i in range(len(list_of_label)):
        if opcode[3] == list_of_label[i][0].replace(":", ""):
            offset = dec2bin(list_of_label[i][1], 13)
    # beq,bne,blt,bge,bltu,bgeu
    if opcode[0] == "beq":
        return offset[0] + offset[1:7] + dec2bin(opcode[2], 5) + dec2bin(opcode[1], 5) \
               + "000" + offset[8:12] + offset[1] + "1100011"
    elif opcode[0] == "bne":
        return offset[0] + offset[1:7] + dec2bin(opcode[2], 5) + dec2bin(opcode[1], 5) \
               + "001" + offset[8:12] + offset[1] + "1100011"
    elif opcode[0] == "blt":
        return offset[0] + offset[1:7] + dec2bin(opcode[2], 5) + dec2bin(opcode[1], 5) \
               + "100" + offset[8:12] + offset[1] + "1100011"
    elif opcode[0] == "bge":
        return offset[0] + offset[1:7] + dec2bin(opcode[2], 5) + dec2bin(opcode[1], 5) \
               + "101" + offset[8:12] + offset[1] + "1100011"
    elif opcode[0] == "bltu":
        return offset[0] + offset[1:7] + dec2bin(opcode[2], 5) + dec2bin(opcode[1], 5) \
               + "110" + offset[8:12] + offset[1] + "1100011"
    elif opcode[0] == "bgeu":
        return offset[0] + offset[1:7] + dec2bin(opcode[2], 5) + dec2bin(opcode[1], 5) \
               + "111" + offset[8:12] + offset[1] + "1100011"


def Find_label(list_of_code):
    temp = []
    n = 0
    offset = 0
    tem_offset = 0
    for i in range(len(list_of_code)):
        if (list_of_code[i][0] == "add") or (list_of_code[i][0] == "sub") or (list_of_code[i][0] == "sll") \
                or (list_of_code[i][0] == "slt") or (list_of_code[i][0] == "sltu") or (list_of_code[i][0] == "xor") \
                or (list_of_code[i][0] == "srl") or (list_of_code[i][0] == "sra") or (list_of_code[i][0] == "or") \
                or (list_of_code[i][0] == "and") or (list_of_code[i][0] == "addi") or (
                list_of_code[i][0] == "slti") or (list_of_code[i][0] == "sltiu") \
                or (list_of_code[i][0] == "xori") or (list_of_code[i][0] == "ori") or (list_of_code[i][0] == "andi") \
                or (list_of_code[i][0] == "slli") or (list_of_code[i][0] == "srli") or (list_of_code[i][0] == "srai") \
                or (list_of_code[i][0] == "lui") or (list_of_code[i][0] == "lb") or (list_of_code[i][0] == "lh") or (
                list_of_code[i][0] == "lw") \
                or (list_of_code[i][0] == "lbu") or (list_of_code[i][0] == "lhu") or (list_of_code[i][0] == "sb") \
                or (list_of_code[i][0] == "sh") or (list_of_code[i][0] == "sw") or (list_of_code[i][0] == "beq") or (
                list_of_code[i][0] == "bne") \
                or (list_of_code[i][0] == "blt") or (list_of_code[i][0] == "bge") or (list_of_code[i][0] == "bltu") \
                or (list_of_code[i][0] == "bgeu") or (list_of_code[i][0] == "jal") or (list_of_code[i][0] == "jalr") \
                or (list_of_code[i][0] == "auipc"):
            n += 1
    if n is not len(list_of_code):
        label = [[] * 2] * (len(list_of_code) - n)
        n = 0
        for i in range(len(list_of_code)):
            if (list_of_code[i][0] != "add") and (list_of_code[i][0] != "sub") and (list_of_code[i][0] != "sll") \
                    and (list_of_code[i][0] != "slt") and (list_of_code[i][0] != "sltu") and (
                    list_of_code[i][0] != "xor") \
                    and (list_of_code[i][0] != "srl") and (list_of_code[i][0] != "sra") and (list_of_code[i][0] != "or") \
                    and (list_of_code[i][0] != "and") and (list_of_code[i][0] != "addi") and (
                    list_of_code[i][0] != "slti") and (list_of_code[i][0] != "sltiu") \
                    and (list_of_code[i][0] != "xori") and (list_of_code[i][0] != "ori") and (
                    list_of_code[i][0] != "andi") \
                    and (list_of_code[i][0] != "slli") and (list_of_code[i][0] != "srli") and (
                    list_of_code[i][0] != "srai") \
                    and (list_of_code[i][0] != "lui") and (list_of_code[i][0] != "lb") and (
                    list_of_code[i][0] != "lh") and (list_of_code[i][0] != "lw") \
                    and (list_of_code[i][0] != "lbu") and (list_of_code[i][0] != "lhu") and (list_of_code[i][0] != "sb") \
                    and (list_of_code[i][0] != "sh") and (list_of_code[i][0] != "sw") and (
                    list_of_code[i][0] != "beq") and (list_of_code[i][0] != "bne") \
                    and (list_of_code[i][0] != "blt") and (list_of_code[i][0] != "bge") and (
                    list_of_code[i][0] != "bltu") \
                    and (list_of_code[i][0] != "bgeu") and (list_of_code[i][0] != "jal") and (
                    list_of_code[i][0] != "jalr") \
                    and (list_of_code[i][0] != "auipc"):
                temp = []
                temp.append(list_of_code[i][0])
                temp.append(i)
                label[n] = temp
                n += 1

        for i in range(len(label)):
            tem_offset = label[i][1]
            count = 0
            for j in range(len(list_of_code)):

                if (label[i][1] is not j) and (len(list_of_code[j]) == 4) and (label[i][0] == list_of_code[j][3] + ":"):
                    offset = label[i][1] - j
                    label[i][1] = offset * 4
                    count = 1
                elif (label[i][1] is not j) and (len(list_of_code[j]) == 5) and (
                        label[i][0] == list_of_code[j][4] + ":"):
                    offset = label[i][1] - j
                    label[i][1] = offset * 4
                    count = 1
            if count == 0:
                label[i][1] = "missing label"
        return label


code = open("code.txt", "r")
list_of_code = get_code(code)  # get risc-v_code

list_of_label = Find_label(list_of_code)
# num = len(list_of_label)
# print(list_of_label)
# print(num)
for i in range(len(list_of_code)):
    machine_code = riscv2machine(list_of_code[i], list_of_label)
    print(machine_code)
# print(list_of_code)
