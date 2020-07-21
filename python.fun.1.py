Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> sukoku[1,2,3]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    sukoku[1,2,3]
NameError: name 'sukoku' is not defined
>>> sudoku = ['a','b','b']
>>> print sudoku
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(sudoku)?
>>> print(sudoku)
['a', 'b', 'b']
>>> for sudoku in range(2)
SyntaxError: invalid syntax
>>> for sudoku in range(2);
SyntaxError: invalid syntax
>>> for sudokuk in range(2):
	print sudoku
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(sudoku)?
>>> for sudoku in range(2):
	print(sudoku)

0
1
>>> print(sudoku)
1
>>> for i in range(3):
	print sudoku[i]
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(sudoku[i])?
>>> sudoku=['a','b','c']
>>> print(sudoku)
['a', 'b', 'c']
>>> for i in range(3):
	print(sudoku[i])

	
a
b
c
>>> print sudoku
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(sudoku)?
>>> print(sudoku)
['a', 'b', 'c']
>>> def sudoku(col,row,step):
	for col in range(9):
		for row in range(9):
			for step in range(9):
				sudoku[col,row,step] = str(col) + str(row) + str(step)

				
>>> rtn sudoku
SyntaxError: invalid syntax
>>> return sudoku
SyntaxError: 'return' outside function
>>> print(sudoku)
<function sudoku at 0x10dad3ae8>
>>> def sudoku(col,row,step):
	for col in range(9):
		for row in range(9):
			for step in range(9):
				sudoku[col,row,step] = str(col) + str(row) + str(step)
				return sudoku

			
>>> print(sudoku)
<function sudoku at 0x10dad3a60>
>>> for col in range(9):
		for row in range(9):
			for step in range(9):
				sudoku[col,row,step] = str(col) + str(row) + str(step)
				print(sudoku[col,row,step])

				
Traceback (most recent call last):
  File "<pyshell#37>", line 4, in <module>
    sudoku[col,row,step] = str(col) + str(row) + str(step)
TypeError: 'function' object does not support item assignment
>>> def sudoku(col,row,step)
SyntaxError: invalid syntax
>>> def sudoku(col,row,step):
	for col in range(9):
		for row in range(9):
			for step in range(9):
				sudoku[col,row,step] = str(col) + str(row) + str(step)
				print(sudoku[col,row,step])

				
>>> def sudoku(col,row,step):
	for col in range(9):
		for row in range(9):
			for step in range(9):
				sudoku[col,row,step] = str(col) + str(row) + str(step)
				return sudoku

			
>>> print(sudoku)
<function sudoku at 0x10dad3a60>
>>> 
>>> for col in range(9):
		for row in range(9):
			for step in range(9):
				print(sudoku[col,row,step])

				
Traceback (most recent call last):
  File "<pyshell#49>", line 4, in <module>
    print(sudoku[col,row,step])
TypeError: 'function' object is not subscriptable
>>> def sudoku(col,row,step):
	for col in range
	
SyntaxError: invalid syntax
>>> 
>>> for col in range(9):
	for row in range(9):
		for step in range(9);
		
SyntaxError: invalid syntax
>>> for col in range(9):
	for row in range(9):
		for step in range(9):
			print(str(col)+str(row)+str(step))

			
000
001
002
003
004
005
006
007
008
010
011
012
013
014
015
016
017
018
020
021
022
023
024
025
026
027
028
030
031
032
033
034
035
036
037
038
040
041
042
043
044
045
046
047
048
050
051
052
053
054
055
056
057
058
060
061
062
063
064
065
066
067
068
070
071
072
073
074
075
076
077
078
080
081
082
083
084
085
086
087
088
100
101
102
103
104
105
106
107
108
110
111
112
113
114
115
116
117
118
120
121
122
123
124
125
126
127
128
130
131
132
133
134
135
136
137
138
140
141
142
143
144
145
146
147
148
150
151
152
153
154
155
156
157
158
160
161
162
163
164
165
166
167
168
170
171
172
173
174
175
176
177
178
180
181
182
183
184
185
186
187
188
200
201
202
203
204
205
206
207
208
210
211
212
213
214
215
216
217
218
220
221
222
223
224
225
226
227
228
230
231
232
233
234
235
236
237
238
240
241
242
243
244
245
246
247
248
250
251
252
253
254
255
256
257
258
260
261
262
263
264
265
266
267
268
270
271
272
273
274
275
276
277
278
280
281
282
283
284
285
286
287
288
300
301
302
303
304
305
306
307
308
310
311
312
313
314
315
316
317
318
320
321
322
323
324
325
326
327
328
330
331
332
333
334
335
336
337
338
340
341
342
343
344
345
346
347
348
350
351
352
353
354
355
356
357
358
360
361
362
363
364
365
366
367
368
370
371
372
373
374
375
376
377
378
380
381
382
383
384
385
386
387
388
400
401
402
403
404
405
406
407
408
410
411
412
413
414
415
416
417
418
420
421
422
423
424
425
426
427
428
430
431
432
433
434
435
436
437
438
440
441
442
443
444
445
446
447
448
450
451
452
453
454
455
456
457
458
460
461
462
463
464
465
466
467
468
470
471
472
473
474
475
476
477
478
480
481
482
483
484
485
486
487
488
500
501
502
503
504
505
506
507
508
510
511
512
513
514
515
516
517
518
520
521
522
523
524
525
526
527
528
530
531
532
533
534
535
536
537
538
540
541
542
543
544
545
546
547
548
550
551
552
553
554
555
556
557
558
560
561
562
563
564
565
566
567
568
570
571
572
573
574
575
576
577
578
580
581
582
583
584
585
586
587
588
600
601
602
603
604
605
606
607
608
610
611
612
613
614
615
616
617
618
620
621
622
623
624
625
626
627
628
630
631
632
633
634
635
636
637
638
640
641
642
643
644
645
646
647
648
650
651
652
653
654
655
656
657
658
660
661
662
663
664
665
666
667
668
670
671
672
673
674
675
676
677
678
680
681
682
683
684
685
686
687
688
700
701
702
703
704
705
706
707
708
710
711
712
713
714
715
716
717
718
720
721
722
723
724
725
726
727
728
730
731
732
733
734
735
736
737
738
740
741
742
743
744
745
746
747
748
750
751
752
753
754
755
756
757
758
760
761
762
763
764
765
766
767
768
770
771
772
773
774
775
776
777
778
780
781
782
783
784
785
786
787
788
800
801
802
803
804
805
806
807
808
810
811
812
813
814
815
816
817
818
820
821
822
823
824
825
826
827
828
830
831
832
833
834
835
836
837
838
840
841
842
843
844
845
846
847
848
850
851
852
853
854
855
856
857
858
860
861
862
863
864
865
866
867
868
870
871
872
873
874
875
876
877
878
880
881
882
883
884
885
886
887
888
>>> for col in range(9):
	for row in range(9):
		for step in range(9):
			print(str(col)+str(row)+'012345678')

			
00012345678
00012345678
00012345678
00012345678
00012345678
00012345678
00012345678
00012345678
00012345678
01012345678
01012345678
01012345678
01012345678
01012345678
01012345678
01012345678
01012345678
01012345678
02012345678
02012345678
02012345678
02012345678
02012345678
02012345678
02012345678
02012345678
02012345678
03012345678
03012345678
03012345678
03012345678
03012345678
03012345678
03012345678
03012345678
03012345678
04012345678
04012345678
04012345678
04012345678
04012345678
04012345678
04012345678
04012345678
04012345678
05012345678
05012345678
05012345678
05012345678
05012345678
05012345678
05012345678
05012345678
05012345678
06012345678
06012345678
06012345678
06012345678
06012345678
06012345678
06012345678
06012345678
06012345678
07012345678
07012345678
07012345678
07012345678
07012345678
07012345678
07012345678
07012345678
07012345678
08012345678
08012345678
08012345678
08012345678
08012345678
08012345678
08012345678
08012345678
08012345678
10012345678
10012345678
10012345678
10012345678
10012345678
10012345678
10012345678
10012345678
10012345678
11012345678
11012345678
11012345678
11012345678
11012345678
11012345678
11012345678
11012345678
11012345678
12012345678
12012345678
12012345678
12012345678
12012345678
12012345678
12012345678
12012345678
12012345678
13012345678
13012345678
13012345678
13012345678
13012345678
13012345678
13012345678
13012345678
13012345678
14012345678
14012345678
14012345678
14012345678
14012345678
14012345678
14012345678
14012345678
14012345678
15012345678
15012345678
15012345678
15012345678
15012345678
15012345678
15012345678
15012345678
15012345678
16012345678
16012345678
16012345678
16012345678
16012345678
16012345678
16012345678
16012345678
16012345678
17012345678
17012345678
17012345678
17012345678
17012345678
17012345678
17012345678
17012345678
17012345678
18012345678
18012345678
18012345678
18012345678
18012345678
18012345678
18012345678
18012345678
18012345678
20012345678
20012345678
20012345678
20012345678
20012345678
20012345678
20012345678
20012345678
20012345678
21012345678
21012345678
21012345678
21012345678
21012345678
21012345678
21012345678
21012345678
21012345678
22012345678
22012345678
22012345678
22012345678
22012345678
22012345678
22012345678
22012345678
22012345678
23012345678
23012345678
23012345678
23012345678
23012345678
23012345678
23012345678
23012345678
23012345678
24012345678
24012345678
24012345678
24012345678
24012345678
24012345678
24012345678
24012345678
24012345678
25012345678
25012345678
25012345678
25012345678
25012345678
25012345678
25012345678
25012345678
25012345678
26012345678
26012345678
26012345678
26012345678
26012345678
26012345678
26012345678
26012345678
26012345678
27012345678
27012345678
27012345678
27012345678
27012345678
27012345678
27012345678
27012345678
27012345678
28012345678
28012345678
28012345678
28012345678
28012345678
28012345678
28012345678
28012345678
28012345678
30012345678
30012345678
30012345678
30012345678
30012345678
30012345678
30012345678
30012345678
30012345678
31012345678
31012345678
31012345678
31012345678
31012345678
31012345678
31012345678
31012345678
31012345678
32012345678
32012345678
32012345678
32012345678
32012345678
32012345678
32012345678
32012345678
32012345678
33012345678
33012345678
33012345678
33012345678
33012345678
33012345678
33012345678
33012345678
33012345678
34012345678
34012345678
34012345678
34012345678
34012345678
34012345678
34012345678
34012345678
34012345678
35012345678
35012345678
35012345678
35012345678
35012345678
35012345678
35012345678
35012345678
35012345678
36012345678
36012345678
36012345678
36012345678
36012345678
36012345678
36012345678
36012345678
36012345678
37012345678
37012345678
37012345678
37012345678
37012345678
37012345678
37012345678
37012345678
37012345678
38012345678
38012345678
38012345678
38012345678
38012345678
38012345678
38012345678
38012345678
38012345678
40012345678
40012345678
40012345678
40012345678
40012345678
40012345678
40012345678
40012345678
40012345678
41012345678
41012345678
41012345678
41012345678
41012345678
41012345678
41012345678
41012345678
41012345678
42012345678
42012345678
42012345678
42012345678
42012345678
42012345678
42012345678
42012345678
42012345678
43012345678
43012345678
43012345678
43012345678
43012345678
43012345678
43012345678
43012345678
43012345678
44012345678
44012345678
44012345678
44012345678
44012345678
44012345678
44012345678
44012345678
44012345678
45012345678
45012345678
45012345678
45012345678
45012345678
45012345678
45012345678
45012345678
45012345678
46012345678
46012345678
46012345678
46012345678
46012345678
46012345678
46012345678
46012345678
46012345678
47012345678
47012345678
47012345678
47012345678
47012345678
47012345678
47012345678
47012345678
47012345678
48012345678
48012345678
48012345678
48012345678
48012345678
48012345678
48012345678
48012345678
48012345678
50012345678
50012345678
50012345678
50012345678
50012345678
50012345678
50012345678
50012345678
50012345678
51012345678
51012345678
51012345678
51012345678
51012345678
51012345678
51012345678
51012345678
51012345678
52012345678
52012345678
52012345678
52012345678
52012345678
52012345678
52012345678
52012345678
52012345678
53012345678
53012345678
53012345678
53012345678
53012345678
53012345678
53012345678
53012345678
53012345678
54012345678
54012345678
54012345678
54012345678
54012345678
54012345678
54012345678
54012345678
54012345678
55012345678
55012345678
55012345678
55012345678
55012345678
55012345678
55012345678
55012345678
55012345678
56012345678
56012345678
56012345678
56012345678
56012345678
56012345678
56012345678
56012345678
56012345678
57012345678
57012345678
57012345678
57012345678
57012345678
57012345678
57012345678
57012345678
57012345678
58012345678
58012345678
58012345678
58012345678
58012345678
58012345678
58012345678
58012345678
58012345678
60012345678
60012345678
60012345678
60012345678
60012345678
60012345678
60012345678
60012345678
60012345678
61012345678
61012345678
61012345678
61012345678
61012345678
61012345678
61012345678
61012345678
61012345678
62012345678
62012345678
62012345678
62012345678
62012345678
62012345678
62012345678
62012345678
62012345678
63012345678
63012345678
63012345678
63012345678
63012345678
63012345678
63012345678
63012345678
63012345678
64012345678
64012345678
64012345678
64012345678
64012345678
64012345678
64012345678
64012345678
64012345678
65012345678
65012345678
65012345678
65012345678
65012345678
65012345678
65012345678
65012345678
65012345678
66012345678
66012345678
66012345678
66012345678
66012345678
66012345678
66012345678
66012345678
66012345678
67012345678
67012345678
67012345678
67012345678
67012345678
67012345678
67012345678
67012345678
67012345678
68012345678
68012345678
68012345678
68012345678
68012345678
68012345678
68012345678
68012345678
68012345678
70012345678
70012345678
70012345678
70012345678
70012345678
70012345678
70012345678
70012345678
70012345678
71012345678
71012345678
71012345678
71012345678
71012345678
71012345678
71012345678
71012345678
71012345678
72012345678
72012345678
72012345678
72012345678
72012345678
72012345678
72012345678
72012345678
72012345678
73012345678
73012345678
73012345678
73012345678
73012345678
73012345678
73012345678
73012345678
73012345678
74012345678
74012345678
74012345678
74012345678
74012345678
74012345678
74012345678
74012345678
74012345678
75012345678
75012345678
75012345678
75012345678
75012345678
75012345678
75012345678
75012345678
75012345678
76012345678
76012345678
76012345678
76012345678
76012345678
76012345678
76012345678
76012345678
76012345678
77012345678
77012345678
77012345678
77012345678
77012345678
77012345678
77012345678
77012345678
77012345678
78012345678
78012345678
78012345678
78012345678
78012345678
78012345678
78012345678
78012345678
78012345678
80012345678
80012345678
80012345678
80012345678
80012345678
80012345678
80012345678
80012345678
80012345678
81012345678
81012345678
81012345678
81012345678
81012345678
81012345678
81012345678
81012345678
81012345678
82012345678
82012345678
82012345678
82012345678
82012345678
82012345678
82012345678
82012345678
82012345678
83012345678
83012345678
83012345678
83012345678
83012345678
83012345678
83012345678
83012345678
83012345678
84012345678
84012345678
84012345678
84012345678
84012345678
84012345678
84012345678
84012345678
84012345678
85012345678
85012345678
85012345678
85012345678
85012345678
85012345678
85012345678
85012345678
85012345678
86012345678
86012345678
86012345678
86012345678
86012345678
86012345678
86012345678
86012345678
86012345678
87012345678
87012345678
87012345678
87012345678
87012345678
87012345678
87012345678
87012345678
87012345678
88012345678
88012345678
88012345678
88012345678
88012345678
88012345678
88012345678
88012345678
88012345678
>>> for col in range(9):
	for row in range(9):
		print(str(col)+str(row)+str(step))

		
008
018
028
038
048
058
068
078
088
108
118
128
138
148
158
168
178
188
208
218
228
238
248
258
268
278
288
308
318
328
338
348
358
368
378
388
408
418
428
438
448
458
468
478
488
508
518
528
538
548
558
568
578
588
608
618
628
638
648
658
668
678
688
708
718
728
738
748
758
768
778
788
808
818
828
838
848
858
868
878
888
>>>  for col in range(9):
	for row in range(9):
		print(str(col)+str(row)+str(step)
		      
SyntaxError: unexpected indent
>>> print(1,end='');print(2)
		      
12
>>> for col in range(9):
	for row in range(9):
		      print(col+row,end="")
		print()
		      
SyntaxError: unindent does not match any outer indentation level
>>> for col in range(9):
	for row in range(9):
		      print(col+row,end="");
		      print()

		      
0
1
2
3
4
5
6
7
8
1
2
3
4
5
6
7
8
9
2
3
4
5
6
7
8
9
10
3
4
5
6
7
8
9
10
11
4
5
6
7
8
9
10
11
12
5
6
7
8
9
10
11
12
13
6
7
8
9
10
11
12
13
14
7
8
9
10
11
12
13
14
15
8
9
10
11
12
13
14
15
16
>>> for col in range(9):
	for row in range(9):
		      print(str(col)+str(row),end="";
			    
SyntaxError: invalid syntax
>>> for col in range(9):
	for row in range(9):
		      print(str(col)+str(row),end="")

			    
000102030405060708101112131415161718202122232425262728303132333435363738404142434445464748505152535455565758606162636465666768707172737475767778808182838485868788
>>> for col in range(9):
	for row in range(9):
		      print(str(col)+str(row),end=""):
			    
SyntaxError: invalid syntax
>>> for col in range(9):
	for row in range(9):
		      print(str(col)+str(row),end="")
		print()
			    
SyntaxError: unindent does not match any outer indentation level
>>> for col in range(9):
	for row in range(9):
		      print(str(col)+str(row),end="")
	print()

			    
000102030405060708
101112131415161718
202122232425262728
303132333435363738
404142434445464748
505152535455565758
606162636465666768
707172737475767778
808182838485868788
>>> for col in range(9):
	for row in range(9):
		      print(str(col)+str(row)+' ',end="")
	print()

			    
00 01 02 03 04 05 06 07 08 
10 11 12 13 14 15 16 17 18 
20 21 22 23 24 25 26 27 28 
30 31 32 33 34 35 36 37 38 
40 41 42 43 44 45 46 47 48 
50 51 52 53 54 55 56 57 58 
60 61 62 63 64 65 66 67 68 
70 71 72 73 74 75 76 77 78 
80 81 82 83 84 85 86 87 88 
>>> for col in range(9):
	for row in range(9):
		      print(str(col+1)+str(row+1),end="")
	print()

			    
111213141516171819
212223242526272829
313233343536373839
414243444546474849
515253545556575859
616263646566676869
717273747576777879
818283848586878889
919293949596979899
>>> for col in range(9):
	for row in range(9):
		      print(str(col+1)+str(row+1)+' ',end="")
	print()

			    
11 12 13 14 15 16 17 18 19 
21 22 23 24 25 26 27 28 29 
31 32 33 34 35 36 37 38 39 
41 42 43 44 45 46 47 48 49 
51 52 53 54 55 56 57 58 59 
61 62 63 64 65 66 67 68 69 
71 72 73 74 75 76 77 78 79 
81 82 83 84 85 86 87 88 89 
91 92 93 94 95 96 97 98 99 
>>> for col in range(3):
	for row in range(3):
		print(str(col+1)+str(row+1)+' ',end="")
	print()

			    
11 12 13 
21 22 23 
31 32 33 
>>> row1=['one','two','three']
			    
>>> row2=['four','five','six']
			    
>>> row3=['seven','eight','nine']
			    
>>> names[1]=row1
			    
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    names[1]=row1
NameError: name 'names' is not defined
>>> names=[row1,row2,row3]
			    
>>> names
			    
[['one', 'two', 'three'], ['four', 'five', 'six'], ['seven', 'eight', 'nine']]
>>> for col in range(3):
	for row in range(3):
		print(names[row,col]+' ',end="")
	print()

			    
Traceback (most recent call last):
  File "<pyshell#98>", line 3, in <module>
    print(names[row,col]+' ',end="")
TypeError: list indices must be integers or slices, not tuple
>>> for col in range(3):
	for row in range(3):
		print(names[row][col]+' ',end="")
	print()

			    
one four seven 
two five eight 
three six nine 
>>> for col in range(3):
	for row in range(3):
		print(names[col,row]+' ',end="")
	print()

			    
Traceback (most recent call last):
  File "<pyshell#102>", line 3, in <module>
    print(names[col,row]+' ',end="")
TypeError: list indices must be integers or slices, not tuple
>>> for col in range(3):
	for row in range(3):
		print(names[row][col]+' ',end="")
	print()

one four seven 
two five eight 
three six nine 
>>> for col in range(3):
	for row in range(3):
		print(names[col][row]+' ',end="")
	print()

			    
one two three 
four five six 
seven eight nine 
>>> names
			    
[['one', 'two', 'three'], ['four', 'five', 'six'], ['seven', 'eight', 'nine']]
>>> for col in range(3):
	for row in range(3):
		print('col'+str(col)+'row'+str(row)+names[col][row]+' ',end="")
	print()

			    
col0row0one col0row1two col0row2three 
col1row0four col1row1five col1row2six 
col2row0seven col2row1eight col2row2nine 
>>> for col in range(3):
	for row in range(3):
		print('col'+str(col)+' row'+str(row)+' '+names[col][row]+' ',end="")
	print()

			    
col0 row0 one col0 row1 two col0 row2 three 
col1 row0 four col1 row1 five col1 row2 six 
col2 row0 seven col2 row1 eight col2 row2 nine 
>>> for col in range(3):
	for row in range(3):
		print('col'+str(col+1)+' row'+str(row+1)+' '+names[col][row]+' ',end="")
	print()

			    
col1 row1 one col1 row2 two col1 row3 three 
col2 row1 four col2 row2 five col2 row3 six 
col3 row1 seven col3 row2 eight col3 row3 nine 
>>> row1=['one','two','three']
			    
>>> row2=['four','five','six']
			    
>>> row3=['seven','eight','nine']
			    
SyntaxError: multiple statements found while compiling a single statement
>>> col1 = ['I','IV','VII']
			    
>>> col2=['II','V','VIII']
			    
>>> col3=['III','VI','IX']
			    
>>> names=[col1,col2,col3]
			    
>>> names
			    
[['I', 'IV', 'VII'], ['II', 'V', 'VIII'], ['III', 'VI', 'IX']]
>>> for col in range(3):
	for row in range(3):
		print('col'+str(col+1)+' row'+str(row+1)+' '+names[col][row]+' ',end="")
	print()

			    
col1 row1 I col1 row2 IV col1 row3 VII 
col2 row1 II col2 row2 V col2 row3 VIII 
col3 row1 III col3 row2 VI col3 row3 IX 
>>> for row in range(3):
	for col in range(3):
		print('col'+str(col+1)+' row'+str(row+1)+' '+names[col][row]+' ',end="")
	print()

			    
col1 row1 I col2 row1 II col3 row1 III 
col1 row2 IV col2 row2 V col3 row2 VI 
col1 row3 VII col2 row3 VIII col3 row3 IX 
>>>  col1 = ['   I','  IV',' VII']
			    
SyntaxError: unexpected indent
>>> col1 = ['I','IV','VII']
			    
>>> col2=['  II','   V','VIII']
			    
>>> col3=[' III','  VI','  IX']
			    
>>> names
			    
[['I', 'IV', 'VII'], ['II', 'V', 'VIII'], ['III', 'VI', 'IX']]
>>> for row in range(3):
	for col in range(3):
		print('col'+str(col+1)+' row'+str(row+1)+' '+names[col][row]+' ',end="")
	print()

col1 row1 I col2 row1 II col3 row1 III 
col1 row2 IV col2 row2 V col3 row2 VI 
col1 row3 VII col2 row3 VIII col3 row3 IX 
>>> 
			    
>>> 
			    
>>> for row in range(3):
	for col in range(3):
		input cellValue
			    
SyntaxError: invalid syntax
>>> 
			    
>>> for row in range(3):
	for col in range(3):
		newNames[col][row] = str(input())

			    

Traceback (most recent call last):
  File "<pyshell#136>", line 3, in <module>
    newNames[col][row] = str(input())
NameError: name 'newNames' is not defined
>>> def newNames[['','',''],['','',''],['','','']]
			    
SyntaxError: invalid syntax
>>> newNames=[['','',''],['','',''],['','','']]
			    
>>> or row in range(3):
	for col in range(3):
		newNames[col][row] = str(input())
			    
SyntaxError: invalid syntax
>>> for row in range(3):
	for col in range(3):
		newNames[col][row] = str(input())

			    

a
b
c
d
e
f
g
h
>>> i
			    
2
j
>>> newNames
			    
[['', 'c', 'f'], ['a', 'd', 'g'], ['b', 'e', 'h']]
>>> for row in range(3):
	for col in range(3):
		print('enter newNames col'+str(col)+' row'+str(row)+' ','')
		newNames[col][row] = str(input())

			    
enter newNames col0 row0  
for row in range(3):
	for col in range(3):
		print('enter newNames col'+str(col)+' row'+str(row)+' ','')
		newNames[col][row] = str(input())
enter newNames col1 row0  
enter newNames col2 row0  

enter newNames col0 row1  

enter newNames col1 row1  

enter newNames col2 row1  

enter newNames col0 row2  

enter newNames col1 row2  

enter newNames col2 row2  

>>> for row in range(3):
	for col in range(3):
		print('enter newNames col'+str(col+1)+' row'+str(row+1)+' ',del'')
		newNames[col][row] = str(input())
			    
SyntaxError: invalid syntax
>>> for row in range(3):
	for col in range(3):
		print('enter newNames col'+str(col+1)+' row'+str(row+1)+' ',end='')
		newNames[col][row] = str(input())

			    
enter newNames col1 row1 one
enter newNames col2 row1 two
enter newNames col3 row1 three
enter newNames col1 row2 four
enter newNames col2 row2 five
enter newNames col3 row2 six
enter newNames col1 row3 seven
enter newNames col2 row3 eight
enter newNames col3 row3 nine
>>> newNames
			    
[['one', 'four', 'seven'], ['two', 'five', 'eight'], ['three', 'six', 'nine']]
>>> for row in range(3):
	for col in range(3):
		print('enter newNames col'+str(col+1)+' row'+str(row+1)+' ',end='')
		newNames[col][row] = str(input())

			    
enter newNames col1 row1 yes
enter newNames col2 row1 
enter newNames col3 row1 no
enter newNames col1 row2 
enter newNames col2 row2 ok
enter newNames col3 row2 
enter newNames col1 row3 gums
enter newNames col2 row3 
enter newNames col3 row3 bum
>>> newNames
			    
[['yes', '', 'gums'], ['', 'ok', ''], ['no', '', 'bum']]
>>> for row in range(3):
	for col in range(3):
		print('|'newNames[col][row])
			    
SyntaxError: invalid syntax
>>> for row in range(3):
	for col in range(3):
		print('enter newNames col'+str(col+1)+' row'+str(row+1)+' ',end='')
		newNames[col][row] = str(input())

			    
enter newNames col1 row1 
enter newNames col2 row1 
enter newNames col3 row1 
enter newNames col1 row2 
enter newNames col2 row2 
enter newNames col3 row2 
enter newNames col1 row3 
enter newNames col2 row3 
enter newNames col3 row3 
>>> 
			    
>>> 
			    
>>> for row in range(3):
	for col in range(3):
		print('|'+str(newNames[col][row]))
	print'|'
			    
SyntaxError: invalid syntax
>>> for row in range(3):
	for col in range(3):
		print('|'+str(newNames[col][row]))
	print('|')
print('|')
			    
SyntaxError: invalid syntax
>>> for row in range(3):
	for col in range(3):
		print('|'+str(newNames[col][row]))
	print('|')

			    
|
|
|
|
|
|
|
|
|
|
|
|
>>> newNames
			    
[['', '', ''], ['', '', ''], ['', '', '']]
>>> for row in range(3):
	for col in range(3):
		print('enter newNames col'+str(col+1)+' row'+str(row+1)+' ',end='')
		newNames[col][row] = str(input())
for row in range(3):
	for col in range(3):
		print('|'+str(newNames[col][row]))
	print'|'
			    
SyntaxError: invalid syntax
>>> for row in range(3):
	for col in range(3):
		print('enter newNames col'+str(col+1)+' row'+str(row+1)+' ',end='')
		newNames[col][row] = str(input());
for row in range(3):
	for col in range(3):
		print('|'+str(newNames[col][row]))
	print'|'
			    
SyntaxError: invalid syntax
>>> for row in range(3):
	for col in range(3):
		print('enter newNames col'+str(col+1)+' row'+str(row+1)+' ',end='')
		newNames[col][row] = str(input())

			    
enter newNames col1 row1 I
enter newNames col2 row1 II
enter newNames col3 row1 III
enter newNames col1 row2 IV
enter newNames col2 row2 V
enter newNames col3 row2 VI
enter newNames col1 row3 VII
enter newNames col2 row3 VIII
enter newNames col3 row3 IX
>>> newNames
			    
for row in range(3):
	for col in range(3):
		print('|'+str(newNames[col][row]))
	print('|')
[['I', 'IV', 'VII'], ['II', 'V', 'VIII'], ['III', 'VI', 'IX']]
>>> for row in range(3):
	for col in range(3):
		print('|'+str(newNames[col][row]))
	print'|'
			    
SyntaxError: invalid syntax
>>> for row in range(3):
	for col in range(3):
		print('|'+str(newNames[col][row]))
	print('|')

			    
|I
|II
|III
|
|IV
|V
|VI
|
|VII
|VIII
|IX
|
>>> for row in range(3):
	for col in range(3):
		print('|'+str(newNames[col][row]),end='')
	print('|')

			    
|I|II|III|
|IV|V|VI|
|VII|VIII|IX|
>>> 
