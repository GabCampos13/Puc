.text
.globl teste
teste:   #s0 = k,s1 = end base,s2 = i,s3 = h
add $t0,$s2,$s2	#t0 = 2i
add $t0,$t0,$t0 #t0 = 4i
add $t1,$t0,$s1 #t1 = 4i+end base
lw $t2,0($t1)	#t2= A[i]
add $s3,$t2,$s0 #h = k + A[i]

