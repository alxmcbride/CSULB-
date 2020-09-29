#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <iostream>
using namespace std;

int main () {
  int clientToServer, serverToClient,multiplicand, multiplier, clientToServer_fd, serverToClient_fd;
  clientToServer = mkfifo("clientToServer",0600);
  serverToClient = mkfifo("serverToClient",0600);
  clientToServer_fd = open("clientToServer",O_WRONLY);
  serverToClient_fd = open("serverToClient",O_RDONLY);

  for(int i = 0; i < 5; i++){
     cin >>multiplicand;
     write(clientToServer_fd,&multiplicand, sizeof(multiplicand));
     cin >> multiplier;
     write(clientToServer_fd, &multiplier, sizeof(multiplier));
     }
  close(clientToServer_fd);
  close(serverToClient_fd);
  return 0;
};

