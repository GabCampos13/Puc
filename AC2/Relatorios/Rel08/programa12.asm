.text
.globl teste
teste:
addi $t0,$zero,0x1001
sll $t0,$t0,16
lw $s1,0($t0)
lw $s2,4($t0)
addi $t1,$zero,0x49
sll $t1,$t1,12
addi $t1,$t1,0x3e0
sub $t2,$s1,$s2
add $t2,$t2,$t1
sw $t2,8($t0)
.data
x: .word 100000
z: .word 200000
y: .word 0 


