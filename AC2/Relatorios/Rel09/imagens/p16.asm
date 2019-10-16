.text
.globl main
main:#s1 - i
addi $t6,$t6,1
addi $s1,$zero,0
addi $t0,$zero,0x1001
sll $t0,$t0,16
sll $t1,$s1,2
add $t0,$t0,$t1
add $t8,$zero,100
add $t9,$zero,100
do:
sw $t8,0($t0)
addi $t8,$t8,-1
addi $t0,$t0,4
bne $t8,0,do
addi $t0,$zero,0x1001
sll $t0,$t0,16
bolha:
lw $t2,0($t0)
lw $t3,4($t0)
beq $t6,$t2,fim
slt $t4,$t3,$t2
bne $t4,$zero,switch
addi $t0,$t0,4
bne $t9,$zero,bolha
switch:
sw $t2,4($t0)
sw $t3,0($t0)
addi $t0,$zero,0x1001
sll $t0,$t0,16
j bolha
fim: