# RISC-V_Assembler

Implementing RISC-V Assembler with Python

### To run the code:

>* Step1: Make an code.txt
>* Step2: Run!

### Limitations:

>* Please only input decimal numbers to I-type instructions
>* All letters must be lowercase
>* Only work with R, S, I type instructions

### Input:

    add x2,x2,x23
    addi x24,x24,2
    sw x27,0(x10)
    sw x1,0(x2)
    addi x24,x24,1
    
### Output:
    
    00000001011100010000000100110011
    00000000001011000000110000010011
    00000001101101010010000000100011
    00000000000100010010000000100011
    00000000000111000000110000010011
