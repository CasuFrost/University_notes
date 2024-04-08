#include <sys/types.h>
#include <unistd.h>

int main(){
    
    pid_t pid = fork();

    if(pid==0){
        //child
        printf("sono il figlio\n");
    }else{
        printf("sono il padre\n");
        //parent
    }

    exit(0);
}