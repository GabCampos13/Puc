.text
.globl teste
teste:#s0 = j,s1 = i
addi $s0,$zero,0 #j = 0	
addi $s1,$zero,10 #i = 10
do:
addi $s0,$s0,1 #j = j + 1
bne $s0,$s1,do #se( j != i) go to DO
