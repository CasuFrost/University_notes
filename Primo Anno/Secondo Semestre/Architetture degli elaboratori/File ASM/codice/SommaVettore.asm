
.data
vector : .word 1,-2,3,-4,5,-6,7,-8,9,-10,11,2
n : .word 5
.text
main:
#Vogliamo sommare al 13esimo valore di un vewettore, la somma tra una variabile n e il 7imo valore di un vettore
la $s5,vector
la $s6,n
lw $t0,24($s5)
lw $t1,($s6)

add $t0,$t1,$t0
sw $t0,48($s5)
