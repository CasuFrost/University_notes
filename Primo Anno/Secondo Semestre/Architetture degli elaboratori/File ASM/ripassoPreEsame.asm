.globl main 					 #verrà eseguito questo programma

.data 						 #qui definirò le mie variabili
	vettore : .word 1,2,3,4,5,6,7,8		 #dichiaro un vettore di 8 valori interi, con "word" si intende una parola di bit 
	vectorLenght : .word 7			#mi salvo in una variabile la lunghezza del vettore
	message : .asciiz "Ciao mondo!" 		 #definisco un messaggio di output
	accapo : .asciiz "\n"
	fineLoop : .asciiz "vettore terminato"
	endProgram : .asciiz "programma terminato"
	
.text 	


					 #da qui in poi si scriverà il nostro programma
main:
	#Vediamo come si stampa un messaggio a schermo :
	la $a0, message  #come prima cosa, carico il messaggio che ho salvate nella variabile "messagge" nel registro $a0, tramite "load address"
	li $v0, 4        #il registro $v0 funge da selettore per le syscall, in base all'intero che gli passiamo, eseguirà un operazione diversa. per stampare una stringa, necessita di 4.
	syscall  #una volta impostati i parametri per la syscall, si può richiamare
	
	la $a0, accapo #Stampo il carattere necessario per andare a capo in console
	syscall
	
	#adesso vediamo come accedere ad un elemento del vettore tramite un indice
	#usiamo $t1 come contenitore del nostro indice (inizialmente uguale a 0)
	li $t1, 0
	#l'elemento del vettore all'indice i si chiama con la keywoard vettore(i)
	lw $a0, vettore($t1) #inserisco nel registro corretto alla stampa, il vettore nell'indice corrente
	li $v0,1 #il selettore deve essere 1 per poter stampare una word
	syscall
	
	#adesso stampiamo il secondo elemento
	#essendo che gli indirizzi sono suddivisi in 4 bit, l'indice andrà di 4 in 4, quindi, bensì ad ogni passo per scorrere il vettore, incrementeremo l'indice di 1
	#sarà necessario chiamare come indice, l'indice tale ma moltiplicato per 3, che terremo in una variabile temporale $t2
	li $t1,1
	mul $t2, $t1, 4 #moltiplichiamo l'indice per 4
	lw $a0, vettore($t2) #inseriamo l'elemento con indice corretto in $a0 per stamparlo
	syscall
	
	add $t1,$t1,1 #Incrementiamo l'indice di 1 e riproviamo
	mul $t2, $t1, 4 #moltiplichiamo l'indice per 4
	lw $a0, vettore($t2) #inseriamo l'elemento con indice corretto in $a0 per stamparlo
	syscall
	
	
	
	la $a0, accapo #Stampo il carattere necessario per andare a capo in console
	li $v0, 4  
	syscall
	
	
	#Adesso, partendo dall'inizio, stamperò tutti i valori del vettore
	
	lw $t4, vectorLenght #Il valore servirà per scorrere tutto il vettore, sarà il limite che il nostro indice dovrà raggiungere
	li $t1, 0
	li $v0, 1
	loop:
		mul $t2, $t1, 4         #Ottengo l'indice corretto moltiplicato per 4
		lw $a0, vettore($t2)   #Carico nel registro che verrà stampato, il vettore nel punto dell'indice corrente
		syscall 			
		beq $t1,$t4,endLoop   #controllo se siamo arrivati alla fine del vettore, se si, salto all'etichetta endLoop
		add $t1,$t1,1        #incremento di 1 l'indice
		j loop 		     #rieseguo l'iterazione con un salto incondizionato all'etichetta loop
	endLoop:
		la $a0, accapo #Stampo il carattere necessario per andare a capo in console
		li $v0, 4  
		syscall
		la $a0, fineLoop
		syscall
	li $v0, 4 
	la $a0, accapo       
	syscall
	la $a0, endProgram 
	syscall
	
	
