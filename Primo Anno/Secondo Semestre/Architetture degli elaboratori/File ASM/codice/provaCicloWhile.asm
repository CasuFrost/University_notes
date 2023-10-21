.globl main

.data
vector  : .word 1,4,6,2,1,6,9
N  : .word 10
cnt : .word 1

.text
main:
lw $t0,N
lw $t2,cnt

do:

slti $t1,$t0,5
beq $t1,$t2,endWhile
subi $t0,$t0,1 
j do
endWhile:
lw $t4,999




