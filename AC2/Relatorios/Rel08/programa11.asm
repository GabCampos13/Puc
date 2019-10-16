.text
.globl teste
teste:
addi $t4,$zero,0x1001
sll $t4,$t4,16
lw $s1,0($t4)
lw $s2,4($t4)
add $t0,$zero,$s1
sll $t0,$t0,7
sub $t0,$t0,$s1
add $t1,$zero,$s2
sll $t1,$t1,6
add $t1,$t1,$s2
sub $t3,$t0,$t1
addi $t3,$t3,1
sw $t3,8($t4)
.data
x: .word 5
z: .word 7
y: .word 0


