from collections import OrderedDict
#se crea una lista con las llaves que seran ordenadas
a=[
    "b/34",
    "b/56",
    "b/2",
    "b/334",
    "a/12",
    "a/23",
    "a/34",
    "a/5",
    "c/34",
    "d/32",
    "d/3",
]
    
#se crea el diccionario donde se agregaran las llaves
b={}
for i in a:
    letter,number =i.split('/')#separa la cadena en numero y letra donde el separador es "/" donde letter es la letra y number es el numero y su sintaxis es letter "/" number
    number=int(number)#se convierte cada elemento de la lista number en un numero para poder ser ordenado
#se utiliza una condicional para agregar los numeros a una lista en base para asi agruparlos
    if letter in b:
        b[letter].append(number)   
    else:
        b[letter]=[number]
for i in b:
    b[i].sort()   #se ordenan los elementos de la listas que componen el diccionario

result=OrderedDict(sorted(b.items())) #se crea un ordereddict donde se van a ordenar las llaves y
                                      #se utiliza sorted para ordenarla en base a las llaves a,b,c,d
print(dict(result))#se imprime el resultado en su formato colleccion
