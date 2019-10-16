.text
.globl main
main:
addi $t0,$zero,0x1001
sll $t0,$t0,16
lw $t1,0($t0)
lw $t2,4($t0)
addi $t3,$zero,1
do:
mult $t3,$t1
mflo $t3
addi $t2,$t2,-1
bne $t2,$zero,do
sw $t3,8($t0)
.data
x: .word 3
y: .word 5