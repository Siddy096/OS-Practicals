#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>

int main() {
    pid_t pid;

    pid = fork();

    if(pid < 0){
        fprintf(stderr, "Fork Failed");
        return 1;
    }
    else if(pid == 0){
        printf("Iam the child, my pid is %d\n", getpid());
        printf("My Parent's pid is %d\n", getpid());
    }
    else{
        printf("Iam the parent, my pid is %d\n", getpid());
        wait(NULL);
    }

    return 0;
}