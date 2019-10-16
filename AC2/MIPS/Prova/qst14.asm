.text
.globl teste
teste:
addi $t0,$zero,0x1001
sll $t0,$t0,16
addi $s0,$zero,0
addi $t1,$zero,1
addi $t2,$zero,1
sw $t1,0($t0)
loop:
sll $t3,$s0,2
add $t4,$t3,$t0		#t4 = end base+4i
sw $t1,0($t4)
add $t1,$t2,$t1
sw $t2,4($t4)
add $t2,$t2,$t1
bne $s0,100,do
do:
addi $s0,$s0,2
bne $s0,100,loop
