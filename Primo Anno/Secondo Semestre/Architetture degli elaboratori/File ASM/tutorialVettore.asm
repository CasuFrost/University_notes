.globl main
.data
vettore : .word 1,3,5,6,3,1,4 #definisco un array di 7 elementi
outputExit : .asciiz "Fine programma"
beginMessage : .asciiz "Questo programma stampa tutti gli elementi di un array"
accapo : .asciiz "\n"
len : .word 7 #Mi serve memorizzare in una variabile la lunghezza del nostro array

#è possibile dare nomi/etichette ai registri
.eqv indice $t1 #utilizzo l'etichetta indice per riferirmi al registro £t1
.eqv max $t0 #utilizzo l'etichetta max per riferirmi al registro £t0
.eqv selettoreSyscall $v0 
.text
main:

la $a0,beginMessage 
li selettoreSyscall,4  
syscall
la $a0,accapo 
syscall

lw max,len #In $t0, memorizzo l'indice dell'ultimo elemento
li indice,0 # userò $t1 come indice mentre scorro l'array

mul max,max,4
while: 
bge indice,max,end

lw $a0,vettore(indice) 
li selettoreSyscall,1  
syscall

la $a0,accapo 
li selettoreSyscall,4  
syscall

addi indice,indice,4
j while

end:
la $a0,outputExit 
li selettoreSyscall,4  
syscall
