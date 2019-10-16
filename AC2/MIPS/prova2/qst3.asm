.text
.globl main
main:
li $v0, 4		#comando 4 do syscall
la $a0, str01		#"digite o tanto de valores que quer usar no vetor:"
syscall
li $v0, 5		#comando 5 do syscall
syscall
la $t8, ($v0)		#t8 recebe quantidade de elementos a usar no vetor
addi $t0,$zero,0x1001
sll $t0,$t0,16		#end base = 0x10010000
addi $t7,$zero,0x1001
sll $t7,$t7,16
addi $t1,$zero,1	#t1 = 10
addi $t5,$0,0
addi $t4,$0,0
addi $t2,$0,0
do:
sw $t1,0($t0)		#1 = A[0]
addi $t0,$t0,0x0004
slt $t6,$t5,$t8		#se t5<t8    t6=1
addi $t5,$t5,1		#t5 = t5+1
addi $t1,$t1,2		#t1 = t1 + 2
bne $t5,$t8,do		#se(t6 != t8)go to DO
addi $t5,$0,0
fase:
lw $t3,0($t7)		#t3 = A[0]
addi $t7,$t7,0x0004	#t0 recebe prox endereço
slt $t6,$t5,$t8		#se t5<t8    t6=1
addi $t5,$t5,1		#t5 = t5+1
add $t2,$t2,$t3		#t2 = t2+A[endereço]
bne $t5,$t8,fase	#se(t5 != tamanho)go to FASE
sw $t2,0($t7)
li $v0, 4		#comando 4 do syscall
la $a0, str02		#"digite o tanto de valores que quer usar no vetor:"
syscall
li $v0, 1	#printar um int
la $a0, ($t2)	#a0 recebe valor de t0
syscall

.data
str01: .asciiz "digite o tanto de valores que quer usar no vetor:"
str02: .asciiz "A soma do elementos = "