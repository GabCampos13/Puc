.text
.globl teste
teste:
addi $s1,$zero,0	#i=0
sll $t1,$s0,2		#t1 = 4i
add $t1,$s0,$t1		#t1 = end base + 4i
addi $t3,$zero,0
loop:
lw $t2,0($t1)
addi $t1,$t1,4
add $t3,$t3,$t2
bne $t1,100,loop