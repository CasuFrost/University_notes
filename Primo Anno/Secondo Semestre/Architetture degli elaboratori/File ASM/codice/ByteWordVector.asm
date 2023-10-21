.data
	N : .word 0x01020304
	N2 : .byte 1,2,3,4
.text
lb $t0,N
lb $t1 N+1
lb $t2 N+2
lb $t3 N+3

lw $t4, N

lb $s0,N2
lb $s1 N2+1
lb $s2 N2+2
lb $s3 N2+3

lw $s4, N2