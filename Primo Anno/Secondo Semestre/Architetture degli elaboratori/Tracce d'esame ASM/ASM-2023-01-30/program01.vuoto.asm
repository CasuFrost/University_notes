##########################################
# INSERIRE I PROPRI DATI QUI
# Nome: 
# Cognome:
# Matricola:
##########################################

# NON MODIFICARE IL CODICE DA QUI...
.data
    buffer: .space 26
    output: .byte  0,0,0,0,0,0,0,0,0  # Un carattere extra per la fine della stringa
    aa : .asciiz "AA"
.text

main:
    li $v0, 8       # Codice per input stringa
    la $a0, buffer  # Carica indirizzo base in $a0
    li $a1, 26      # Alloca al massimo 24 caratteri + \n + \0
    syscall         # $a0 contiene l'indirizzo base della stringa
    
    
    
    li $v0,4
    syscall
    li $t1,30
    beq $a0,30,end
    j end2
    
    
    la $a2, output
    end:
    la $a0,aa
    syscall
    end2:
# ... A QUI

##########################################
## INSERIRE IL PROPRIO CODICE QUI
