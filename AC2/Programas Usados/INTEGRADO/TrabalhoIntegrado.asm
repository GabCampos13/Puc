#INCLUDE <P16F628A.INC>		;ARQUIVO PADRÃO MICROCHIP PARA 16F628A
__CONFIG H'3F10'
RADIX DEC
#DEFINE	BANK0	BCF STATUS,RP0	;SETA BANK 0 DE MEMÓRIA

#DEFINE	BANK1	BSF STATUS,RP0	;SETA BANK 1 DE MAMÓRIA

	CBLOCK	0x20	;ENDEREÇO INICIAL DA MEMÓRIA DE USUÁRIO
	
	CONTADOR1
	CONTADOR2	
	CONTADOR3		
	CONTADOR4	
	QUALANDAR	;Numero do andar que está o elevador


	ENDC			;FIM DO BLOCO DE MEMÓRIA		

#DEFINE	BOTAO	PORTA,2	;PORTA DO BOTÃO
					; 0 -> PRESSIONADO
					; 1 -> LIBERADO

#DEFINE	LED1	PORTB,0	;PORTA DO LED
				; 0 -> APAGADO
				; 1 -> ACESO

#DEFINE	LED2	PORTB,1	;PORTA DO LED
				; 0 -> APAGADO
				; 1 -> ACESO
#DEFINE	LED3	PORTB,2	;PORTA DO LED
				; 0 -> APAGADO
				; 1 -> ACESO
#DEFINE LED4	PORTB,3 ;PORTA DO LED
				;0 -> APAGADO
				;1 -> ACESO


	ORG	0x00		;ENDEREÇO INICIAL DE PROCESSAMENTO
	GOTO	INICIO
	
INICIO

	CLRF	PORTA		;LIMPA O PORTA
	CLRF	PORTB		;LIMPA O PORTB
	BANK1			;ALTERA PARA O BANCO 1
	MOVLW	B'00000100'
	MOVWF	TRISA		;DEFINE RA2 COMO ENTRADA E DEMAIS COMO SAÍDAS
	MOVLW	B'00000000'
	MOVWF	TRISB		;DEFINE TODO O PORTB COMO SAÍDA
	MOVLW	B'00000000'
	MOVWF	INTCON		;TODAS AS INTERRUPÇÕES DESLIGADAS
	BANK0			;RETORNA PARA O BANCO 0
	MOVLW	B'00000111'
	MOVWF	CMCON		;DEFINE O MODO DO COMPARADOR ANALÓGICO


MAIN

	MOVLW -1				;Coloca -1 em W
	MOVWF CONTADOR4			;Escreve W em CONTADOR4
	DECFSZ CONTADOR4		;decrementa em 1 o contador2, caso seja 0 pula uma linha
	call TERREO				;Chama TERREO
	GOTO MAIN				;LOOP da MAIN

TERREO
	MOVLW 0				;Coloca 0 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR

	BSF LED1			;LIGA LED1
	call ATRASO1		;Chama ATRASO1(2seg)
	BCF LED1			;DESLIGA LED1
	call ANDAR1			;Vai para o ANDAR1
	
	MOVLW 0				;Coloca 0 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR
	return				;retorna para onde chamou(MAIN)

ANDAR1
	;SUBINDO
	MOVLW 1				;Coloca 1 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR

	BSF	LED2			;LIGA LED2
	call ATRASO1		;Chama ATRASO1(2seg)
	call ATRASO1		;Chama ATRASO1(2seg)
	BCF LED2			;DESLIGA LED2
	call ANDAR2			;Vai para ANDAR2
	
	;DESCENDO
	MOVLW 1				;Coloca 1 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR

	BSF	LED2			;LIGA LED2
	call ATRASO1		;Chama ATRASO1(2seg)
	call ATRASO1		;Chama ATRASO1(2seg)
	BCF LED2			;DESLIGA LED2
	return				;retorna para onde chamou(TERREO)
	

ANDAR2
	;SUBINDO
	MOVLW 2				;Coloca 2 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR

	BSF LED3			;LIGA LED3
	call ATRASO1		;Chama ATRASO1(2seg)
	call ATRASO1		;Chama ATRASO1(2seg)
	call ATRASO1		;Chama ATRASO1(2seg)
	BCF LED3			;DESLIGA LED3
	call ANDAR3

	;DESCENDO
	MOVLW 2				;Coloca 2 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR

	BSF LED3			;LIGA LED3
	call ATRASO1		;Chama ATRASO1(2seg)
	call ATRASO1		;Chama ATRASO1(2seg)
	call ATRASO1		;Chama ATRASO1(2seg)
	BCF LED3			;DESLIGA LED3
	return				;retorna para onde chamou(ANDAR1)

ANDAR3
	MOVLW 3				;Coloca 3 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR

	BSF LED4			;LIGA LED4
	call ATRASO1		;Chama ATRASO1(2seg)
	call ATRASO1		;Chama ATRASO1(2seg)
	call ATRASO1		;Chama ATRASO1(2seg)
	call ATRASO1		;Chama ATRASO1(2seg)
	BCF LED4			;DESLIGA LED4
	return				;retorna para onde chamou(ANDAR2)
	

ATRASO1
	MOVLW 54				;Coloca 54 em W ---  54-2seg 	27-1seg
	MOVWF CONTADOR1			;Escreve W em CONTADOR1
ATRASO11
	nop						;nop		
	call ATRASO2			;NAO,chama ATRASO2 ;Testa o botao 27 vezes por segundo	
	MOVLW 101				;Coloca 101 em W
	MOVWF CONTADOR2			;Escreve W em CONTADOR2
	DECFSZ CONTADOR1		;Decrementa em 1 o contador1, se 0 pula uma linha
	GOTO ATRASO11			;jump para ATRASO11
	RETURN					;retorna para onde chamou
ATRASO2
	BTFSS BOTAO				;O BOTÃO ESTÁ PRESSIONADO?
	GOTO PRESS_BUTTON		;SIM, ENTÃO TRATA BOTÃO PRESSIONADO
ATRASO22	
	call ATRASO3			;Chama ATRASO3
	MOVLW 120				;Coloca 120 em W
	MOVWF CONTADOR3			;Escreve W em Contador3
	DECFSZ CONTADOR2		;decrementa em 1 o contador2, se 0 pula uma linha
	GOTO ATRASO22			;jump para ATRASO22
	RETURN					;retorna para onde chamou


ATRASO1B
	MOVLW 54				;Coloca 54 em W ---  54-2seg 	27-1seg
	MOVWF CONTADOR1			;Escreve W em CONTADOR1
ATRASO11B
	nop						;nop		
	call ATRASO2B			;NAO,chama ATRASO2B
	MOVLW 101				;Coloca 101 em W
	MOVWF CONTADOR2			;Escreve W em CONTADOR2
	DECFSZ CONTADOR1		;Decrementa em 1 o contador1, se 0 pula uma linha
	GOTO ATRASO11B			;jump para ATRASO11B
	RETURN					;retorna para onde chamou
ATRASO2B
	call ATRASO3			;Chama ATRASO3
	MOVLW 120				;Coloca 120 em W
	MOVWF CONTADOR3			;Escreve W em Contador3
	DECFSZ CONTADOR2		;decrementa em 1 o contador2, se 0 pula uma linha
	GOTO ATRASO2B			;jump para ATRASO2B
	return					;retorna para onde chamou

ATRASO3
 	DECFSZ CONTADOR3		;decrementa em 1 o contador3, se 0 pula uma linha
	GOTO ATRASO3			;jump para ATRASO3
	RETURN					;retorna para onde chamou


PRESS_BUTTON
	DECF QUALANDAR			;Decrementa em 1 o QUALANDAR
	INCFSZ QUALANDAR		;Incrementa em 1 o QUALANDAR, se 0 pula 1 linha
	GOTO IF1				;if(QUALANDAR != 0) va para IF1
	GOTO noTerreo			;if(QUALANDAR == 0) va para noTerreo
IF1
	DECFSZ QUALANDAR		;Decrementa em 1 o QUALANDAR, se 0 pula 1 linha
	GOTO IF2				;if(QUALANDAR != 0) va para IF2
	GOTO noPrimeiro			;if(QUALANDAR == 0) va para noPrimeiro
IF2
	DECFSZ QUALANDAR		;Decrementa em 1 o QUALANDAR, se 0 pula 1 linha
	GOTO IF3				;if(QUALANDAR != 0) va para IF3
	GOTO noSegundo			;if(QUALANDAR == 0) va para noSegundo
IF3
	GOTO noTerceiro			;va para noTerceiro

noTerreo
	MOVLW 0				;Coloca 0 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR

	BSF LED1			;LIGA LED1
	BTFSS BOTAO			;O BOTÃO ESTÁ PRESSIONADO?
	GOTO noTerreo		;SIM, va para noTerreo(LOOP)
	call ATRASO1B		;Chama ATRASO1B(2seg)
	call ATRASO1B		;Chama ATRASO1B(2seg)
	call ATRASO1B		;Chama ATRASO1B(2seg)
	call ATRASO1B		;Chama ATRASO1B(2seg)
	GOTO MAIN			;va para MAIN

noPrimeiro
	MOVLW 1				;Coloca 1 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR

	BSF	LED2			;LIGA LED2
	call ATRASO1B		;Chama ATRASO1B(2seg)
	BCF LED2			;DESLIGA LED2
	GOTO noTerreo		;va para noTerreo

noSegundo
	MOVLW 2				;Coloca 2 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR

	BSF LED3			;LIGA LED3
	call ATRASO1B		;Chama ATRASO1B(2seg)
	BCF LED3			;DESLIGA LED3
	GOTO noPrimeiro		;va para noPrimeiro

noTerceiro
	MOVLW 3				;Coloca 3 em W
	MOVWF QUALANDAR		;Escreve W em QUALANDAR
	
	BSF LED4			;LIGA LED4
	call ATRASO1B		;Chama ATRASO1B(2seg)
	BCF LED4			;DESLIGA LED4
	GOTO noSegundo		;va para noSegundo
		
	END			;OBRIGATÓRIO


