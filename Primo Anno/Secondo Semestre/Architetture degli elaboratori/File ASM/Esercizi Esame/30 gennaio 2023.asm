##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: Marco
# Cognome: Casu
# Matricola: (assente perchè condividerò questo file)
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

    la $a2, output
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI

move $t9,$a2

jal codificaOttale



move $s0,$v0
#jal bl 

move $a0,$s0
li $v0,1
syscall
jal bl 

move $a0,$v1
li $v0,1
syscall
jal bl 

li $t0,0
li $t1,9
cycle:
	beq $t0,$t1,fin
	
	lb $a0,($t9)
	li $v0,1
	syscall
	
	addi $t0,$t0,1
	addi $t9,$t9,4
	j cycle

fin:
li $v0,10
syscall



codificaOttale:
	li $v0,0
	li $v1,1
	li $s1,0 #lo useremo come counter, per controllare che cifra di ogni terzetto stiamo vedendo
	li $s2,0 #lo useremo come contenitore per ogni cifra ottale
	move $s0,$a0 #Userò s0 come indirizzo
	
	while:
		lb $t0,($s0)
		beq $t0,0xA,end
		
		#in t0 ho il byte corrente
		
		
		bne $t0,49,continue
		#Controllo se va sommato 4,2 o 1
		beq $s1,2,somma1
		beq $s1,1,somma2
		beq $s1,0,somma4
		j continue
		somma4:
			addi $s2,$s2,4
			j continue
		somma2:
			addi $s2,$s2,2
			j continue
		somma1:
			addi $s2,$s2,1
			j continue
		
		continue:
		bne $s1,2,endLoop
			addi $v1,$v1,1
			li $s1,-1
			sb $s2,($a2)
			addi $a2,$a2,4
			
			li $s2,0
			
		endLoop:
		addi $s0,$s0,1
		addi $s1,$s1,1
		j while
	end :
		beq $s1,0,carica0
		li $v0,1
		sb $s2,($a2)
		#subi $v1,$v1,1
		#move $a0,$s2
		#syscall
		jr $ra
		
		carica0:
		subi $v1,$v1,1
		#addi $v1,$v1,1
		li $v0,0
		jr $ra



bl : 
li $v0,11
li $a0,'\n'
syscall
jr $ra





