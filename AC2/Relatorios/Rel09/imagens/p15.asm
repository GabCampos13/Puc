.text
.globl main
main:#s1 = i
addi $s1,$zero,0
addi $t0,$zero,0x1001
sll $t0,$t0,16
sll $t1,$s1,2
add $t0,$t0,$t1
add $t8,$zero,$s1
do:
add $t2,$s1,$s1
addi $t2,$t2,1
sw $t2,0($t0)
addi $t0,$t0,4
addi $s1,$s1,1
addi $t8,$t8,1
add $t5,$t5,$t2
bne $t8,100,do
fim:
sw $t5,0($t0)