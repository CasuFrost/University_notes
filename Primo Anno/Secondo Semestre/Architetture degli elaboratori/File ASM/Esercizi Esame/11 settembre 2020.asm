.globl main

.data
M : .word 1,1,4,2,2
N : .byte 7

.text
main:
la $a0,M
lb $a1,N
jal sommaContaUgualiPrec

move $a0,$v0
li $v0,1
syscall

li $v0,11
li $a0,'\n'
syscall

move $a0,$v1
li $v0,1
syscall

li $v0,10 #FINE PROGRAMMA
syscall   #FINE PROGRAMMA

sommaContaUgualiPrec:
	li $v0,0
	li $v1,0
	move $s1,$a1 #lunghezza array
	subi $s1,$s1,1 #mi servirà controllare se il contatore è uguale a len(array) - 1 
	move $s0,$a0 #s0 conterrà l'indirizzo
	lw $t0,($s0) #t0 sarà l'elemento precedente
	li $t2,0 #t2 sarà il counter
	addi $s0,$s0,4 #mi preparo a controllare il prossimo elemento
	
	while:
		beq $t2,$s1,endCycle #se il contatore è uguale a len(array) - 1, finisco il ciclo
		lw $t1,($s0) #carico in t1 l'elemento corrente

		bne $t0,$t1,continue #se esso è uguale all'elemento precedente, eseguo l'aggiornamento di v0 e v1
		add $v0,$v0,$t1
		addi $v1,$v1,1
		
		continue:
		addi $t2,$t2,1 #aumento il contatore di 1
		addi $s0,$s0,4 #mi sposto all'elemento successivo (si trova 4 byte dopo)
		move $t0,$t1  #l'elemento corrente diventa l'elemento precedente per la prossima iterazione
		j while

	endCycle:
		jr $ra
		
