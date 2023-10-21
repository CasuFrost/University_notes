.globl main

.data

	A : .half 0x5BE1,0xA5FF,0x002A
	parityWord : .half
	L : 3
.text
main:
	la $a0, A
	lb $a1,L
	
	
	
parity:
	.eqv adr,$s0
	.eqv indice,$s1
	li indice,0
	move adr,$a0
	cycle:
		lh $a0,(adr)
		beq indice,$a1,end
		
		
		
		srl $t2, $a0,1
		xor $a0,$a0,$t2
		
		li $v0,1
		syscall
		
		li $v0,11
		li $a0,'\n'
		syscall
		
		addi indice,indice,1
		addi adr,adr,2
		j cycle
		
	end:
	

	
	