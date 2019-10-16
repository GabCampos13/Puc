.text
.globl main
main:
addi $t0,$zero,0x1001
sll $t0,$t0,16
lw $t1,0($t0)
slt $t2,$zero,$t1
bne $t2,$zero,maior
mult $t1,$t1
mflo $t2
mult $t2,$t2
mflo $t2
addi $t2,$t2,+1
sub $t2,$zero,$t2
j fim
maior:
mult $t1,$t1
mflo $t2
mult $t2,$t1
mflo $t2
addi $t2,$t2,1
sw $t2,4($t0)
fim:
sw $t2,4($t0)
.data
X: .word -3