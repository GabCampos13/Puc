.text
.globl main
main:
addi $t0,$zero,0x1001
sll $t0,$t0,16
lw $t1,0($t0)
lw $t7,4($t0)
lw $t8,8($t0)
slt $t5,$t1,$t7
bne $t5,$zero,fora
slt $t6,$t8,$t1
bne $t6,$zero,fora
addi $t3,$zero,1
sw $t3,12($t0)
j end
fora:
addi $t3,$zero,0
sw $t3,12($t0)
end:

.data
A: .word 40
Menor: .word 30
Maior: .word 50
Flag: .word 0