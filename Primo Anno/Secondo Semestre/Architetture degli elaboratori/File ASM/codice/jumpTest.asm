.data
vector : .word 4,3,-5,500
rez:  .word 0
.text

main:
lw $s0,vector
lw $s1,vector+4
lw $s2,vector+8
lw $s3,vector+12

or $s4,$zero,$s0

CheckB:
slt $t0,$s4,$s1
beq $t0,$zero,CheckC
or $s4,$zero,$s1

CheckC:
slt $t0,$s4,$s2
beq $t0,$zero,CheckD
or $s4,$zero,$s2

CheckD:
slt $t0,$s4,$s3
beq $t0,$zero,End
or $s4,$zero,$s3

End:
sw $s4,rez