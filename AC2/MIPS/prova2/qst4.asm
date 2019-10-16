.text
.globl main
main:
li $v0, 4		#comando 4 do syscall
la $a0, str01		#"digite o valor em fahrenheit"
syscall
li $v0, 5		#comando 5 do syscall
syscall
la $t0, ($v0)		#t8 recebe quantidade de elementos a usar no vetor
sub $t0,$t0,32
addi $t1,$zero,5
addi $t2,$zero,9
mult $t0,$t1
mflo $t8
div $t8,$t2
mflo $t7
mfhi $t6
li $v0, 4		#comando 4 do syscall
la $a0, str02		#"O valor em Celsius vale: "
syscall
li $v0, 1
la $a0,($t7)
syscall
li $v0, 4		#comando 4 do syscall
la $a0, str03		#"."
syscall
li $v0, 1
la $a0,($t6)
syscall

.data
str01: .asciiz "Digite o valor em fahrenheit: "
str02: .asciiz "O valor em Celsius vale: "
str03: .asciiz "."
