.text
.globl main
main:

addi $a0, $0, 0x1001
sll $a0, $a0, 16
addi $a1, $0, 5
jal criaVet
add $t0, $0, $v0
li $v0, 1
la $a0, ($t0)
syscall
li $v0, 10
syscall

criaVet:
add $t0, $0, $a0 # recebe end
add $t1, $0, $a1 # recebe i
add $t5, $0, $t0
addi $t1, $t1, -1
add $t7, $0, $t1
sll $t2, $t1, 2
add $t0, $t0, $t2
addi $s0, $0, 2

while:
div $t1, $s0 # divisao de i por 2
mfhi $t3 # valor do resto para t3
beq $t3, $0, par # se o resto for igual de 0, vai pra par
sw $t1, 0($t0) # v[i] = i
j fim # pula pra dps do par

par:
add $t6, $t1, $t1 # 2i
addi $t6, $t6, -1 # 21 - 1
sw $t6, 0($t0) # salva (2i-1) no v[i]

fim:
addi $t0, $t0, -4 # prox posicao anterior
addi $t1, $t1, -1 # diminui i
slt $t4, $t1, $0  # compara o numero t1 < 0
beq $t4, $0, while # saiu do while, o vetor ta criado
add $t3, $0, $0

while2:
lw $t2, 0($t5)
add $t3, $t3, $t2
addi $t5, $t5, 4 # prox posicao
addi $t7, $t7, -1 # diminui i
slt $t4, $t7, $0  # compara o numero t6 < 0
beq $t4, $0, while2 # saiu do while2
add $v0, $0, $t3
jr $ra

.data

