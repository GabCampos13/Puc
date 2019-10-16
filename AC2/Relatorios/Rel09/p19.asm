.text
.globl main
main:
addi $t0,$zero,0x1001
sll $t0,$t0,16
addi $t1,$zero,0x186A
sll $t1,$t1,8
addi $t2,$zero,0x1388
sll $t2,$t2,4
addi $t3,$zero,0x61A8
sll $t3,$t3,4
mult $t1,$t2
mflo $t4
div $t4,$t3
mflo $t5