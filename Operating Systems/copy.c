#include <sys/types.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

int main (int argc, char* argv[]) {
  int src_fd;
  int dest_fd;
  char filebuf[256]; /* a small buffer used to copy the file */
  ssize_t readSize;

  src_fd = open(argv[1],O_RDONLY);

  if (src_fd < 0){
    printf("File does not exist\n");
    return 0; }

  if((dest_fd = open (argv[2], O_EXCL, S_IRUSR))>=0){
     printf("File already exists\n");
     return 0;
}else{
    dest_fd= open(argv[2], O_CREAT|O_WRONLY, S_IRUSR);
}

  while (( readSize = read(src_fd, filebuf, sizeof(filebuf)-1)) > 0)
  {
    write(dest_fd,filebuf,readSize);
  }
  close(src_fd);
  close(dest_fd);
  return 0;
}

