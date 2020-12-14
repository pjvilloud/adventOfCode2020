"""
--- Day 14: Docking Data ---
As your ferry approaches the sea port, the captain asks for your help again. The computer system that runs this port isn't compatible with the docking program on the ferry, so the docking parameters aren't being correctly initialized in the docking program's memory.

After a brief inspection, you discover that the sea port's computer system uses a strange bitmask system in its initialization program. Although you don't have the correct decoder chip handy, you can emulate it in software!

The initialization program (your puzzle input) can either update the bitmask or write a value to memory. Values and memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a moment, a line like mem[8] = 11 would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) on the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current bitmask is applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit in the value, while an X leaves the bit in the value unchanged.

For example, consider the following program:

mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
This program starts by specifying a bitmask (mask = ....). The mask it specifies will overwrite two bits in every written value: the 2s bit is overwritten with 0, and the 64s bit is overwritten with 1.

The program then attempts to write the value 11 to memory address 8. By expanding everything out to individual bits, the mask is applied as follows:

value:  000000000000000000000000000000001011  (decimal 11)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001001001  (decimal 73)
So, because of the mask, the value 73 is written to memory address 8 instead. Then, the program tries to write 101 to address 7:

value:  000000000000000000000000000001100101  (decimal 101)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001100101  (decimal 101)
This time, the mask has no effect, as the bits it overwrote were already the values the mask tried to set. Finally, the program tries to write 0 to address 8:

value:  000000000000000000000000000000000000  (decimal 0)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001000000  (decimal 64)
64 is written to address 8 instead, overwriting the value that was there previously.

To initialize your ferry's docking program, you need the sum of all values left in memory after the initialization program completes. (The entire 36-bit address space begins initialized to the value 0 at every address.) In the above example, only two values in memory are not zero - 101 (at address 7) and 64 (at address 8) - producing a sum of 165.

Execute the initialization program. What is the sum of all values left in memory after it completes?

Your puzzle answer was 6631883285184.

--- Part Two ---
For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

For example, consider the following program:

mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
When this program goes to write to memory address 42, it first applies the bitmask:

address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X
After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)
Next, the program is about to write to memory address 26 with a different bitmask:

address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX
This results in an address with three floating bits, causing writes to eight memory addresses:

000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is 208.

Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?

Your puzzle answer was 3161838538691.
"""
input = """mask = 0X0X1110X1010X1X10010X0011010X100110
mem[40190] = 23031023
mem[13516] = 384739600
mask = XX00111XX1010X0110011110X1XX110010X1
mem[12490] = 3068791
mem[61106] = 3432
mem[48664] = 204086010
mask = X0X01101010001X10X01X1X1101010100000
mem[43153] = 831935068
mem[61625] = 5711
mem[43599] = 125635699
mem[36959] = 776266806
mask = 0000111XX1010101X001XXX1X01000001110
mem[48186] = 257869
mem[59392] = 738895
mem[65386] = 4054824
mem[10464] = 2127
mem[13157] = 3065832
mem[32527] = 5148099
mem[11578] = 47394043
mask = 0000XX1X1X01001111011X000011101100X1
mem[49914] = 789
mem[4369] = 707
mem[42622] = 57353
mask = 000X111111010011110X00X00X00101XX00X
mem[11935] = 5289
mem[37504] = 11253192
mem[19249] = 7675784
mem[54234] = 154953
mask = 100011101X0X0X1X0X0101110111X0101XX1
mem[10812] = 453923
mem[63398] = 912
mem[6051] = 14102698
mem[20865] = 55854
mask = X1X110101100011100X0X110010110100111
mem[19497] = 25377951
mem[1453] = 6580
mem[27914] = 3060231
mem[31492] = 350
mem[3524] = 24817238
mask = 100011X0110110110001110000X011100X1X
mem[35829] = 26554027
mem[62092] = 29219
mem[32025] = 472
mem[13072] = 1639
mem[50563] = 90274
mask = 000100X011111011XX00X010010001101011
mem[31857] = 1048
mem[19108] = 338887
mem[35434] = 28216
mem[60774] = 6266
mem[43153] = 253275666
mask = X000100010X1010100X11XX0110XXX011X01
mem[10624] = 457482
mem[37932] = 1954
mem[14840] = 17345899
mem[13784] = 63343
mem[42014] = 43155127
mem[64776] = 13454
mem[3904] = 62118
mask = 0000111011010111X1XX11X1XX1001111010
mem[60613] = 15496
mem[2173] = 22888539
mem[25440] = 28075628
mem[37682] = 31592780
mem[20667] = 365247
mask = 0X0X11X001010101000XX010111X0000111X
mem[12455] = 7882
mem[14311] = 596
mem[28934] = 40439830
mask = 1X00XX1011X110110X01010110X000XX01X0
mem[14618] = 789
mem[362] = 60235
mem[2816] = 119067
mask = 1000111001X10111X00100XX00110000010X
mem[466] = 326507
mem[44593] = 5014
mem[8356] = 12567436
mem[43420] = 29769
mem[53433] = 19683179
mask = 00001X1011010111X0010X11X0011XX1011X
mem[61697] = 7156
mem[33280] = 58216
mem[40394] = 50625
mem[11578] = 21809457
mem[26729] = 93660269
mem[34586] = 263574
mask = X00X00101101111110010X10X0X0X0011000
mem[59256] = 1730680
mem[41435] = 92329839
mem[4497] = 9476
mem[13811] = 1654260
mask = 10X010100101011X0X1X0101110100000001
mem[17332] = 7813345
mem[1001] = 204359
mem[28516] = 265519412
mem[28940] = 131981555
mem[39113] = 1895784
mem[47340] = 2838572
mem[25173] = 358383699
mask = 100XX110X11X01000101101X00111110X011
mem[55419] = 39220
mem[16382] = 388948
mem[58038] = 170145020
mem[20667] = 2659216
mem[17540] = 72534
mem[32554] = 436
mask = 0X0010001X01X1X1000110X1110X10XX0001
mem[20940] = 1671
mem[43952] = 38617
mem[37682] = 1905
mem[4678] = 1463101
mem[6158] = 5719158
mem[48132] = 55174
mask = X0010000011X10111001110XXX111110101X
mem[39251] = 6799
mem[8211] = 62437
mem[3866] = 1045835
mem[59817] = 337757
mem[43531] = 337
mask = 00001110110101010001X01X0X010101X111
mem[7754] = 37917
mem[63898] = 1020441
mem[48186] = 6776286
mem[64976] = 4166
mask = X001XX00X1111X11X00X0110101X1X101010
mem[60011] = 54362690
mem[44785] = 14835747
mem[11821] = 162
mem[19553] = 9995077
mem[45910] = 214595
mask = 0X01111011X101X1000100111X1X0XXX0111
mem[49462] = 814866
mem[50563] = 5803
mem[13772] = 1996784
mask = 000111X01X010011000110X1X0X0101000X1
mem[64423] = 105235
mem[52617] = 81683761
mem[35172] = 70451
mem[49737] = 256
mem[33210] = 455586090
mem[22581] = 182
mem[8818] = 434
mask = X0001110110111110001X010X000011111X0
mem[21950] = 4249
mem[1001] = 214247076
mem[52843] = 33456
mem[34466] = 728
mem[49384] = 31357234
mem[36737] = 4843
mask = 1X0011XXX00000X1X1011X0XX01110000011
mem[65191] = 2171
mem[31638] = 344
mem[58923] = 14214
mem[59055] = 1362547
mem[15108] = 195318
mask = 0010111111X101X1100XX10101X10X10X001
mem[7466] = 4866
mem[3536] = 3575
mem[49169] = 19106439
mem[33875] = 30297117
mem[20066] = 5397682
mem[18651] = 506641235
mem[31638] = 541
mask = 1000111001010X01000110100XX10010X1X0
mem[5697] = 15269
mem[41327] = 865222
mem[41400] = 80523535
mem[41457] = 2032
mask = 000X111011010X11XX0110X10X0100010XXX
mem[61659] = 15724
mem[37559] = 14276
mem[21098] = 50
mem[22776] = 10661
mem[40621] = 1973
mem[48571] = 3492782
mask = 10001X100101011X00XX000011X000001101
mem[4240] = 748914
mem[44593] = 8652
mem[31496] = 10966651
mem[14609] = 42203
mem[59392] = 399
mem[27914] = 1370
mask = 1X0X1111100000111101111X0XXX1X10101X
mem[61691] = 285691
mem[55023] = 51957222
mem[49120] = 13715470
mem[55045] = 2053
mem[37781] = 13494125
mask = 10001110X1010111X00100X0X1110X11X0X1
mem[39105] = 1328593
mem[24340] = 2543685
mem[52431] = 176
mask = 0X00111011000101X001000101010100X10X
mem[33425] = 123
mem[33903] = 72283570
mem[2666] = 506663
mask = 1X0XX11011010101000XX1101X1000000100
mem[13817] = 20411
mem[22028] = 4723
mem[9055] = 44968
mem[13157] = 3037
mask = XXX011X0110X0X11X001101101100010X101
mem[51483] = 495506871
mem[32527] = 605
mem[15801] = 113459
mask = 000X1010X0X1111X00010011100100X00X10
mem[52909] = 28078182
mem[39113] = 969683639
mem[37014] = 1041988
mask = 00X1111X110101111001X00100111X1X0011
mem[9619] = 385477
mem[45379] = 10011
mem[28156] = 41942
mem[39346] = 7110739
mask = XXX011111101010XX0010X0010100X0XX000
mem[37550] = 1235297
mem[57131] = 156045
mem[41570] = 713
mem[14840] = 830
mask = X0001110XX01011100010101X1110X1X1101
mem[52431] = 26933009
mem[12455] = 11903
mem[27708] = 887224
mask = X11X1110X10101110000X01011000X10101X
mem[57169] = 47699
mem[20342] = 644
mem[53136] = 874365
mem[22138] = 225094
mem[31310] = 45943
mask = 00101X100101011X100XX100000110010XX0
mem[29002] = 334
mem[28808] = 11128717
mem[64584] = 3481
mask = 1000X1101X010111X0X101101110000XX100
mem[52013] = 12610837
mem[48803] = 81625275
mem[48526] = 190697
mem[466] = 634639611
mem[6612] = 3318
mem[41026] = 92410
mask = 0000111001010111000X00100XX10010010X
mem[5056] = 993417
mem[21584] = 3373081
mask = 1000XX100101011110010000010X10000X01
mem[34559] = 6815
mem[6149] = 254307143
mem[1799] = 3464321
mem[47490] = 27818
mask = 100X1000XXX1XX01X011X000010101001X11
mem[36058] = 1021
mem[55222] = 216555
mem[10250] = 696
mask = 000X1111100100111101X011011011X0000X
mem[63750] = 561
mem[48132] = 1169
mem[46304] = 21184
mem[3366] = 6931762
mem[19670] = 57354682
mem[60180] = 1142
mask = 100011100X010111X001X000000000X00001
mem[55696] = 1346718
mem[40798] = 134344722
mem[15108] = 1122
mem[24212] = 864
mem[40100] = 1367042
mem[8818] = 19610351
mask = 00X11110X1X1011X00010X10110X0001101X
mem[1759] = 125492745
mem[35383] = 245406
mem[28283] = 703229
mem[41026] = 116097086
mem[24877] = 119355
mem[43747] = 94728
mask = 1000111010X1001XX10101010101X000X011
mem[37283] = 1680180
mem[39183] = 43995
mem[9014] = 41941652
mem[25378] = 5915217
mem[64548] = 3166
mask = X01X111011010X11000101XX00010X011X00
mem[12626] = 11376
mem[14670] = 89578705
mem[45765] = 3704
mem[54692] = 16057292
mem[42291] = 1226
mem[53392] = 524102
mask = X00X1110X10101X10001X01X00110X0X01X1
mem[14609] = 26483783
mem[20342] = 7487
mem[32554] = 32271503
mem[27722] = 43199
mem[33269] = 728090199
mask = 1110X111110101001001X0X0X11100X0001X
mem[39473] = 197988
mem[7779] = 4977773
mem[24823] = 15226380
mem[2064] = 221601
mem[25502] = 3061605
mem[43333] = 2413
mask = 1001111011X1010X0X0100110XX10X111001
mem[63963] = 16325
mem[64259] = 190108968
mem[23092] = 143
mask = X010111XX1010111X0011110010X001X1110
mem[8801] = 3339320
mem[42232] = 724
mem[51084] = 3938
mem[47824] = 116463
mem[34294] = 4000592
mask = 111X011111X1010X100XX0100X10010001X1
mem[45005] = 399
mem[42758] = 5831495
mask = 0X00111011X10111100111110001X11100X0
mem[58038] = 297528
mem[10454] = 123623
mem[2208] = 6782111
mem[46927] = 7516963
mem[38761] = 594918
mask = 100111X0110X0X111001X01010001X0X1X01
mem[6814] = 378
mem[7381] = 249509203
mem[54802] = 89683
mem[15084] = 295931
mem[1409] = 33792328
mask = 0001111XXXX1001X11011X01000XX01000X0
mem[30305] = 2645304
mem[20804] = 55687985
mem[38536] = 650758
mem[31659] = 3342918
mem[64835] = 147269231
mem[5056] = 395055093
mask = 000011X0X10101111X0110101X1X10111111
mem[5727] = 521314742
mem[55088] = 124475
mem[47490] = 52711
mask = 00X01X1XX101X11X00X11X101001X1010110
mem[22784] = 17799
mem[6047] = 300
mem[64898] = 105405
mem[30411] = 444576
mem[39714] = 3027
mem[13811] = 4033281
mask = 00001X1010X10111000101X00X1100100001
mem[46064] = 455365
mem[13837] = 223881282
mem[13837] = 114271853
mem[58817] = 242927
mem[2064] = 176633484
mem[37946] = 8386508
mem[57078] = 144941624
mask = 00X011X10X01010110011X1X0X01001XX10X
mem[20042] = 127795517
mem[63009] = 231577613
mem[8801] = 29002189
mem[39051] = 239841748
mem[22469] = 37946
mem[60639] = 44143112
mem[32149] = 633771
mask = 0X0011X01101X111010111X10X0101010001
mem[10127] = 3501050
mem[4720] = 702873
mem[58586] = 37830472
mem[54692] = 6750
mask = 100X0110110X01X110X1010000X1X0010X00
mem[9031] = 2373661
mem[47492] = 6765890
mem[28358] = 17836
mem[53001] = 1260
mem[28452] = 10259652
mem[55687] = 26179
mask = 0000111X010X010100010000X00X00001110
mem[7011] = 59306
mem[1429] = 65197311
mem[23697] = 1131168
mem[21315] = 627
mask = 0000111X110X0101100XX000100101101010
mem[5113] = 5682
mem[8004] = 123
mem[11578] = 1885
mem[61976] = 644
mem[54037] = 490885
mask = 1000111X10010X111001111011X0X1010100
mem[37908] = 14018
mem[33287] = 23863416
mem[44038] = 4176015
mem[11310] = 50194816
mem[23697] = 668207618
mask = XX00110X0X000X01X1010111100010101XX1
mem[36651] = 4719114
mem[61976] = 3799771
mem[1450] = 863
mem[41704] = 56437182
mask = 0000111011010XX1000100010000X10X1110
mem[15084] = 1947
mem[7589] = 34532623
mem[16135] = 16695
mask = 0X0XX11011010X110X0X1010101100000000
mem[58637] = 15834
mem[55985] = 811002
mem[1292] = 187066
mem[24612] = 90054417
mask = 10001X1X01010111X0011110X0000X100010
mem[7011] = 3880
mem[50826] = 832372
mem[39326] = 3860682
mem[6658] = 716
mem[48257] = 2880959
mem[63146] = 67563839
mask = X0001X100001X11100010010XX1100000000
mem[28608] = 50703005
mem[6149] = 82720
mem[52808] = 1187801
mem[44962] = 1974
mask = X0X01110X101XX11X00111100X0X1X001000
mem[28884] = 3732
mem[5862] = 90891
mem[45130] = 349356
mem[49462] = 976899
mem[4391] = 7609421
mem[12682] = 13724
mem[50922] = 616373
mask = 1000XX1011011X11X00100X100X0X0000000
mem[6919] = 1093
mem[8985] = 3677701
mem[31636] = 11751
mem[57500] = 33955
mem[4391] = 118569
mask = 100X1X1X110111111X0100X11001000000X0
mem[6919] = 305
mem[10315] = 17745
mask = X0011110101011X100111X0010011001XX10
mem[25505] = 3926
mem[15147] = 417445321
mem[44962] = 92006918
mem[60141] = 990579
mem[8478] = 556738
mask = X00XX111000XX011110110X1X0101000101X
mem[48803] = 380668169
mem[58011] = 938783
mem[53044] = 37340
mem[50207] = 92553
mem[48424] = 28446945
mem[52572] = 1678
mem[21832] = 150
mask = 000011111101010110X1XX1110000110XX10
mem[59890] = 7253
mem[31400] = 90
mem[9750] = 28283
mem[48571] = 577072
mem[44593] = 125859
mask = 1X001101X000X00111011011XX1010010001
mem[7996] = 43642
mem[51903] = 10448
mem[59055] = 15340
mask = 100011101101011100XX00001011000001XX
mem[32527] = 252219307
mem[12289] = 65205817
mem[57078] = 25737987
mem[5255] = 66
mem[4720] = 434040528
mask = 1X00110110000011010X1XX101X000101X1X
mem[27560] = 12121493
mem[26746] = 531
mem[63732] = 418686
mask = X10111X0111111XX00001111001000000001
mem[24587] = 203786512
mem[3720] = 26278895
mem[1263] = 13414622
mem[55374] = 207626224
mem[47623] = 22641
mem[1719] = 216991
mem[52572] = 201930
mask = 1X100XX1111X010X10000010001X010000X1
mem[58611] = 365536843
mem[3763] = 44414500
mem[8964] = 917
mem[9871] = 251036
mask = 000X11X01011011X010X001X001101101100
mem[50718] = 4335
mem[38354] = 14163
mem[10343] = 413021
mem[48686] = 115112
mask = 0000011X000110XX11011101001011001X0X
mem[57775] = 50195
mem[16604] = 10543218
mem[38274] = 7286689
mem[17680] = 20668
mem[59919] = 57930
mask = 00X11110010101X1XX0100101100X01001X1
mem[10579] = 9847648
mem[19249] = 1771
mem[60774] = 1408
mem[5697] = 6541425
mask = 000010100X01111X00X11011XXXX0X01011X
mem[9556] = 32443
mem[11396] = 5627
mem[38795] = 65631601
mem[1008] = 23252
mem[9392] = 802385
mem[12518] = 454170913
mem[13837] = 45280
mask = 0001000X0X111111100101100010X1000XX1
mem[49079] = 448
mem[14262] = 1621704
mem[3882] = 5042
mem[15341] = 5443083
mem[3292] = 616
mem[41026] = 125406
mask = 1X00111011010X111001011XX00100110000
mem[16135] = 542015991
mem[53314] = 392101
mem[21315] = 12937
mask = 100110000XXX10110000X1001010010100X0
mem[28751] = 131755533
mem[63740] = 6390359
mem[466] = 156702
mask = 01XX1X10110X0111000X111X1110X0X00100
mem[32231] = 13750
mem[21315] = 1758
mem[53067] = 15976128
mem[2027] = 5058
mem[28778] = 37493263
mem[2851] = 5277389
mask = XX00111X1101010010X11100001000101X1X
mem[42575] = 25301
mem[26666] = 318142129
mem[6149] = 60806635
mask = 00001XX0110101X10X01000100X110110001
mem[41945] = 3298
mem[34813] = 128424
mem[8949] = 502
mem[48160] = 20040
mem[5255] = 21655661
mem[30120] = 699
mem[41457] = 824415
mask = 100XX110X10101X110011001X1X011001XXX
mem[24943] = 449996801
mem[57496] = 877686
mem[12627] = 297
mask = 01011110X111X111000X011110100000011X
mem[4240] = 1772
mem[277] = 601643
mem[49914] = 92592528
mem[50287] = 1111
mem[47104] = 276570260
mask = 000XX11XXX010101101100111110X110X0XX
mem[39051] = 23560
mem[14386] = 369537680
mem[46064] = 270225086
mask = 000111X0XX1XX1110XX100101X0100101111
mem[18336] = 6341
mem[5697] = 289319505
mem[2887] = 1103
mem[13220] = 22335
mem[35] = 3139
mem[63416] = 3606
mask = 1000110000X000110101001X0X01X0010111
mem[19225] = 57
mem[37520] = 978
mask = 1000X11011X1011XX001X110X0100X010100
mem[64225] = 1527057
mem[53029] = 38306435
mem[10812] = 30350620"""

input_test = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

numbers = dict()
numbers_v2 = dict()
mask = ""


def apply_mask(m, n):
    value_after_mask = list(m.replace("X", "0"))
    length_diff = len(m) - len(n)
    for i in range(len(n) - 1, 1, -1):
        if m[i + length_diff] == "X":
            value_after_mask[i + length_diff] = n[i]
    return int("".join(value_after_mask), 2)


def apply_mask_v2(m, a, v):
    addresses_after_mask = list(m)
    length_diff = len(m) - len(a)
    for i in range(len(a) - 1, 1, -1):
        if m[i + length_diff] == "0":
            addresses_after_mask[i + length_diff] = a[i]
    apply_value_to_addresses(v, addresses_after_mask)


def apply_value_to_addresses(v, addr):
    try:
        x_index = addr.index("X")
        addresses = list(addr)
        addresses[x_index] = "0"
        apply_value_to_addresses(v, addresses)
        addresses[x_index] = "1"
        apply_value_to_addresses(v, addresses)
    except ValueError:
        numbers_v2[int("".join(addr), 2)] = v


for instruction in input.splitlines():
    if instruction.startswith("mask"):
        mask = instruction[7:len(instruction)]
        continue
    mem_addr = instruction[4:instruction.index("]")]
    val = int(instruction[instruction.index("=") + 2: len(instruction)])
    numbers[mem_addr] = apply_mask(mask, bin(val))
    apply_mask_v2(mask, bin(int(mem_addr)), val)

print "The answer to part 1 is", sum(numbers.values())
print "The answer to part 2 is", sum(numbers_v2.values())
