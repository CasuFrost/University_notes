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

##########################################
## INSERIRE IL CODICE QUI

	jal contaOccorrenze
	move $a0,$v0
	li $v0,1
	syscall
	
	li $a0,'\n' #il carattere per andare a capo
	li $v0,11   #il selettore per stampare un char
	syscall
	
	move $a0,$v1
	li $v0,1
	syscall	
	
	li $v0,10 #FINE PROGRAMMA
        syscall   #FINE PROGRAMMA
        
contaOccorrenze:
li $v0,0 #inizializzo il contatore dei divisibili per 2 a 0
li $v1,0 #inizializzo il contatore dei divisibili per 4 a 0
	move $s0,$a0 #userò $s0 come indirizzo della stringa
	
	while:
	lb $a0,($s0) #carico in $a0 il byte corrente
	beq $a0,0xA,end #Se il byte corrente è uguale a '\n', la stringa è terminata e finisco il ciclo
	addi $s0,$s0,1 #mi sposto al byte successivo
	
	
	subi $a0,$a0,0x30 #trasformo il carattere numerico da ascii ad intero
	beqz $a0,while #Se il numero è 0, non va controllato e ricomincio il ciclo
	andi $t0,$a0,3 #Se l'and tra il numero controllato e 3 è uguale a 0, il numero è DIVISIBILE per 4
	beqz $t0,divisibilePer4 
	andi $t0,$a0,1 #Se l'and tra il numero controllato e 1 è uguale a 0, il numero è DIVISIBILE per 2
	beqz $t0,divisibilePer2
	j while
	
	divisibilePer4: #Se divisibile per 4, è anche divisibile per 2
	addi $v0,$v0,1 #Aumento il counter dei divisibili per 2
	addi $v1,$v1,1 #Aumento il counter dei divisibili per 4
	j while
	
	divisibilePer2:
	addi $v0,$v0,1 #Aumento il counter dei divisibili per 2
	j while #ricomincio il cilco
	
	
	
end:
	jr $ra #Una volta finito, torno all'indirizzo dalla quale è stata chiamata la funzione
	
	
	
	
