# CONAS v3.0 output file
#
# Processor name: ARM 7
#
8 ; memory word width
#
32 ; address width
#
#
# Original file: C:/Users/Ivan/Desktop/ARH/ARM/zadatak1.a
#
#
<1,0>	                      ;        ORG 0x0
<2,0>	00000000  05 00 00 EA ;        B MAIN
<3,0>	                      ;
<4,0>	                      ;        ORG 0x18
<5,0>	00000018  13 00 00 EA ;        B DO_IRQ
<6,0>	                      ;
<7,0>	0000001C  D2 F0 29 E3 ;MAIN    MSR CPSR, #0b11010010 ; stog za irq i svc
<8,0>	00000020  40 DB A0 E3 ;        MOV R13, #0X10000
<9,0>	00000024  D3 F0 29 E3 ;        MSR CPSR, #0b11010011
<10,0>	00000028  FC DC A0 E3 ;        MOV R13, #0XFC00
<11,0>	                      ;   
<12,0>	0000002C  DC 11 9F E5 ;        LDR R1, GPIO1
<13,0>	00000030  04 10 81 E2 ;        ADD R1, R1, #4
<14,0>	00000034  D8 21 9F E5 ;        LDR R2 , GPIO2
<15,0>	00000038  D8 31 9F E5 ;        LDR R3, RTC
<16,0>	                      ;
<17,0>	0000003C  E0 00 A0 E3 ;GPIO_IN MOV R0, #0B11100000 ;;GPIO2
<18,0>	00000040  08 00 82 E5 ;        STR R0, [R2,#8]
<19,0>	                      ;
<20,0>	00000044  05 00 A0 E3 ;RTC_IN  MOV R0, #5
<21,0>	00000048  04 00 83 E5 ;        STR R0, [R3,#4]
<22,0>	0000004C  00 00 A0 E3 ;        MOV R0, #0
<23,0>	00000050  0C 00 83 E5 ;        STR R0, [R3, #0XC]
<24,0>	00000054  01 00 A0 E3 ;        MOV R0, #1
<25,0>	00000058  10 00 83 E5 ;        STR R0, [R3, #0X10]
<26,0>	                      ;        
<27,0>	0000005C  00 00 0F E1 ;DOZVOLI MRS R0,CPSR 
<28,0>	00000060  80 00 C0 E3 ;        BIC R0,R0,#0b10000000
<29,0>	00000064  00 F0 29 E1 ;        MSR CPSR,R0      
<30,0>	00000068  FE FF FF EA ;LOOP    B LOOP          
<31,0>	                      ;
<32,0>	0000006C  0F 40 2D E9 ;DO_IRQ  STMFD SP!, {R0-R3,LR}
<33,0>	00000070  A0 31 9F E5 ;        LDR R3, RTC
<34,0>	00000074  00 00 A0 E3 ;        MOV R0, #0
<35,0>	00000078  08 00 83 E5 ;        STR R0, [R3,#0X8] ; brojac
<36,0>	0000007C  0C 00 83 E5 ;        STR R0, [R3,#0XC] ; potvrda prekida
<37,0>	                      ;        
<38,0>	00000080  80 04 9F E5 ;        LDR R0, STATUS
<39,0>	                      ;
<40,0>	00000084  01 00 50 E3 ;        CMP R0, #1
<41,0>	00000088  0F 00 00 0B ;        BLEQ STAT1
<42,0>	0000008C  0C 00 00 0A ;        BEQ END
<43,0>	                      ;
<44,0>	00000090  02 00 50 E3 ;        CMP R0, #2
<45,0>	00000094  21 00 00 0B ;        BLEQ STAT2
<46,0>	00000098  09 00 00 0A ;        BEQ END
<47,0>	                      ;
<48,0>	0000009C  03 00 50 E3 ;        CMP R0, #3
<49,0>	000000A0  31 00 00 0B ;        BLEQ STAT3
<50,0>	000000A4  06 00 00 0A ;        BEQ END
<51,0>	                      ;
<52,0>	000000A8  04 00 50 E3 ;        CMP R0, #4
<53,0>	000000AC  36 00 00 0B ;        BLEQ STAT4
<54,0>	000000B0  03 00 00 0A ;        BEQ END
<55,0>	                      ;
<56,0>	000000B4  05 00 50 E3 ;        CMP R0, #5
<57,0>	000000B8  3B 00 00 0B ;        BLEQ STAT5
<58,0>	000000BC  00 00 00 0A ;        BEQ END
<59,0>	                      ;
<60,0>	000000C0  41 00 00 EB ;        BL STAT6
<61,0>	                      ;
<62,0>	000000C4  0F 40 BD E8 ;END     LDMFD SP!, {R0-R3,LR}
<63,0>	000000C8  04 F0 5E E2 ;        SUBS PC, LR, #4
<64,0>	                      ;
<65,0>	000000CC  1F 40 2D E9 ;STAT1   STMFD R13!, {R0-R4,LR}
<66,0>	000000D0  01 00 80 E2 ;        ADD R0, R0, #1
<67,0>	000000D4  2C 04 8F E5 ;        STR R0, STATUS
<68,0>	000000D8  30 11 9F E5 ;        LDR R1, GPIO1
<69,0>	000000DC  04 10 81 E2 ;        ADD R1, R1, #4
<70,0>	000000E0  2C 21 9F E5 ;        LDR R2, GPIO2
<71,0>	                      ;
<72,0>	000000E4  20 00 A0 E3 ;        MOV R0, #0B00100000
<73,0>	000000E8  00 00 82 E5 ;        STR R0, [R2, #0X0]
<74,0>	                      ;
<75,0>	000000EC  0D 00 A0 E3 ;        MOV R0, #0X0D
<76,0>	000000F0  3D 00 00 EB ;        BL LCDWR
<77,0>	                      ;
<78,0>	000000F4  40 3E A0 E3 ;        MOV R3, #0X400 
<79,0>	000000F8  00 40 A0 E3 ;        MOV R4, #0
<80,0>	000000FC  01 00 D3 E4 ;WRITE1  LDRB R0, [R3],#1
<81,0>	00000100  39 00 00 EB ;        BL LCDWR
<82,0>	00000104  01 40 84 E2 ;        ADD R4, R4, #1
<83,0>	00000108  05 00 54 E3 ;        CMP R4, #5
<84,0>	0000010C  FA FF FF 1A ;        BNE WRITE1
<85,0>	00000110  0A 00 A0 E3 ;        MOV R0, #0X0A
<86,0>	00000114  34 00 00 EB ;        BL LCDWR
<87,0>	00000118  1F 40 BD E8 ;        LDMFD R13!, {R0-R4,LR}
<88,0>	0000011C  0E F0 A0 E1 ;        MOV PC, LR
<89,0>	                      ;
<90,0>	00000120  1F 40 2D E9 ;STAT2   STMFD R13!, {R0-R4,LR}
<91,0>	00000124  01 00 80 E2 ;        ADD R0, R0, #1
<92,0>	00000128  D8 03 8F E5 ;        STR R0, STATUS
<93,0>	0000012C  DC 10 9F E5 ;        LDR R1, GPIO1
<94,0>	00000130  04 10 81 E2 ;        ADD R1, R1, #4
<95,0>	00000134  D8 20 9F E5 ;        LDR R2, GPIO2
<96,0>	                      ;
<97,0>	00000138  0D 00 A0 E3 ;        MOV R0, #0X0D
<98,0>	0000013C  2A 00 00 EB ;        BL LCDWR
<99,0>	                      ;
<100,0>	00000140  50 3E A0 E3 ;        MOV R3, #0X500
<101,0>	00000144  00 40 A0 E3 ;        MOV R4, #0
<102,0>	00000148  01 00 D3 E4 ;WRITE2  LDRB R0, [R3], #1
<103,0>	0000014C  26 00 00 EB ;        BL LCDWR
<104,0>	00000150  01 40 84 E2 ;        ADD R4, R4, #1
<105,0>	00000154  05 00 54 E3 ;        CMP R4, #5
<106,0>	00000158  FA FF FF 1A ;        BNE WRITE2
<107,0>	0000015C  0A 00 A0 E3 ;        MOV R0, #0X0A
<108,0>	00000160  21 00 00 EB ;        BL LCDWR
<109,0>	00000164  1F 40 BD E8 ;        LDMFD R13!, {R0-R4,LR}
<110,0>	00000168  0E F0 A0 E1 ;        MOV PC, LR
<111,0>	                      ;
<112,0>	0000016C  03 00 2D E9 ;STAT3   STMFD R13!, {R0-R1}
<113,0>	00000170  01 00 80 E2 ;        ADD R0, R0, #1
<114,0>	00000174  8C 03 8F E5 ;        STR R0, STATUS
<115,0>	00000178  94 10 9F E5 ;        LDR R1, GPIO2
<116,0>	0000017C  60 00 A0 E3 ;        MOV R0, #0B01100000
<117,0>	00000180  00 00 81 E5 ;        STR R0, [R1,#0]
<118,0>	00000184  03 00 BD E8 ;        LDMFD R13!, {R0-R1}
<119,0>	00000188  0E F0 A0 E1 ;        MOV PC, LR
<120,0>	                      ;
<121,0>	0000018C  03 00 2D E9 ;STAT4   STMFD R13!, {R0,R1}
<122,0>	00000190  01 00 80 E2 ;        ADD R0, R0, #1
<123,0>	00000194  6C 03 8F E5 ;        STR R0, STATUS
<124,0>	00000198  74 10 9F E5 ;        LDR R1, GPIO2
<125,0>	0000019C  80 00 A0 E3 ;        MOV R0, #0B10000000
<126,0>	000001A0  00 00 81 E5 ;        STR R0, [R1, #0]
<127,0>	000001A4  03 00 BD E8 ;        LDMFD R13!, {R0-R1}
<128,0>	000001A8  0E F0 A0 E1 ;        MOV PC, LR
<129,0>	                      ;
<130,0>	000001AC  03 00 2D E9 ;STAT5   STMFD R13!, {R0,R1}
<131,0>	000001B0  01 00 80 E2 ;        ADD R0, R0, #1
<132,0>	000001B4  4C 03 8F E5 ;        STR R0, STATUS
<133,0>	000001B8  54 10 9F E5 ;        LDR R1, GPIO2
<134,0>	000001BC  40 00 A0 E3 ;        MOV R0, #0B01000000
<135,0>	000001C0  00 00 81 E5 ;        STR R0, [R1, #0]
<136,0>	000001C4  03 00 BD E8 ;        LDMFD R13!, {R0-R1}
<137,0>	000001C8  0E F0 A0 E1 ;        MOV PC, LR
<138,0>	                      ;
<139,0>	000001CC  03 00 2D E9 ;STAT6   STMFD R13!, {R0,R1}
<140,0>	000001D0  01 00 A0 E3 ;        MOV R0, #1
<141,0>	000001D4  2C 03 8F E5 ;        STR R0, STATUS
<142,0>	000001D8  34 10 9F E5 ;        LDR R1, GPIO2
<143,0>	000001DC  20 00 A0 E3 ;        MOV R0, #0B00100000
<144,0>	000001E0  00 00 81 E5 ;        STR R0, [R1, #0]
<145,0>	000001E4  03 00 BD E8 ;        LDMFD R13!, {R0-R1}
<146,0>	000001E8  0E F0 A0 E1 ;        MOV PC, LR
<147,0>	                      ;        
<148,0>	                      ;
<149,0>	000001EC  01 00 2D E9 ;LCDWR   STMFD R13!, {R0} ; za ispis na LCD (ctrl+v sa predavanja)
<150,0>	000001F0  7F 00 00 E2 ;        AND R0, R0, #0x7F 
<151,0>	000001F4  00 00 C1 E5 ;        STRB R0, [R1]
<152,0>	000001F8  80 00 80 E3 ;        ORR R0, R0, #0x80 
<153,0>	000001FC  00 00 C1 E5 ;        STRB R0, [R1]
<154,0>	00000200  7F 00 00 E2 ;        AND R0, R0, #0x7F 
<155,0>	00000204  00 00 C1 E5 ;        STRB R0, [R1]
<156,0>	00000208  01 00 BD E8 ;        LDMFD R13!, {R0}
<157,0>	0000020C  0E F0 A0 E1 ;        MOV PC, LR
<158,0>	                      ;
<159,0>	00000210! 00 0F FF FF ;GPIO1 DW 0XFFFF0F00
<160,0>	00000214! 00 0B FF FF ;GPIO2 DW 0XFFFF0B00
<161,0>	00000218! 00 0E FF FF ;RTC DW 0XFFFF0E00
<162,0>	                      ;
<163,0>	                      ; ORG 0X400
<164,0>	00000400! 48 4F 44 41 ; DB 0X48,0X4F,0X44,0X41,0X4A ;HODAJ
|         4A
<165,0>	                      ;
<166,0>	                      ; ORG 0X500
<167,0>	00000500! 53 54 41 4E ; DB 0X53, 0X54, 0X41,0X4E,0X49 ;STANI
|         49
<168,0>	                      ;
<169,0>	00000508! 01 00 00 00 ;STATUS DW 1
#
# Debug Data
#
.debug:

#
#
# Assembling: OK