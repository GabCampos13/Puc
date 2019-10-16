.text
.globl teste
teste:#s0 = h,s1 = end base,s2 = i
add $t0,$s2,$s2
add $t0,$t0,$t0
add $t1,$s1,$t0
lw $t2,0($t1) #t2 = A[i]
add $s0,$zero,$t2 # h = A[i]
lw $t3,4($t1) #t3 = A[i+1]
sw $t3,0($t1) #A[i] = A[i+1]
sw $s0,4($t1) #A[i+1] = h