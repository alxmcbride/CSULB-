#include <stdlib.h> /* Needed for fork */
#include <stdio.h> /* Needed for printf. */
#include <stdbool.h> /* Needed for bool, optional. */
#include <unistd.h> /* Needed for fork and exit. */
#include <sys/wait.h>
int sum;
int main (int argc, char*argv[]) {
  int i;
  sum=0;
  printf("sleeping");
  sleep(5);
  int result= fork();  /* create a new process */
  char type = result ? 'P':'C';
  for (i=1; i<=10 ; i++) {
    sum += i;
    int charc=getchar();
    printf("sum is %c%d",type,sum);
    printf("%c\n",charc);
    result? sleep(1) : sleep(2);
    fflush(stdout);
  }
  if(argc>1 && result){
     wait3(&result,0,NULL);
}else{
     return 0;
  }
  return 0;
};

