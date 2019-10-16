.text
.globl main
main:
addi $t0,$zero,0x1001
sll $t0,$t0,16
addi $t1,$zero,0
par:
sw $t1,0($t0)
addi $t0,$t0,4
addi $t1,$t1,2
bne $t1,100,par
addi $t1,$zero,1
impar:
sw $t1,0($t0)
addi $t0,$t0,4
addi $t1,$t1,2
bne $t1,101,impar
