.data
vettore: 	.word 11, 35, 2, 17, 29, 95
N:		    .word 6
.text
	lw	$t0, vettore($zero)	# max → $t0
	lw	$t1, N		     	# N → $t1
	li	$t2, 1			    # i = 1
for:
	bge	$t2, $t1, endFor
	sll	$t3, $t2, 2		# i*4
	lw	$t4, vettore($t3)	# el. = vettore[i]
	ble	$t4, $t0, else		# if (el >= max)
	move	$t0, $t4		# max = el.
else:
	addi	$t2, $t2, 1		# i++
	j for
endFor:
