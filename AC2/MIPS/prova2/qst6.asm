.text
.globl main
main:
addi $t4,$t4,0		#valor para sair do programa
li $v0, 4		#comando 4 do syscall
la $a0, str01		#"Digite o primeiro valor que será elevado pelo segundo,digite 0 para sair do programa: "
syscall
li $v0, 5		#comando 5 do syscall
syscall
la $t0, ($v0)		#salva em t0 o primeiro valor
beq $t4,$t0,fim		#se valor de um dos 2 for 0 sai do programa
li $v0, 4		#comando 4 do syscall
la $a0, str02		#"Digite o segundo valor: "
syscall
li $v0, 5		#comando 5 do syscall
syscall
la $t1, ($v0)		#salva em t0 o segundo valor
beq $t4,$t1,fim		#se valor de um dos 2 for 0 sai do programa
add $a0,$zero,$t0
add $a1,$zero,$t1
addi $t7,$zero,1
add $t5,$zero,$a0

jal eleva

add $t8,$zero,$v0
li $v0, 4		#comando 4 do syscall
la $a0, str03		#"O primeiro valor elevado ao segundo vale: "
syscall
li $v0, 1		#comando 1 do syscall
la $a0,($t8)		#a0 recebe o valor de t8
syscall
li $v0, 4		#comando 4 do syscall
la $a0, str05		#"digite o tanto de valores que quer usar no vetor:"
syscall
j main

eleva:
mult $a0,$t5
mflo $a0
addi $t7,$t7,1
bne $t7,$a1,eleva
add $v0,$zero,$a0
jr $ra

fim:
li $v0, 4		#comando 4 do syscall
la $a0, str04		#"digite o tanto de valores que quer usar no vetor:"
syscall

.data
str01: .asciiz "\nDigite o primeiro valor que será elevado pelo segundo,digite 0 para sair do programa: "
str02: .asciiz "Digite o segundo valor: "
str03: .asciiz "O primeiro valor elevado ao segundo vale: "
str04: .asciiz "Programa finalizado!"
str05: .asciiz "\nComeçando novamente o programa"
