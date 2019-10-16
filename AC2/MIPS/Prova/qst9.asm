.text
.globl teste
teste:#s0 = h,s1 = end base,s2 = i,s3 = j
add $t0,$s2,$s2
add $t0,$t0,$t0
add $t1,$s1,$t0
lw $t2,0($t1)	# t2 = A[i]
add $t5,$s0,$t2	#t5 = h + A[i]
add $t3,$s3,$s3
add $t3,$t3,$t3	
add $t4,$s1,$t3 #t4 = A[j]
sw $t5,0($t4) 	#A[j] = h + A[i]


