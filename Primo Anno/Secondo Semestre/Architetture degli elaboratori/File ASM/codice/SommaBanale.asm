#realizzerò un programma che esegue un operazione aritmetica tra 4 numeri
.data

.text

main:	
	addi $s1,$zero,4 #inizializzo le variabili/registri, inserendoci una costante (va sommata a 0)
	addi $s2,$zero,3
	addi $s3,$zero,9
	addi $s4,$zero,4

	sub $t0,$s1,$s2 #inseriamo dentro una variabile temporale t0 la sottrazione fra due  valori
	sub $t1,$s3,$s4
	add $s0,$t1,$t0 #alla fine sommiamo dentro s0 le due nostre variabili temporali
