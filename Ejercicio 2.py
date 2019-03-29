def primos():
    n=int(input("Digite el numero que quiera saber si es primo:"))
    primo=True
    for i in range(2,n):
        if n%i==0:
            primo=False
    if primo:
        print("Es primo")
    else:
        print("No es primo")
primos()
            
