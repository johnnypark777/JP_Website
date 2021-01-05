/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

/* 3000test.c */
/* v1 Oct. 1, 2017 */
/* Licenced under the GPLv3, copyright Anil Somayaji */
/* You really shouldn't be incorporating parts of this in any other code,
   it is meant for teaching, not production */
#define _GNU_SOURCE 
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>

void sparsecheck(int filed, size_t s){
    int tracker;
    tracker = lseek(filed, 0, SEEK_HOLE);
    if(s != tracker && tracker > 0){
        printf("The file has holes in it. \n");
        return;
    } 
    printf("The file doesn't have any holes in it. \n");
   
 }

void report_error(char *error)
{
        fprintf(stderr, "Error: %s\n", error);

        exit(-1);
}

int main(int argc, char *argv[])
{
        struct stat statbuf;
        char *fn;
        int fd;
        size_t len, i, count;
        
        char *data;

        if (argc < 2) {
                if (argc < 1) {
                        report_error("no command line");
                        fprintf(stderr, "Usage: %s <file>\n", argv[0]); 
                } else {
                        report_error("Not enough arguments");
                        fprintf(stderr, "Usage: %s <file>\n", argv[0]); 
                }
        }

        fn = argv[1];

        if (stat(fn, &statbuf)) {
                report_error(strerror(errno));
        }

        len = statbuf.st_size;
        sparsecheck(fd, len);
        printf("File %s: \n", fn);
        printf("   inode %ld\n", statbuf.st_ino);
        printf("  length %ld\n", len);        

        if (S_ISREG(statbuf.st_mode)) {
                fd = open(fn, O_RDONLY);
                if (fd == -1) {
                        report_error(strerror(errno));
                }
                data = (char *) mmap(NULL, len,
                                     PROT_READ, MAP_SHARED, fd, 0);
                if (data == MAP_FAILED) {
                        report_error(strerror(errno));
                }

                count = 0;
                for (i=0; i<len; i++) {
                        if (data[i] == 'a') {
                                count++;
                        }
                }

                printf(" a count %ld\n", count);

                if (munmap(data, len) == -1) {
                        report_error(strerror(errno));                        
                }
                close(fd);
        }

        return 0;
}