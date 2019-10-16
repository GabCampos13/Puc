.text
.globl teste
teste:
addi $t0,$zero,0x1001
sll $t0,$t0,16
lw $t1,0($t0)
lw $t2,4($t0)
lw $t3,8($t0)
lw $t4,12($t0)
add $t1,$t1,$t2
add $t3,$t3,$t4
add $t1,$t1,$t3
sw $t1,16($t0)
.data
x1: .word 15
x2: .word 25
x3: .word 13
x4: .word 17
soma: .word -1


