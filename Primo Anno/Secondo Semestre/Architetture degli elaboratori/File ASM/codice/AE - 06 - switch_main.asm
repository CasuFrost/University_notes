# Programma ASM (assembly MIPS) che implementa lettura di valori da tastiera da utente e 
# in seguito utente decide se fare somma o prodotto in base ad input 0/1; 
# il risultato è mostrato a video. Nota che non vi e' nessun controllo sulla scelta
# quindi inserire un valore diverso da 0 o 1 nella terza selezone prota il PC a puntare
# ad una parte di codice non corretta e genera un'eccezione che interrompe il programma
# le info sulla eccezione sono nel Coproc 0

.globl main

.data
	switch_case:  .word case_00, case_01
	case_string:  .asciiz "Ran case #: "
	input_question: .asciiz "Input 0 for sum or 1 for multiplication\n"
	address_of_main: .word main #for example of exploit

.text
main:
	jal read_int # Leggi intero
	move $t2,$v0 # mettilo in $t2
	
	jal read_int # Leggi intero
	move $t3,$v0 # mettilo in $t3
	
	la $a0, input_question # ask question
	jal print_string
	
	jal read_int # Leggi caso 0 o 1
	move $t1,$v0
	sll $t0, $t1, 2    				# the index of the case to run points to the address of the line of code
	                   				# so I have to index the mem at location switch_case. Given I have word,
	                   				# the offset is 0,4,8,12...
	lw $s1, switch_case($t0)  # load the corresponding address of case $t0

	la $a0, case_string
	jal print_string          # Print first part of case selected
	
	move $a0,$t1              # Print 0 or 1 case selected
	jal print_rez
	jr $s1             		  # jump to the address loaded in $s1; we go either to case00 or case01
	
case_00:
	# sum
	add $t3,$t3,$t2
	j end_switch
	
case_01:
	# product
	mul $t3,$t3,$t2
	j end_switch
	
end_switch:
	li $a0,0x0A  #10         # 10 is ascii encoding in decimal of '\n' python: int(('\n'.encode('ascii')).hex(),base=16)
	jal print_char
	move $a0,$t3
	jal print_rez
	j exit
