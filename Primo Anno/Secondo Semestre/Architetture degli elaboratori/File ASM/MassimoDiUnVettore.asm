.globl main
.data
vettore : .word 11,4,7,9,40,99,1,5,78,119,5,2,1,44,15
len : .word 15
messaggioIniziale : .asciiz "Questo programma si occupa di analizzare un vettore e restituirne il suo massimo"
messaggioFinale : .asciiz "Il massimo del vettore è : "
messaggioMeme : .asciiz "\n Funzione chiamata "
bl : .asciiz "\n"

finalMessage: .asciiz "il massimo del vettore è : "
linea : .asciiz " - "



.text

main:
	li $v0,4
	la $a0,messaggioIniziale
	syscall
	la $a0,bl
	syscall
	li $v0,1
	.eqv max,$t0 #Chiamo "max" il registro $t0
	lw max,vettore($zero)
	.eqv index,$t1 #Chiamo "index" il registro $t1
	.eqv tmpValue,$t3
	.eqv checker,$t4
	lw $t2,len
	li index,0
	lw $t6,len
	
	while:
		mul $t5,index,4
		lw $t3,vettore($t5)
		add $a0,$t3,$zero
		li $v0,1
		syscall
		
		#Controlla se il temporaneo è maggiore del massimo, se si scambia i due valori
		slt checker,max,$t3 #Se max < $t3, checker = 1
		beq checker,1,scambia
		
		
		addi index,index,1
		li $v0,4
		la $a0,linea
		syscall
		beq index,$t6,end
		j while
		
		scambia:
		beq index,$t6,end
		addi index,index,1
		li $v0,4
		la $a0,linea
		syscall
		#Metti $t3 dentro max
		move max,$t3
		beq index,$t6,end
		j while
		
	end:
	li $v0,4
	la $a0,bl
	syscall
	la $a0,finalMessage
	syscall
	li $v0,1
	move $a0,max
	syscall
	

	
	
	
	
