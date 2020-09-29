#include <limits.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

using namespace std;

int main(int argc, char * argv[]){
 int multiplicand,multiplier,product;
 int toParent[2], toChild[2];//0- parent to child 1-child to parent
 pipe(toParent),pipe(toChild);
  if(fork()==0){
  while(true){
  close(toChild[1]);
  close(toParent[0]);
   if( (read(toChild[0],&multiplicand,sizeof(multiplicand)))==0){
    break;
   }
   if( (read(toChild[0],&multiplier,sizeof(multiplier)))==0){
     break;
   }
 product=multiplicand * multiplier;
    write(toParent[1],&product,sizeof(product));
   }
  close(toChild[0]);
  close(toParent[1]);
  }else{
 for(int i=0;i<5;i++){
 close(toChild[0]);
 close(toParent[1]);
 cin>>multiplicand;
 write(toChild[1],&multiplicand,sizeof(multiplicand));
 cin>>multiplier;
 write(toChild[1],&multiplier,sizeof(multiplier));
 read(toParent[0],&product,sizeof(product));
 printf("Result: %d\n",product);
  }
 close(toChild[1]);
 close(toParent[0]);
}


}

