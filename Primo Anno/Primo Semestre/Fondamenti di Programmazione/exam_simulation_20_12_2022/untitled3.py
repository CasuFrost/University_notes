def func4(triangles):
    # WRITE HERE YOUR CODE
    eliminatedTriples=0
    for k in range(len(triangles)-1):
        tmp=triangles[k]
        if  (round(tmp[0]**2+tmp[1]**2,3)==round(tmp[2]**2,3) or round(tmp[0]**2+tmp[2]**2,3)==round(tmp[1]**2,3) or round(tmp[1]**2+tmp[2]**2,3)==round(tmp[0]**2,3)):
              pass
        else:
            triangles.remove(tmp)
            eliminatedTriples+=1
            continue
    print(triangles)
    return triangles



triangles = [(3, 4, 5), (12, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
expected = [(3, 4, 5), (12, 36.05551, 34)]

#print(func4(triangles)==expected)



print("*"*50)

import os
directory = 'ex3/C'
namefile = 'a.txt'


# WRITE HERE YOUR CODE
def readAndUpdate(directory,i,finalList):
    with open(directory+"/"+i) as f:
        file=str(f.read()).split()
        for j in range(len(file)):
            if len(finalList)<j+1:
                finalList.append(0)
                finalList[j]+=int(file[j])
            else:
                finalList[j]+=int(file[j])
                
def ex1(directory, namefile):
    finalList=[]
    def search(directory):
        listaDir=os.listdir(directory)
        for i in listaDir:
            if ".txt" not in i:
                search(directory+"/"+i)  
            else:
                if namefile in i:
                    readAndUpdate(directory,i,finalList)      
        return finalList
    search(directory)
    return finalList

strings = {'a','b','c','de'}
n = 2
expected = ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb']

def concatenating(letter,lista,n,finalList):
    if n==1:
        for j in lista:
            finalList.append(letter+j)
    else:
        for j in lista:
            tmp = lista.copy()
            tmp.remove(j)
            concatenating(letter+j,tmp,n-1,finalList)
def sorting(finalList):
    for i in range(len(finalList)):
        for j in range(len(finalList)):
            if i != j:
                if len(finalList[i])>len(finalList[j]):
                    tmp = finalList[i]
                    finalList[i]=finalList[j]
                    finalList[j]=tmp
                if len(finalList[i])==len(finalList[j]):
                    tmp=max(finalList[i],finalList[j])
                    if finalList[i]!=tmp:
                        tmp2 = finalList[i]
                        finalList[i]=finalList[j]
                        finalList[j]=tmp2
                
def ex2(strings, n):
    # WRITE HERE YOUR CODE
    finalList=[]
    for i in strings:
        tmp = strings.copy()
        tmp.remove(i)
        concatenating(i,tmp,n-1,finalList)
  
    
    
    sorting(finalList)
    print(finalList)
    return finalList


print(ex2(strings, n)==expected)

























