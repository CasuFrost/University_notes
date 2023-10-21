.data
matrice2D: .word 0:400
dim: .word 20

.text
# ind + [z*(x*y) + y *x+x]  matrice a 3 dimensioni
main:
li $t0, 0 
li $t1, 0 
li $t2, 0
lw $t3, dim
cicloRighe:
bge $t1, $t3, fine
cicloColonne:
bge $t0, $t3, nextRiga
bne $t0, $t1, continua
mul $t4, $t1, $t3
add $t4, $t4, $t0
sll $t4, $t4, 2
lw $t4, matrice2D($t4)
add $t2, $t4, $t2
continua:
addi $t0,$t0,1
j cicloColonne
nextRiga:
li $t0,0
addi $t1,$t1,1
j cicloRighe
fine:
move $a0, $t2
li $v0,1
syscall
li $v0,10
syscall