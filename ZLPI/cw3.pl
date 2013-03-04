/*cw.3*/

/*zad.1*/

result(X,Y,Z):-Z is X/Y.

zad_1:-
       write('Czytam plik...'),nl,
       see('/home/bogna/Projekty/studia/ZLPI/dane.txt'),
       read(L),
       seen,
       sum_list(L,Suma),
       length(L,Len),
       write('srednia arytmetyczna wynosi:'),
       result(Suma,Len,Avg),
       write(Avg).
