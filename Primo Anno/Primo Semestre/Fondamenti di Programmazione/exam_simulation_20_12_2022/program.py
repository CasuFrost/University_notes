#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to do FIRST OF ALL:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and MATRICULATION NUMBER
 3) Change the directory name examPY in your matriculation number

To pass the exam you have to:
    - solve at least 3 func problems and
    - solve at least 1 rec problem
    - get a score greater or equal tu 18

The final score is the sum of the solved problems.
"""
name       = "MARCO"
surname    = "CASU"
student_id = "2046212"

#########################################

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
#
# To debug recursive functions you can turn off the recursive test setting
# DEBUG=True in the file grade.py
#
# DEBUG=True turns on also the STACK TRACE that allows you to know which
# line number in program.py generated the error.
################################################################################

# %%  ---- FUNC1 ----
''' func1: 2 points
Define a function func1(string_list) that takes as input a list of strings an
returns another list with only the strings that start with a capital letter.
The returned list has to be ordered by the number of letters in
increasing order.
'''
def func1(string_list):
    #print(sorted([x for x in string_list if x[0].isupper()],key= lambda x : -len(x)))
    return sorted([x for x in string_list if x[0].isupper()],key= lambda x : len(x))
    
        
# %%  ---- FUNC2 ----
''' func2: 2 points
Define a function func2(pathname) that takes as input a string representing
the path of a text file. The file has only rows with two words separated by
whitespace. The function must return a dictionary where the keys are the first
elements of a row and the values are sets with the second elements of a row.
Every second element of a row appears in the set corresponding to the key
of the first element of the same row.

Example:
Content of animals.txt:
    cat     meaow
    dog     woof
    cat     purr
The call func2('animals.txt') returns {'cat':{'meaow', 'purr'}, 'dog':{'woof'}
'''
def func2(pathname):
    diz={}
    with open(pathname) as f:
        l=[]
        while(True):
            a=f.readline()
            if  len(a)==0:
                break
            l.append(a.strip())
        
       
        for i in l:
            k=i.split()
            if k[0] not in diz:
                diz[k[0]]={k[1]}
            else:
                diz[k[0]].add(k[1])
    return diz

# %%  ---- FUNC3 ----
'''  func3: 2 points
Define a function func3(listA, listB, listC, pathname) that takes three lists
of numbers (integers or floats) and returns a new list where each element is
obtained considering the sum between the corresponding elements of the lists
listA and listB, sum multiplied for the corresponding element of listC.
The list built as above has to be written, one value for each row, in a text
file, with name pathname,
The function has to return the maximum value of the built list.
'''
def func3(listA, listB, listC, pathname):
    # YOUR CODE HERE
    newList=[]
    with open(pathname,"w") as f :
        for i in range(len(listA)):
            k=(listA[i]+listB[i])*listC[i]
            newList.append(k)
            f.write(str(k)+"\n")
    return max(newList)

    
# %%  ---- FUNC4 ----
""" func4: 6 points

Define the function func4(triangles) that takes as input a list of
triples of positive numbers and eliminates from the list all triples
that cannot be the sides of a right triangle. Each number in the
triple can be either cathetus or hypotenuse, and there is no
predetermined order.  The function must return the number of triples
deleted from the triangles list. The triangles list must be modified
in-place.  To evaluate whether a triangle is right-angled one can use
the Pythagorean theorem: the sum of the squares constructed on the
catheti must equal the square constructed on the hypotenuse.  For
comparisons, use the round(x,3) rounding function.

Example: if triangles = [(3, 4, 5), (12, 36.05551, 34),
                         (1,1,3), (8,8,8), (2, 3, 4)],
         the function func4(triangles) return the value 3 and modifies the list
         so that
         triangles = [(3, 4, 5), (12, 36.05551, 34)].

In fact, considering the expected result triangles = [(3, 4, 5), (12, 36.05551, 34)]
it holds the following:

| triplet            | check is True                                  |
| (3, 4, 5)          | round( 3² + 4² ), 3) == round( 5² ,3)          |
| (12, 36.05551, 34) | round( 12² + 34² ), 3) == round( 36.05551² ,3) |

NOTE: Break down the problem in small sub problems. Write small functions
for each sub problem. Compose everything together.

"""

def func4(triangles):
    # WRITE HERE YOUR CODE
    list2=[]
    eliminatedTriples=0
    for k in triangles:
        print(k)
        if  (round(k[0]**2+k[1]**2,3)==round(k[2]**2,3) or round(k[0]**2+k[2]**2,3)==round(k[1]**2,3) or round(k[1]**2+k[2]**2,3)==round(k[0]**2,3)):
              list2.append(k)
        else:
            #triangles.remove(k)
            eliminatedTriples+=1
    triangles[:]=list2
    return eliminatedTriples



# %%  ---- FUNC5 ----
""" func5: 6 points
Define a function func5(img, filename) that returns a copy of the image img
flipped with respect to the vertical axis and saves the image in the file
with path as the filename string taken in input. The function returns the
color of the pixel in position (0,0) of the new image.
"""
import images
def func5(img, filename):
    # WRITE HERE YOUR CODE
    
    flippedMatrix = [] 
    
    for i in range(len(img)):
        tmp=[]
        for j in reversed(range(len(img[0]))):
            tmp.append(img[i][j])
        flippedMatrix.append(tmp)
        
    images.save(flippedMatrix,filename)
    return flippedMatrix[0][0]


# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex1: 6 points

Define the recursive function ex1 that takes as input a string
'directory' and a string 'namefile'. The function must search recursively
within the directory given by directory and in all subdirectories for
all files with name equal to namefile.  Such files are to be
interpreted as text files. Each text file contains only positive
numeric strings. Files with the same namefile always have the same
number of numeric strings.  The function must return a list of
integers obtained by summing the numeric strings of the files found,
position by position.

Example: if two files with the SAME namefile are found and those
files contain the sequences "11 23 90" and "11 77 0," the function ex3
returns the list [22, 100, 90].

We suggest using the functions os.listdir, os.path.isfile and
os.path.isdir and NOT to use the os.join function in Windows (use
concatenation between strings with the '/' character).

It is forbidden to use the os.walk function.

NOTE: Break down the problem in small sub problems. Write small
functions for each sub problem. Compose everything together.
"""

import os

def readAndUpdate(directory,i,finalList):
    with open(directory+"/"+i) as f:
        file=str(f.read()).split()
        for j in range(len(file)):
            if len(finalList)<j+1:
                finalList.append(0)
                finalList[j]+=int(file[j])
            else:
                finalList[j]+=int(file[j])
def search(directory,finalList,namefile):
    listaDir=os.listdir(directory)
    for i in listaDir:
        if ".txt" not in i:
            search(directory+"/"+i,finalList,namefile)  
        else:
            if namefile in i:
                readAndUpdate(directory,i,finalList)      
    return finalList                
def ex1(directory, namefile):
    finalList=[]
    search(directory,finalList,namefile)
    return finalList


# %% Ex2
"""
Ex2: 3+3 points
Define a recursive function (or one that uses recursive functions)
ex2(strings, n) that takes a set 'strings' and an integer 'n' and
recursively generates all possible strings that can be constructed by
concatenating n strings of the set strings. The function must return
all strings constructed. The function can return either a set with all
strings constructed (3 points), or a sorted list (6 points).  The list
is ordered considering the descending order of the length of the
strings and, in case of parity, considering the alphabetical order.

Example: if strings={'a','b','c','de'}, the function ex2(strings, 2)
returns the set {'ab','ac','ade','ba','ca','dea','bc','bde','cb','deb','cde','dec'} (6 points)
or the list ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb'] (9 points)
"""
def concatenating(letter,lista,n,finalList):
    if n==0:
        return False
    if n==1:
        concatenating(letter,lista,n-1,finalList)  
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
    return finalList

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)







