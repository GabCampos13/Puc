.text
.globl main
main:
addi $t0,$zero,0x1001
sll $t0,$t0,16
lw $t1,0($t0)
slt $t2,$zero,$t1		#if(0 < A) = 1
beq $t2,$zero,menor		
j end
menor:
sub $s0,$zero,$t1		#s0 = 0 - A
sw $s0,0($t0)
end:
.data
A: .word -3
