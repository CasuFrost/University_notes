.globl main
.data
	matrix : .word 0:50
	#matrix : .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50
	len : 50
	Nrighe : 5
	Ncolonne : 10
	accapo : .asciiz "\n"
.text
main:
	.eqv matrice,$t5
	lw matrice,matrix
	.eqv counter,$t3
	lw $t1,len
	lw $t4,Ncolonne
	li $t2,0
	loop:
	
	
	jal stampa
	

	beq $t0,$t1,end
	
	mul $t2,$t0,4
	beq counter,$t4,righa
	addi $t0,$t0,1
	addi counter,counter,1
	j loop
	righa:
	jal bl
	li counter,0
	j loop
	
end:
	li $v0,10
	syscall

bl:
	la $a0,accapo
	li $v0,4
	syscall
	jr $ra
stampa:
	lw $a0,matrix($t2)
	li $v0,1
	syscall
	jr $ra
