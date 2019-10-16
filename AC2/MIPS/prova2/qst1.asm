.text
.globl teste
teste:
li $v0,4
la $a0,str
syscall
li $v0,10
.data
str: .asciiz "Hello world!"
.text
