kobieta(ewa).
kobieta(wiesia).
kobieta(anna).
kobieta(krysia).
kobieta(bogna).

mezczyzna(piotr).
mezczyzna(krzysztof).
mezczyzna(olek).
mezczyzna(wacek).
mezczyzna(kamil).
mezczyzna(szymon).

rodzic(anna,krzysztof).
rodzic(anna,ewa).
rodzic(olek,krzysztof).
rodzic(olek,ewa).
rodzic(wacek,wiesia).
rodzic(krysia,wiesia).
rodzic(wiesia,kamil).
rodzic(wiesia,bogna).
rodzic(krzysztof,kamil).
rodzic(krzysztof,bogna).
rodzic(ewa,szymon).
rodzic(piotr,szymon).

wiek(ewa,40).
wiek(wiesia,45).
wiek(bogna,20).
wiek(krysia,70).
wiek(anna,65).

wiek(piotr,45).
wiek(krzysztof,50).
wiek(olek,80).
wiek(wacek,76).
wiek(kamil,10).
wiek(szymon,19).

ojciec(X,Y):-mezczyzna(X),rodzic(X,Y).
matka(X,Y):-kobieta(X),rodzic(X,Y).
rodzenstwo(X,Y):-matka(Z,X),matka(Z,Y),X\=Y.
dziadek(X,Y):-mezczyzna(X),ojciec(X,Z),ojciec(Z,Y).
wuj(X,Y):-mezczyzna(X),rodzic(Z,Y),rodzenstwo(Z,X).
ciocia(X,Y):-kobieta(X),rodzic(Z,Y),rodzenstwo(Z,X).
kuzyn(X,Y):-mezczyzna(X),rodzenstwo(A,B),rodzic(A,X),rodzic(B,Y).
przodek(X,Y):-rodzic(X,Y).
przodek(X,Y):-przodek(X,Z),rodzic(Z,Y).

starszy(X,Y):-wiek(X,B),wiek(Y,A),B>A.
mlodszy(X,Y):-wiek(X,B),wiek(Y,A),B<A.
uczen(X):-wiek(X,A),A>5,A<20.
pracownik(X):-wiek(X,A),A>19.

wiekszy(X,Y,Z):-X>Y,Z=X.
wiekszy(X,Y,Z):-X<Y,Z=Y.

%%%%%ZADANIE 4%%%%%%%%%%
odcinek(punkt(1,2),punkt(A)) = odcinek(B,punkt(1,2)). %%% result NO
odcinek(punkt(1,2),punkt(A,C)) = odcinek(B,punkt(1,2)). %%% result: A=1, C=2, B=punkt(1,2)
odcinek(punkt(1,2), punkt(A,B)) = odcinek(B,punkt(1,C)). %%% result A=1, B=punkt(1,2), C=punkt(1,2)
punkt(X,Y,Z)=punkt(X1,Y1,Z1). %%% result X1=X,Y1=Y,Z1=Z
lot(A,londyn)=lot(londyn,paryz). %%% result NO
′student′=student. %%% result YES
′Student′=student. %%% result NO
′Student′=Student. %%% result Student = 'Student'
Student=”Student”. %%% result Student = [83,116,117,100,101,110,116]
f(X,X)=f(a,b). %%% result NO
f(X,a(b,c))=f(Z,a(Z,c)). %%% result Z=b, X=b
1+2=3. %%% result NO
1+2=1+2. %%% result YES
1+2==2+1. %%% result NO
1+2=:=3. %%% result YES
1+2=\=3. %%% result NO
X=X. %%% result YES
X==X %%% result YES
X=Y %%% result Y=X.
X==Y %%% result NO.

%%%%%ZADANIE 5%%%%%%%%
append([b,c,[s,a],a],[a],X). %%% result X=[b,c,[s,a],a,a]
append([a],[b],[a,b]). %%% result YES
append(L1,L2,[b,c,[s,a]]). %%% result SERIA ROZWIAZAN: L1=[], L2=[b,c,[s,a]]; L1=[b], L2=[c,[s,a]] itd...

member(a,[b,c,[s,a],a]). %%% result true;
member(a,[b,c,[s,a]]). %%% result NO.
member([s,a],[b,c,[s,a]]). %%% result true.
member(X,[a,b,c]). %%% result X=a, X=b, X=c
member(a,X) %%% result nieskonczona liczba rozwiazan gdzie a moze byc w X




















