#include <stdio.h>

int checkIfPal(char str[],int len){
    len--;
    int check=0;

    for(int i=0;i<len/2;i++){
        if(str[i]!=str[len-1-i]){
            check=1;
        } 
    }

    return check;
}