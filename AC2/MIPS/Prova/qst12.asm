.text
.globl teste
teste:
li $v0, 4		#comando 4 do syscall
la $a0, str0		#"Nesse programa voce tera que digitar 3 numeros (int)\n"
syscall
addi $t0,$zero,0x1001
sll $t0,$t0,16		#end base = 0x10010000
addi $t7,$zero,0x1001
sll $t7,$t7,16
addi $t1,$zero,1	#t1 = 1
do:
sw $t1,0($t0)		#1 = A[0]
addi $t0,$t0,0x0004
addi $t1,$t1,2		#t1 = t1 + 2
bne $t1,101,do		#se(t1 != 101)go to DO
fase:
lw $t4,0($t7)		#t4 = A[0]	
addi $t7,$t7,0x0004	#next endereço
add $t3,$t3,$t4		#t3 = t3 + A[endereço]
bne $t4,99,fase		#se(t4 != 99)go to FASE
sw $t3,0($t7)
.data
