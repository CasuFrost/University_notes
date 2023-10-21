##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Marco
# Cognome: Casu
# Matricola: (assente perchè condividerò questo file)
##########################################

# NON MODIFICARE QUESTA PARTE
.data
    buffer: .space 20

.text

main:
    li $v0, 8       # Codice per input stringa
    la $a0, buffer  # Carica indirizzo base in $a0
    li $a1, 20      # Alloca al massimo 20 caratteri
    syscall         # $a0 contiene l'indirizzo base della stringa
    
    jal contaOccorrenze
    	
    move $a0,$v0
    li $v0,1
    syscall
    
    
    li $a0,'\n'
    li $v0,11
    syscall
    	
    li $v0,1
    move $a0,$v1
    syscall
	
    li $v0,10 #FINE PROGRAMMA
    syscall   #FINE PROGRAMMA
    
##########################################
## INSERIRE IL CODICE QUI
contaOccorrenze:

	lb $t1,($a0) #il valore precedente
	li $v1,0 #inizializzo a 0
	li $v0,0 #inizializzo a 0
	beq $t1,0xA,end #Se il primo valore è \n, il programma va subito terminato
	
	
	subi $t1,$t1,0x30 #trasformo il valore in intero
	move $v1,$t1 # $v1 conterrà la somma di valori
	
	
	addi $a0,$a0,1 #Avendo controllato il primo byte, comincio dal byte successivo
	
	while:
	
	lb $t0,($a0) #Carico il byte corrente in $t0
	addi $a0,$a0,1 #passo al prossimo byte
	beq $t0,0xA,end #Se il byte corrente è \n, il programma va  terminato
	subi $t0,$t0,0x30  #trasformo il valore in intero
	bne $t0,$t1,continue #Se il byte controllato (in $t0) ed il byte precedente (in $t1) sono uguali, non farò nessuna somma
	addi $v0,$v0,1 #la sopra-citata somma per il counter dei valori che si ripetono
	
	continue:
	
	add $v1,$v1,$t0 # a prescindere, devo fare la somma di tutti i valori
	move $t1,$t0 #sposto il byte corrente nel registro del byte precedente (per il prossimo ciclo)
	
	
	j while
	
	end:
	jr $ra





	
