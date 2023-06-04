```sh
rakamlar = (0,1,2,3,4,5,6,7,8,9)
rakamlar
```
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```sh
type(rakamlar)
```
tuple
```sh
sifir =(0)
sifir
```
0
```sh
type(sifir)
```
int
```sh
sifir =(0,)
type(sifir)
```
tuple
```sh
rakamlar = (0,1,2,3,4,5,6,7,8,9)
rakamlar
```
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```sh
rakamlar[5]
```
5
```sh
rakamlar[-1]
```
9
```sh
rakamlar[4:8]
```
(4, 5, 6, 7)
```sh
abc = (1,2,3,4,5,"ege","atalay")
type(abc)
```
tuple
```sh
abc.index("ege")
```
5
```sh
abc.index("Ege")
```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_20216\2860433024.py in <module>
  
----> 1 abc.index("Ege")

ValueError: tuple.index(x): x not in tuple
```sh
abc.remove("ege")
 ```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_20216\3809472131.py in <module>
----> 1 abc.remove("ege")

AttributeError: 'tuple' object has no attribute 'remove'
 
