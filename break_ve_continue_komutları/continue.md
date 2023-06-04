# continue
**continue** komutu döngünün içindeki koşul yerine geldiğinde sıradaki hamleyi atlar.
```sh
i = 0
while (i < 20):
    if (i == 5):
        continue
        
    print("i: ", i)
    i += 1
```
i:  0

i:  1

i:  2

i:  3

i:  4

i:  6

i:  7

...

...

...

i:  19
