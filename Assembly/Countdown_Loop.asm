;=====================================================
; Count down from 10 and start over when reaches 0.
;=====================================================

LDA #1
STA $80
Start:
    LDA #10
Loop:
    OUT
    SUB $80
    BEQ Start
    BNE Loop
HLT
