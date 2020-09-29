#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdio.h>

int main () {
  int myqueue;
  key_t mykey;
  int status;

  int msgsz = 10;
  struct Mybuf {
    long mtype;
    char mtext[msgsz];
  };

  struct Mybuf buf;


  mykey = ftok( ".cshrc" , 'a' );

  myqueue = msgget(mykey, IPC_CREAT | 0600 );
 if ( -1 == myqueue) {
    printf("error in msgget");
    return 1;
  }

  /* no special instructions, no flags */
  status = msgrcv(myqueue, (struct msgbuf *)&buf, msgsz, 0, 0);

  if ( -1 == status) {
    printf("error in msgrcv");
    return 1;
  }

  printf("%s\n", buf.mtext);


}

