.globl main

.data
	x : .word 13
	accapo : .asciiz "\n"
	dist1 : .word 11
	dist2 : .word 99
.text

main:
	.eqv input,$a1
	.eqv input2,$a2
	.eqv output,$v1
	
	lw input,x
	jal funzione
	
	jal stampaOutput
	
	jal bl
	#Adesso scriverò una funzione che calcoli la distanza tra due valori
	lw input,dist1
	
	lw,input2,dist2
	
	jal distanza
	
	jal stampaOutput
	
	li $v0,10 #Questo selettore, fa si che la syscall termini il programma
	syscall
	
funzione: #Questa funzione prende l'argomento in input, e lo somma ad 8, mettendolo in output
	addi input,input,8
	move output,input
	jr $ra
	
stampaOutput :
	move $a0,output
	li $v0,1
	syscall
	jr $ra
	
distanza:
	sub output,input,input2
	ble output,$zero,absolute
	jr $ra
	absolute:
	li $t0,-1
	mul output,output,$t0
	jr $ra
	
bl : 
	li $v0,4
	la $a0,accapo
	syscall
	jr $ra
