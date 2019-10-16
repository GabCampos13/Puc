.text
.globl teste
teste:
addi $t0,$zero,0x1001
sll $t0,$t0,16
addi $t1,$zero,0
loop:
sw $t1,0($t0)
addi $t1,$t1,2
addi $t0,$t0,0x0004
bne $t1,102,loop
addi $t1,$zero,1
impares:
sw $t1,0($t0)
addi $t1,$t1,2
addi $t0,$t0,0x0004
bne $t1,101,impares