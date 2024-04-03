#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/fcntl.h>
#include <unistd.h>
#include<dirent.h>
#include <string.h>

#define EXECPATH "exec"
#define REGPATH "regular"

int prof;
void copyFileIntoPath(char* fileName,char* filePath, char* dstDir){
    //create a file called fileName into dstDir 
    char* tmp;
    /*strcpy(tmp,dstDir);
    strcat(tmp,"/");
    strcat(tmp,fileName);*/

    //open(tmp,O_CREAT);
    //close(tmp);
}

void recSearch(char* dirName, int depth){
    if(depth==0){return;}

    char *ident[100];
    ident[0]=' ';

    for(int i=0;i<=prof-depth;i++){
        strcat(ident,"  |   ");
    }
    
    DIR *openedDir=opendir(dirName);
    
    struct dirent *tmp;
    tmp=readdir(openedDir);

    while(tmp!=NULL){


        if(!strcmp(tmp->d_name,".")||!strcmp(tmp->d_name,"..")){
            tmp=readdir(openedDir);
            continue;
        }

        //Concatenare i path e leggere il file
        char* path[100];
        strcpy(path,dirName);
        strcat(path,"/");
        strcat(path,tmp->d_name);
        
        

        struct stat statbuf; //creo la struttura dati per le statistiche del file

    
        if(stat(path,&statbuf)==-1){ //leggo le statistiche del file
            printf("errore nella funzione stat");
            exit(1);
        }
        
        if(S_ISDIR(statbuf.st_mode)){
            printf("%s",ident);
            printf("è stata trovata la cartella : %s\n",path); 
            
            recSearch(path,depth-1);
        }
        else{
            
            if(statbuf.st_mode & S_IXUSR){
                //copy to exec path
                printf("%s",ident);
                printf("è stato trovato il file eseguibile : %s\n",path);
                copyFileIntoPath(tmp->d_name,path,EXECPATH);
            }
            else if(S_ISREG(statbuf.st_mode)){
                //copy to regular path
                printf("%s",ident);
                printf("è stato trovato il file regolare : %s\n",path);
                copyFileIntoPath(tmp->d_name,path,REGPATH);
            }

        }

        tmp=readdir(openedDir);
        

    }

    closedir(openedDir);
    
}


int main(int argc, char* argv[]){
    printf("verrà analizzata la directory %s.\nPer favore, si inserisca la profondità di ricerca : ",argv[1]);

    int n;
    scanf("%d",&n);
    prof=n;

    printf("\nverrà eseguita una ricerca fino ad una profondità %d.\n",n);

    struct stat statbuf; //creo la struttura dati per le statistiche del file

    
    if(stat(argv[1],&statbuf)==-1){ //leggo le statistiche del file
        printf("errore nella funzione stat");
        exit(1);
    }

    if(!S_ISDIR(statbuf.st_mode)){ //controllo se il file passato in input è una directory
        printf("c'è stato un errore, non è stata passata in input una directory\n");
        exit(1);
    }
    char* ident="";
    recSearch(argv[1],n);
}
