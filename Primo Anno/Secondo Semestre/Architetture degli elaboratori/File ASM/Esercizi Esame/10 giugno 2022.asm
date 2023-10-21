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
	
    jal contaOccorrenze #Chiamo la funzione contaOccorrenze (in $a0 ho l'indirizzo della stringa)
    
   
    move $a0,$v0 #Devo stampare il counter degli 0, quindi metto in $a0, il valore contenuto in $v0
    li $v0,1 #per stampare un intero
    syscall
    
    li $a0,'\n' #il carattere per andare a capo
    li $v0,11 #per stampare un char
    syscall
    
    move $a0,$v1  #Devo stampare il counter degli 1, quindi metto in $a0, il valore contenuto in $v1
    li $v0,1 #per stampare un intero
    syscall
    
    li $v0,10 #FINE PROGRAMMA
    syscall   #FINE PROGRAMMA

##########################################
## INSERIRE IL CODICE QUI

contaOccorrenze:
	li $v0,0 #Inizializzo il contatore degli zero, a 0
	li $v1,0 #Inizializzo il contatore degli uno, a 0
	move $s0,$a0 #sposto In $s0 l'indirizzo della stringa in input
	
	loop: #ciclo di iterazione per contare

	lb $a0,($s0) #carico il byte corrente della stringa in input dentro $a0
	beq $a0,0,end #Se tale byte corrisponde a 0 (come valore ascii) , siamo alla fine della stringa
	addi $s0,$s0,1 #Mi sposto al byte successivo
	
	beq $a0,48,zeroDetected #Se il byte controllato è 0 (valore ascii = 48)
	beq $a0,49,oneDetected  #Se il byte controllato è 1 (valore ascii = 49)
	
	zeroDetected:
		addi $v0,$v0,1 #Sommo contatore degli 0
		j continue
	oneDetected:
		addi $v1,$v1,1 #Sommo contatore degli 1
		j continue
		
	continue:
	j loop #rieseguo il ciclo
	
	end:
	subi $v0,$v0,1 #La funzione, conta uno 0 in più, quindi va sottratto
        jr $ra #Una volta finito, torno all'indirizzo dalla quale è stata chiamata la funzione
        
        
       


