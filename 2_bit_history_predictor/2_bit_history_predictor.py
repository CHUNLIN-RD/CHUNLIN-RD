import colorama
from colorama import Fore, Style
def get_code(input):
    list_of_input = []
    for line in input:
        stripped_line = line.strip()
        list_of_input.append(stripped_line)
    # print(list_of_input)
    return list_of_input

def bit_history_predictor(input, history, list_of_predictor):
    for i in range(len(input)):
        # '00'
        if history[0] == '00':
            k = 0
        elif history[0] == '01':
            k = 1
        elif history[0] == '10':
            k = 2
        elif history[0] == '11':
            k = 3
        temp = history[k + 1]
        list_of_predictor[i] = temp[1:2]
        print(list_of_input)
        print(history)
        print(list_of_predictor)
        if input[i] != list_of_predictor[i]:
            if input[i][0] == 'T':
                if history[k + 1] == 'SN':
                    history[k + 1] = 'WN'
                elif history[k + 1] == 'WN':
                    history[k + 1] = 'WT'
            elif input[i] == 'N':
                if history[k + 1] == 'ST':
                    history[k + 1] = 'WT'
                elif history[k + 1] == 'WT':
                    history[k + 1] = 'WN'
            print(Fore.RED + "Misprediction ! " + Style.RESET_ALL)

        elif input[i] == list_of_predictor[i]:
            if input[i] == 'T':
                if history[k + 1] == 'ST':
                    history[k + 1] = 'ST'
                elif history[k + 1] == 'WT':
                    history[k + 1] = 'ST'
            elif input[i] == 'N':
                if history[k + 1] == 'SN':
                    history[k + 1] = 'SN'
                elif history[k + 1] == 'WN':
                    history[k + 1] = 'SN'
            print(Fore.GREEN + "Prediction ! " + Style.RESET_ALL)

        temp = history[0]
        temp = temp[1:2]
        if input[i] == 'T':
            history[0] = temp + '1'
        elif input[i] == 'N':
            history[0] = temp + '0'
        print()


input_txt = open("input.txt", "r")
list_input = input_txt.read()
list_of_input = get_code(list_input)
list_of_predictor = [''] * len(list_input)
history = ['00', 'SN', 'SN', 'SN', 'SN']
print('input:', end=' ')
print(list_of_input)
print()
bit_history_predictor(list_of_input, history, list_of_predictor)
