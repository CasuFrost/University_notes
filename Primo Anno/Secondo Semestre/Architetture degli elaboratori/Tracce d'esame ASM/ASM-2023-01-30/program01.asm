##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Marco
# Cognome: Casu
# Matricola: xxxxxx
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    buffer: .space 26
    output: .byte  0,0,0,0,0,0,0,0,0  # Un carattere extra per la fine della stringa

.text

main:
    li $v0, 8       # Codice per input stringa
    la $a0, buffer  # Carica indirizzo base in $a0
    li $a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    syscall         # $a0 contiene l'indirizzo base della stringa
    
    
    syscall
    
    
    la $a2, output
    
# ... A QUI
	move $t8,$a2
	jal codificaOttale
	
	j endReal
	
##########################################
codificaOttale:
## INSERIRE IL PROPRIO CODICE QUI
	.eqv byteCorrente,$t0
	.eqv ottaleCorrente,$t1
	.eqv offsetCifra,$t2
	.eqv address,$t3
	.eqv cifreTotaliProdotte,$t4
	move address,$a0
	li offsetCifra,0
	
	cycle:
	lb byteCorrente,(address)
	beq byteCorrente,0xA,end
	beq byteCorrente,48,continue
	beq offsetCifra,0,somma4
	beq offsetCifra,1,somma2
	beq offsetCifra,2,somma1
	
	somma4:
		addi ottaleCorrente,ottaleCorrente,4
		j continue
	somma2:
		addi ottaleCorrente,ottaleCorrente,2
		j continue
	somma1:
		addi ottaleCorrente,ottaleCorrente,1
		j continue
	continue:
	beq offsetCifra,2,storeOctal
	j endCycle
	storeOctal:
		sb ottaleCorrente,($t8)
		addi cifreTotaliProdotte,cifreTotaliProdotte,1
		move $a0,ottaleCorrente #print cifra
		li $v0,1 #print cifra
		syscall  #print cifra
		
		addi $t8,$t8,1
		li offsetCifra,-1
		li ottaleCorrente,0
	endCycle:
	addi offsetCifra,offsetCifra,1
	addi address,address,1
	j cycle
	end:
	
	
	
	beq offsetCifra,0,noSimboliMancanti
	addi cifreTotaliProdotte,cifreTotaliProdotte,1
	move $a0,ottaleCorrente #print cifra
	li $v0,1 #print cifra
	syscall  #print cifra
	sb ottaleCorrente,($a2)
	li $a0,'\n' #Break line
	li $v0,11   #Break line
	syscall     #Break line
	li $t5,1
	li $a0,1 
	li $v0,1 
	syscall
	j next
	noSimboliMancanti:
	li $t5,0
	li $a0,'\n' #Break line
	li $v0,11   #Break line
	syscall     #Break line
	li $a0,0
	li $v0,1 
	syscall

	next:
	li $a0,'\n' #Break line
	li $v0,11   #Break line
	syscall     #Break line

	move $a0,cifreTotaliProdotte #print cifra
	li $v0,1 #print cifra
	syscall  #print cifra

	
	move $v0,$t5
	move $v1,cifreTotaliProdotte
jr $ra
	

endReal:


