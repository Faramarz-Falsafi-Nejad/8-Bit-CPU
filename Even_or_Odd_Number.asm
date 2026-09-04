;=============================================================
; Display 1 if a number is even or 0 if it's odd.
;=============================================================

LDA #48
AND #1
BNE Odd
LDA #1
JMP Output
Odd:
    LDA #0
Output:
    OUT
HLT
