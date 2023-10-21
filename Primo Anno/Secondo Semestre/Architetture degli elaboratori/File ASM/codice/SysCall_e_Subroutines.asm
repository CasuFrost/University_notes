.globl main
.data
string: .asciiz "Hello world"
.text 
main:
li $v0,4
la $a0, string
syscall

#per le subroutines sono importanti queste funzioni : 
#j - jump
#jr jump to register
#jal jump and link

while:
bge $t1,$s7, whileEnd
lw $t2,Array($t1)
add $s0,$s0, $t2
addi $t1,$t1,4
j while
whileEnd: