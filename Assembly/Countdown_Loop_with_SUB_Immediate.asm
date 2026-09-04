;=====================================================
; Count down from 10 and start over when reaches 0.
;=====================================================

Start:
    LDA #10
Loop:
    OUT
    SUB #1
    BEQ Start
    BNE Loop
HLT
