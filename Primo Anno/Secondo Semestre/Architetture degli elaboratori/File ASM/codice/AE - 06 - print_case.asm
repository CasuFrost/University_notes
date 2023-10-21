.globl print_string, read_int, print_rez, print_char, exit

.data
	# Syscall lookup table
	print_s: 		.byte 4
	print_i: 		.byte 1
	read_i: 		.byte 5
	print_c: 		.byte 11
	exit_s: 		.byte 10
	
.text	
print_string:                # cenno ad una procedura
	lb $v0, print_s          # print a string (4 means that)
	syscall
	jr $ra
	
print_rez:
	lb $v0, print_i          # print an integer (1 means that but now is encoded in the lookup table)
	syscall
	jr $ra

read_int:
	lb $v0, read_i
	syscall
	jr $ra

print_char:
	lb $v0, print_c
	syscall
	jr $ra
	
exit:
	lb $v0, exit_s           # Very important: tells the OS to exit the pro
	syscall                  # if we do not add this we may go in infinite loop
