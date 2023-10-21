.globl main
.data
.text
main:
	li $a0,2  #preparo il primo argomento della funzione
	li $a1,5 #preparo il secondo argomento della funzione
	jal potenza #chiamo la funzione, avrò il risultato in $v1
	
	move $a0,$v0 #sposto il risultato in $a0, argomento di stampaIntero
	jal stampaIntero   #stampo il risultato
	
	li $v0,10 #FINE PROFGRAMMA
	syscall	  #FINE PROFGRAMMA


stampaIntero :
	li $v0,1
	syscall
	jr $ra
	
potenza:
	#in $a0 il numero da elevare
	#in $a1 l'elevazione
	#in $v0 il risultato
	li $t1,1 #variabile temporale nella quale salverò il risultato
	loop:  #eseguo il numero per se stesso, tante volte quanto è il numero di elevazione
		beqz $a1,end
		mul $t1,$t1,$a0
		subi $a1,$a1,1
		j loop
	end:
		move $v0,$t1 #sposto il risultato in $t1
		li $t1,0 #resetto $t1
		jr $ra