El algoritmo para validar un DNI es muy sencillo: se toma la parte del numero del documento y se divide entre 23 y se obtiene el resto. Ese resto es un índice que se consulta en una tabla de letras. La letra correspondiente al índice es la que debería tener un DNI válido. Por tanto, si la letra del DNI concuerda con la que hemos obtenido, es que es válido.

La tabla en cuestión es esta:

Resto |	Letra
0 	T
1	R
2	W
3	A
4	G
5	M
6	Y
7	F
8	P
9	D
10	X
11	B
12	N
13	J
14	Z
15	S
16	Q
17	V
18	H
19	L
20	C
21	K
22	E
