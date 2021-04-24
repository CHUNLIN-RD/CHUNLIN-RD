# RISC-V_Assembler

Implementing RISC-V Assembler with Python

### To run the code:

>* Step1: Make an code.txt.
>* Step2: Read the Restrictions.
>* Step3: Run!

### Restrictions:

>* Please only input decimal numbers to I-type instructions.
>* All letters must be lowercase.
>* Branch labels do not allow in a single line.
>* ### Supported type: 
..>- [x] Type-U
>- [X] Type-UJ
>- [X] Type-I
>- [X] Type-S
>- [X] Type-R

### Input:

        sw x27,0(x10)
        bne x2,x2,L2
    L1: sw x1,0(x2)
        addi x24,x24,-1
        beq x2,x2,L1
    L2: lui x2,2
        jalr x0 x1 1
        auipc x0 1
    
### Output:
    
    00000001101101010010000000100011
    00000000001000010001100001100011
    00000000000100010010000000100011
    11111111111111000000110000010011
    11111110001000010000110011100011
    00000000000000000010000100110111
    00000000000100001000000001100111
    00000000000000000000000000010111
