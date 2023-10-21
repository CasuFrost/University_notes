.globl main
.data 
	input : .asciiz "abc"
.text
main:
	#0($v1) caratteri
	#1($v1) numeri
	#2($v1) caratteri speciali
	la $t1, input
	

contaLettere:
	lb $t0,($t1)
	beq $t0,0,end
	
	li $v0,1
	move $a0,$t0
	syscall
	ble $t0,0x2F,carattereSpeciale
	ble $t0,0x39,numero
	ble $t0,0x7A,probLettera
	
	#addi $t1,$t1,1
	#j contaLettere
	
	probLettera:
	bge $t0,0x61,minuscola
	ble $t0,0x5A,maiuscola
	
	
	carattereSpeciale:
	li $v0,11
	li $a0,'s'
	syscall
	addi $t1,$t1,1
	j contaLettere
	
	numero:
	li $v0,11
	li $a0,'n'
	syscall
	addi $t1,$t1,1
	j contaLettere
	
	minuscola:
	li $v0,11
	li $a0,'l'
	syscall
	addi $t1,$t1,1
	j contaLettere
	maiuscola:
	li $v0,11
	li $a0,'l'
	syscall
	addi $t1,$t1,1
	j contaLettere
end:
