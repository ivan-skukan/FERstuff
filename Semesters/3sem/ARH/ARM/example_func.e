# CONAS v3.0 output file
#
# Processor name: ARM 7
#
8 ; memory word width
#
32 ; address width
#
#
# Original file: C:\Users\Ivan\Desktop\ARH\ARM\example_func.a
#
#
<1,0>	00000000  40 DB A0 E3 ;      MOV   R13, #0x10000
<2,0>	                      ;        
<3,0>	00000004  38 50 A0 E3 ;      MOV   R5, #OPRND
<4,0>	00000008  00 30 95 E5 ;      LDR   R3, [R5]
<5,0>	0000000C  04 40 95 E5 ;      LDR   R4, [R5,#4]
<6,0>	                      ;
<7,0>	00000010  18 00 2D E9 ;      STMFD R13!, {R3,R4}
<8,0>	00000014  01 00 00 EB ;      BL    FUNC
<9,0>	00000018  20 00 8F E5 ;      STR   R0, REZ
<10,0>	                      ;
<11,0>	0000001C  56 34 12 EF ;      SWI   0x123456
<12,0>	                      ;
<13,0>	                      ;
<14,0>	00000020  06 00 2D E9 ;FUNC  STMFD R13!, {R1, R2}
<15,0>	00000024  08 10 9D E5 ;      LDR   R1, [SP, #8]
<16,0>	00000028  0C 20 9D E5 ;      LDR   R2, [SP, #12]
<17,0>	0000002C  02 00 81 E0 ;      ADD   R0, R1, R2
<18,0>	00000030  06 00 BD E8 ;      LDMFD R13!, {R1, R2}
<19,0>	00000034  0E F0 A0 E1 ;      MOV   PC, LR
<20,0>	                      ;
<21,0>	00000038! 0F 00 00 00 ;OPRND DW    15, 3
|         03 00 00 00
<22,0>	00000040! 00 00 00 00 ;REZ   DW    0
#
# Debug Data
#
.debug:

#
#
# Assembling: OK