.globl main

.data 
	buffer : .space 20
	
.text 
main:
	li $v0, 8       # Codice per input stringa
   	la $a0, buffer  # Carica indirizzo base in $a0
   	li $a1, 26      # Alloca al massimo 24 caratteri + \n + \0
   	syscall         # $a0 contiene l'indirizzo base della stringa
 	jal contaOccorrenze
 	
 	move $a0,$v0
 	li $v0,1
 	syscall
 	
 	li $v0,11
 	li $a0,'\n'
 	syscall
 	
 	move $a0,$v1
 	li $v0,1
 	syscall
 	
 	li $v0,10
 	syscall
 
contaOccorrenze:
	.eqv adr,$t0
	move adr,$a0
	.eqv contatoreCifre,$t1
	.eqv offsetCifra,$t2
	.eqv sommaTemporanea,$t3
	.eqv sommaFinale,$t4
	.eqv byteCorrente,$t5
	
	cycle:
	lb byteCorrente,(adr)
	beq byteCorrente,0xA,end #Se leggo \n finisco
	subi byteCorrente,byteCorrente,48
	addi contatoreCifre,contatoreCifre,1 #Conto una cifra
	beq offsetCifra,1,nonMoltiplicare #Se è la prima cifra delle due, va moltiplicata per 10
	mul byteCorrente,byteCorrente,10 #moltiplico per 10 la cifra a sinistra
	nonMoltiplicare:
	add sommaTemporanea,byteCorrente,sommaTemporanea #sommo la coppia corrente
	beq offsetCifra,1,AggiungiCifra #Se siamo alla seconda cifra, devo sommare alla somma finale
	j continue
	AggiungiCifra:
		li offsetCifra,-1 #dato che lo sommo a prescindere con 1, qui va settato a -1 per far si che valga 0 al prossimo ciclo
		add sommaFinale,sommaTemporanea,sommaFinale #aggiorno la somma finale
		li sommaTemporanea,0 #resetto la somma temporanea della coppia
	continue:
	addi offsetCifra,offsetCifra,1 #passo alla prossima cifra della coppia
	addi adr,adr,1 #passo al prossimo byte della stringa
	j cycle
	end:
	move $v0,sommaFinale
	
	div sommaTemporanea,sommaTemporanea,10
	add $v0, $v0,sommaTemporanea
	
	move $v1,contatoreCifre
	jr $ra
	
	
	
	
	
	
	