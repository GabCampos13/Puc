.text
.globl teste
teste:
addi $t0,$zero,0x1001
sll $t0,$t0,16
lw $s1,0($t0)
lw $s2,4($t0)
lw $s3,8($t0)
lw $s4,12($t0)
.data
x1: .word 15
x2: .word 25
x3: .word 13
x4: .word 17