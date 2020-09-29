#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>

int semid, count;
key_t mykey;

int main(){
 mykey = ftok("copy.c",'d');
 if(( semid = semget(mykey, 4, IPC_CREAT | IPC_EXCL | 0660)) != -1){
   semctl(semid,0,SETVAL, 1);//Setting as unlocked for readers
   semctl(semid,1,SETVAL, 1); //Setting as unlocked for readers
   semctl(semid,2,SETVAL, 1); //Settig as unlocked for counterlock
   semctl(semid,3,SETVAL,0); //setting counter to 0
}else{
   semid = semget(mykey,4,0660);
}
   static struct sembuf Lock[3] ={ {0,-1,SEM_UNDO}, {1,-1,SEM_UNDO},{2,-1,SEM_UNDO}};
   static struct sembuf UnLock[3]={ {0, 1, SEM_UNDO}, {1,1,SEM_UNDO}, {2,1,SEM_UNDO}};
   static struct sembuf  Decrement={3,-1,SEM_UNDO};
   static struct sembuf  Increment={3,1,SEM_UNDO};

   struct sembuf OpList[2];

   count=0;

   while(count < 5){
     OpList[0] = Lock[0];
     OpList[1] = Lock[2];
     if((semop(semid, OpList, 2)) != -1){
         if((semctl(semid, 3, GETVAL))==0)semop(semid, &Lock[1],1);
            semop(semid, &Increment,1);

         OpList[0]=UnLock[2];
         OpList[1] = UnLock[0];

         semop(semid, OpList, 2);

         printf("Reading\n");
         sleep(4);
         printf("Done reading\n");
         semop(semid, &Lock[2], 1);
         semop(semid, &Decrement, 1);
         if((semctl(semid, 3,GETVAL))==0) semop(semid,&UnLock[1], 1);
          semop(semid, &UnLock[2],1);
         sleep(4);
         count++;
      }
   }
  if ((semctl(semid,0,GETVAL)) ==1 &&( semctl(semid,1,GETVAL)) == 1 &&( semctl(semid, 2, GETVAL)) == 1 && (semctl(semid, 3, GETVAL) == 0)){
    semctl(semid, 0, IPC_RMID, 0);
  }
 return 0;

};


