#include <stdio.h>
#include <stdlib.h>
#include "mkswap.h"
MKSWAP(int)

int main(int argc, char *argv[])
{

    int len = argc-1, *a = malloc(len*sizeof(int));
    for(int i = 1; i < argc; i++)
        a[i-1] = atoi(argv[i]);

    int *b = a, *e = a+len-1;
    do{
        while(*b%2) b++;
        while(!(*e%2)) e--;
    } while(e > b && swap(b++, e--));

    for(int i=0; i<len; i++) printf("[%d]:%d\n", i, a[i]);
    return 0;
}
