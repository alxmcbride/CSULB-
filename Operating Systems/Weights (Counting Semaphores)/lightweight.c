#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <stdio.h>
#include <unistd.h>


   key_t mykey;
   int semid;
int main(){
   mykey=ftok("scheduler.c",'c');
   if((semid= semget(mykey,1,IPC_CREAT | IPC_EXCL | 0660)) != -1){
      semctl(semid,0,SETVAL,5);
   }
   else{
      semid = semget(mykey,1,0660);
  }
  static struct sembuf Wait = {0,-2,SEM_UNDO};
  static struct sembuf Signal = {0,2,SEM_UNDO};
  int count=0;
  while (count < 5){
   if(semop(semid,&Wait, 1)!=-1){
      printf("LightWeight Starting\n");
  sleep(4);
      printf("LightWeight Ending\n");
      semop(semid, &Signal,1);
      sleep(8);
      count++;
   }
  }
  if(semctl(semid,0,GETVAL)==5){
    semctl(semid,0,IPC_RMID,0);
  }
  return 0;
}

