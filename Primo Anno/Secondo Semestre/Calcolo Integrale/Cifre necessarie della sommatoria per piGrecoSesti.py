
rounded=16
import math
RoundedValue=round(math.pi/6,rounded)
Sum=0
i=0
lista=[]
cnt=0
while True:
    tmp=math.pow(-1,i)/(i+1)
    if Sum>RoundedValue:
        if tmp<0:
            Sum+=tmp
            lista.append(tmp)
    else:
        if tmp>0:
            Sum+=tmp
            lista.append(tmp)
    if RoundedValue==round(Sum,rounded):
        break
    i+=1


print(lista[-100:])
print("*"*100)
print("Dopo ",i," iterazioni è stato trovato il valore corrispondente a pi/6. Qui sopra sono riportati gli ultimi 100 valori") 
print("Il valore di p/6 è stato arrotondato a ",rounded," cifre dopo la virgola (limite di python)")   
    