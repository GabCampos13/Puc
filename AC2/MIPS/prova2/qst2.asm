.text
.globl main
main:

li $v0, 4		#comando 4 do syscall
la $a0, str0		#"Nesse programa voce tera que digitar 3 numeros (int)\n"
syscall
li $v0, 4		
la $a0, str1		#"Favor digitar o primeiro:"
syscall
li $v0, 5		#comando 5 do syscall
syscall
la $t0, ($v0)		#salva em t0 o valor escrito
li $v0, 4
la $a0, str2		#"Favor digitar o segundo:"
syscall
li $v0, 5	
syscall
la $t1, ($v0)		#salva em t1 o valor escrito
slt $t4, $t1, $t0	#se t1<t0 t4 = 1
beq $t4, $0, prox	#se t4 = 0 go to prox
add $t5, $0, $t0	#t5 = t0
add $t0, $0, $t1	#t0 = t1
add $t1, $0, $t5	#t1 = t5

prox:
li $v0, 4
la $a0, str3		#"Favor digitar o terceiro:"
syscall
li $v0, 5
syscall
la $t2, ($v0)		#salva em t2 o valor escrito
slt $t4, $t2, $t0	#se t2 < t0 t4 = 1
beq $t4, $0, test2	#se t4 = 0 go to test2
add $t5, $0, $t2	#t5 = t2
add $t2, $0, $t1	#t2 = t1
add $t1, $0, $t0	#t1 = t0
add $t0, $0, $t5	#t0 = t5

test2:
slt $t4, $t1, $t2	#se t1<t2 t4 = 1
bne $t4, $0, fim	#se t4 = 0 go to fim
add $t5, $0, $t1	#t5 = t1
add $t1, $0, $t2	#t1 = t2
add $t2, $0, $t5	#t2 = t5

fim:
li $v0, 4
la $a0, str4	#"maior eh:"
syscall
li $v0, 1	#printar um int
la $a0, ($t2)	#a0 recebe valor de t2
syscall
li $v0, 4	
la $a0, str5	#"menor eh:"	
syscall
li $v0, 1	#printar um int
la $a0, ($t0)	#a0 recebe valor de t0
syscall

.data
str0: .asciiz "Nesse programa voce tera que digitar 3 numeros (int)\n"
str1: .asciiz "Favor digitar o primeiro:"
str2: .asciiz "\nFavor digitar o segundo:"
str3: .asciiz "\nFavor digitar o terceiro:"
str4: .asciiz "\nO maior eh:"
str5: .asciiz "\nO menor eh:"


