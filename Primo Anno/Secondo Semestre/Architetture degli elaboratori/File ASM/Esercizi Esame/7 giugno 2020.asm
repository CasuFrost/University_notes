.globl main

.data
	M : 0,1,2,3,4,5,6,7,8
	lato : .byte 3
	
.text
main:
la $a0,M
lb $a1,lato

jal sommaScacchiera

move $a0,$v0
li $v0,1 
syscall

li $v0,11   #VAI A CAPO
li $a0,'\n'
syscall

li $v0,1 
move $a0,$v1
syscall


li $v0,10
syscall

sommaScacchiera:

	lw $t8,lato
	subi $t8,$t8,1 # in t8 ho lato-1

	move $t0,$a1 #metto in t0 il lato
	mul $t0,$t0,$t0 #eseguirò il ciclo finchè il contatore è minore di t0 (ossia la dimensione della matrice, dato che t0=lato*lato)
	li $t1,0 #t1 è il contatore
	move $s0,$a0 # uso s0 come indirizzo

	li $t3,0 #Colonna corrente
	li $t4,0 #Riga corrente

	li $s6,0 #contatore elementi di riga e colonna pari
	li $s7,0 #contatore elementi di riga e colonna dispari


	while:
		beq $t1,$t0,end #se il contatore è uguale a lato*lato, ho finito di scorrere la matrice
		lb $t2,($s0) #carico in $t2 il valore da controllare
		
		#!REGOLA LOGICA DEI BIT! - se l'AND logico tra x ed 1 è uguale a 0, vuol dire che x è pari.
		andi $t7,$t3,1 #metto in t7, l'AND tra la colonna corrente ed 1
		bnez $t7,colonnaDispari #se il risultato è 0, la colonna corrente è pari, altrimenti dispari
		
		colonnaPari:
		andi $t7,$t4,1 #controllo poi se la riga è pari
		bnez $t7,endCounterOp
		add $s6,$s6,$t2 #colonna e riga sono pari
		j endCounterOp
	
		colonnaDispari: #controllo poi se la riga è dispari
		andi $t7,$t4,1
		beqz $t7,endCounterOp
		add $s7,$s7,$t2 #colonna e riga sono dispari
	
		endCounterOp:
		beq $t3,$t8,prossimaRiga #in t8 ho le dimensioni del lato-1, se la colonna corrente è uguale a t8, dobbiamo scorrere alla prossima riga
		j continue
		prossimaRiga:
		li $t3,-1 #risettiamo la colonna a -1 dato che  a prescindere incrementeremo il numero di colonna ad ogni iterazione
		addi $t4,$t4,1 #aumenta riga

		continue:
		addi $t1,$t1,1 #aumenta contatore 
		addi $t3,$t3,1 #aumenta colonna
		addi $s0,$s0,4 #aumenta indirizzo (il prossimo elemento si trova a 4 byte dal corrente)
		j while

	end:
		#sposto i valori nei loro registri di output
		move $v0,$s6
		move $v1,$s7
		jr $ra 
