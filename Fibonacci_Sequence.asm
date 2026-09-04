;===================
; Fibonacci Sequence
;===================
Start:
    LDA #0
    STA $80
    OUT
    LDA #1
    STA $81
Loop:
    OUT
    ADD $80
    BCS Start
    STA $82
    LDA $81
    STA $80
    LDA $82
    STA $81
    JMP Loop
HLT
