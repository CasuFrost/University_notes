.globl main

.data
	matrice : .word 1,2,3,4,5,6,7,8,9,10
	prova : .float 0.14
.text
main:
	li $t1,8
	lw $t5,matrice($t1)
	
	li $v0,2
	lwc1 $f12,prova
	syscall