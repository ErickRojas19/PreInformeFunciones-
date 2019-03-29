def primos_hermano():
    
        n=int(input("Digite el numero que quiera saber si es primo hermano:"))
        primo_hermano=False
        if n%6!=0:
            primo_hermano=True
            for i in range(2,n+2):
                if n%i==0:
                    primo_hermano=False
                    break
        if primo_hermano:
            print(str(n)+" y "+str(n+1) + " Es primo hermano")
        else:
            print(str(n)+" y "+str(n+1) + " No es primo hermano")
    
primos_hermano()
            

            
