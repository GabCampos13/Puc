.text
.globl main
main:
addi $t0,$zero,0x1001
sll $t0,$t0,16
addi $t1,$zero,1
do:
add $t2,$t2,$t1
sw $t1,0($t0)
addi $t0,$t0,4
addi $t1,$t1,2
bne $t1,101,do
sw $t2,0($t0)
