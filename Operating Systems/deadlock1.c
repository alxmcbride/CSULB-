/* file: deadlock1.c */
/* Rearrange the semaphores so the program no longer deadlocks */
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/wait.h>
#include <stddef.h>
#include <stdio.h>
#include <unistd.h>
void main () {
  /* The two semaphores are numbered 0 and 1 */
  struct sembuf Wait[2] ={{0,-1,SEM_UNDO},{1,-1,SEM_UNDO}};
  struct sembuf Signal[2] = {{0,1,SEM_UNDO},{1,1,SEM_UNDO}};
  struct sembuf OpList[2];
  int pid; /* for knowing who the parent is */
  key_t mykey;
  int semid;
  int waitstatus;

  mykey = ftok("./a.out",'a');
  /* request 2 semaphores for my programs only */
  semid = semget(mykey, 2, IPC_CREAT | 0600 );
  semctl(semid,  0, SETVAL,  1);
 semctl(semid,  1, SETVAL,  1);
  /* fork one child */
  pid = fork();
  if ( 0 != pid ) {
    /* parent */
    OpList[0]=Wait[0];
 //   sleep(1);
    OpList[1] = Wait[1];
    semop(semid, OpList, 2); /* get second lock */
    /* place critical section here */
    printf("start process %d \n", getpid() );
    sleep(1);
    printf("end process %d \n\n", getpid() );
    OpList[0]=Signal[1];
    OpList[1]=Signal[0];
    semop(semid,OpList, 2); /* surrender second lock */
    /* wait for any children to finish, the status is ignored */
    wait3(&waitstatus,0,NULL);
  } else {
    /* child */
    OpList[0]=Signal[1];
    OpList[1] = Signal[0];
    semop(semid,OpList,2);
 sleep(1);
    /* place critical section here */
    printf("start process %d \n", getpid() );
    sleep(1);
    printf("end process %d \n\n", getpid() );
    OpList[0]=Signal[0];
    OpList[1]=Signal[1];
    semop(semid, OpList,2);
  }
}

