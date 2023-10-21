.globl main
.data
	Matrix : .byte 1,9,3,8,2,3,4,5,6,7,9,8,1,4,3,9
	L : 16
	rows : 4
.text
main:
	.eqv mat,$s0
	.eqv len,$s1
	.eqv col,$s2
	.eqv row,$s3
	.eqv offsetRiga,$s4
	.eqv index,$s5
	.eqv somma,$s6
	.eqv indexDaSommare,$s7
	li indexDaSommare,0
	li index,0
	li offsetRiga,0
	la mat, Matrix #Carico variabile
	lb len, L	#Carico variabile
	lb row,rows	#Carico variabile
	subi row,row,1
	
	#Se dovessimo immaginare la matrice a 2 dimensioni con coordinate x,y offsetRiga mi terrà conto della coordinata x del byte corrente
	#Andrà quindi ogni volta aumentata di 1, e poi resettata quando passo alla prossima riga
	#Invece indexDaSommare terrà conto della coordinata y. Quando x=y, ossia indexDaSommare
	#e  offsetRiga sono uguali, vuol dire che ci troviamo sulla diagnoale, e quel valore va sommato dentro somma (ossia $s6)
	
	cycle: beq index,len,end #Inizio a scorrere la matrice (terminerò quando sarà giunto all'ultimo valore)
	lb $a0,(mat) #Carico in $a0 il byte corrente
	
	
	
	bne offsetRiga,indexDaSommare,notSum #Se non siamo sulla diagonale, non dobbiamo sommare il byte corrente 
	add somma,somma,$a0
	
	notSum: 
	bne offsetRiga,row,continue # Se ci troviamo all'ultimo elemento della riga, dobbiamo aumentare la colonna e resettare le righe 
	li offsetRiga,-1 #Resetto la x = -1 dato che a prescindere la sommo a fine ciclo, quindi per la prossima iterazione varrà 0
	addi indexDaSommare,indexDaSommare,1 #incremento la y
	
	continue:
	addi offsetRiga,offsetRiga,1 #Incremento la x
	addi mat,mat,1 #Passo al prossimo elemento della matrice
	addi index,index,1 #Tengo conto dell'indice dell'elemento
	j cycle
	end:
	
	move $a0,somma #Stampo la somma
	li $v0,1
	syscall
	
	
	
	
	
	
	
	