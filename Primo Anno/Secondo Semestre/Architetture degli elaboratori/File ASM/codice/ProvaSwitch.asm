.globl main
.data 
dest  : .word caso0,caso1,caso2
.text
main:
li $t0,2
sll $t0,$t0,2
lw $t1,dest($t0)
jr $t1

caso0:
li $s0,1
j endSwitch
caso1:
li $s0,2
j endSwitch
caso2:
li $s0,3
j endSwitch
endSwitch:
