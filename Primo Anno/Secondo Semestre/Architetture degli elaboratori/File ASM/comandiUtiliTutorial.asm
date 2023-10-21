.globl main


.data
#le variabili si definiscono cos�:
#nome : .tipo valore

uno : .word 1
quattro : .word 4
float : .float 3.14 #Definisco una variabile di tipo float
string : .asciiz "ciao"  #Definisco una stringa
outputLoop : .asciiz "sono entrato nel while"
outputExit : .asciiz "sono uscito dal while"
accapo : .asciiz "\n"  #Definisco una stringa che utilizzer� per andare accapo
.text

main:
la $a0,string #dentro $a0 crico la stringa da stampare
li $v0,4  #dentro $v0 ci va un intero che seleziona il tipo di syscall da eseguire
syscall #chiamo la syscall, dato che in $v0 c'� 4, stamper� una stringa

la $a0,accapo 
syscall

lwc1 $f12,float #carico in f12 con "load word coprocessor 1" il float
li $v0,2  #Se in $v0 c'� 2, la syscall stamper� il float in $f12
syscall

lw $t0,quattro
lw $t1,uno

while:
#bge vuol dire bigger greater equal, e funziona cos� :
# bge $t0, $t1, et
#se $t0 � maggiore o uguale a $t, il codice salta all'etichetta et
bge $t1,$t0,end  #Se il primo argomento ($t1) � maggiore o uguale al secondo ($t0), salta all'etichetta end
la $a0,outputLoop 
li $v0,4  
syscall

end:
la $a0,outputExit 
li $v0,4  
syscall
