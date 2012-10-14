kobieta(ewa).
kobieta(anna).
kobieta(marta).
kobieta(iza).
kobieta(daria).
kobieta(zofia).

mezczyzna(piotr).
mezczyzna(adam).
mezczyzna(pawel).
mezczyzna(artur).
mezczyzna(szymon).

rodzic(ewa,anna).
rodzic(ewa,adam).
rodzic(anna,marta).
rodzic(anna,pawel).
rodzic(iza,szymon).
rodzic(artur,szymon).
rodzic(piotr,adam).
rodzic(piotr,anna).
rodzic(adam,iza).
rodzic(zofia,iza).

wiek(ewa,90).
wiek(piotr,90).
wiek(anna,70).
wiek(adam,70).
wiek(zofia,70).
wiek(marta,50).
wiek(pawel,50).
wiek(iza,50).
wiek(artur,50).
wiek(szymon,30).

matka(X,Y):-kobieta(X),rodzic(X,Y).
ojciec(X,Y):-mezczyzna(X),rodzic(X,Y).
rodzenstwo(X,Y):-matka(Z,X),matka(Z,Y),X\=Y.
dziadek(X,Y):-ojciec(X,Z),ojciec(Z,Y),mezczyzna(X).
wuj(X,Y):-rodzenstwo(X,Z),rodzic(Z,Y),mezczyzna(X).
kuzyn(X,Y):-rodzic(Z,X),rodzic(R,Y),rodzenstwo(Z,R).
przodek(X,Y):-rodzic(X,Y).
przodek(X,Y):-przodek(X,Z),rodzic(Z,Y).

starszy(X,Y):-wiek(X,A),wiek(Y,B),A>B.
mlodszy(X,Y):-wiek(X,A),wiek(Y,B),A<B.

uczen(X):-wiek(X,Y),Y<19,Y>6.
pracownik(X):-wiek(X,Y),Y>19,Y<65.
emeryt(X):-wiek(X,Y),Y>65.

wiekszy(X,X,X).
wiekszy(X,Y,Z):-
