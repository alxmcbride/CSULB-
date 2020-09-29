/*
   The parser piece for the minishell assignment
   Replace the part that prints the parsed command
   with you code that does the fork, exec, wait.
*/
#include <stdlib.h>
#include <unistd.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <sys/wait.h>
int main()
{
  char line[40];
  char *nargs[10];
  char *space = " ";
  char *where;
  while(1)
  {
    int i = 0;
    printf("Your command please: ");
    fgets(line,sizeof(line),stdin); //gets input from stream and saves into line with size
// with size
    line[strlen(line)-1] = '\0';    //sets it to end the string (c-string)
    where = strtok(line,space);     //
    nargs[i++] = where;
    while (where != NULL)
    {
      where = strtok(NULL,space);
      nargs[i++] = where;
    }


   int ch=fork();
   if(ch>0){
      wait3(&ch,0,NULL);
   }else{
      execvp(nargs[0],nargs);
   }
}
};

