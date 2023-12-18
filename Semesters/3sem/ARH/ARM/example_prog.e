# CONAS v3.0 output file
#
# Processor name: ARM 7
#
8 ; memory word width
#
32 ; address width
#
#
# Original file: C:\Users\Ivan\Desktop\ARH\ARM\example_prog.a
#
#
<1,0>	00000000  0C 30 9F E5 ;      LDR   R3, OP1
<2,0>	00000004  0C 40 9F E5 ;      LDR   R4, OP2
<3,0>	                      ;
<4,0>	00000008  04 00 83 E0 ;      ADD   R0, R3, R4
<5,0>	0000000C  08 00 8F E5 ;      STR   R0, REZ
<6,0>	                      ;
<7,0>	00000010  56 34 12 EF ;      SWI   0x123456
<8,0>	                      ;
<9,0>	                      ;
<10,0>	00000014! 0F 00 00 00 ;OP1   DW    15
<11,0>	00000018! 03 00 00 00 ;OP2   DW    3
<12,0>	0000001C! 00 00 00 00 ;REZ   DW    0
#
# Debug Data
#
.debug:

#
#
# Assembling: OK