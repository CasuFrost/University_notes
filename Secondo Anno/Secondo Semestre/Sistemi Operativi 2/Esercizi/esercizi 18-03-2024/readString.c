#include <stdio.h>
#include <string.h>

int main(){ 
    char s[1000];
    int i = 0;
    do{
        char tmp;
        tmp=getchar();
        if(tmp=='\n')break;
        s[i]=tmp;
        i++;
    }while(i<1000);

    printf("\n");
    printf("%s\n",s);
    
}