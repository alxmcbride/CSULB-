#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(){
  key_t mykey;
  mykey=ftok("scheduler.c",'c');
  int semid=semget(mykey,1,IPC_CREAT | 0600);
  int semval=semctl(semid,0,SETVAL,1);
  printf("ID:%d\n",semid);
  int result=fork();
  static struct sembuf Wait={0,-1,SEM_UNDO};
  static struct sembuf Signal={0,1,SEM_UNDO};
  for(int i=0;i<10;i++){
    if(result==0){
       semop(semid,&Wait,1);
       printf("N/S car entering the intersection\n");
       fflush(stdout);
       sleep(1);
printf("N/S leaving the intersection\n");
       semop(semid,&Signal,1);
       fflush(stdout);
    }else{
     semop(semid,&Wait,1);
     printf("E/W car entering the intersection\n");
       fflush(stdout);
     sleep(1);
     printf("E/W leaving the intersection\n");
    semop(semid,&Signal,1);
       fflush(stdout);
   }
 }
}

