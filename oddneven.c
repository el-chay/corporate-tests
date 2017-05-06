#include <stdio.h>
#include "mkswap.h"
MKSWAP(int)

int main()
{
    int a[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    int *b = a, *e = a+9;
    while(e > b){
        if(*b%2){
            b++;
            continue;
        }
        if(!(*e%2)){
            e--;
            continue;
        }
        swap(b, e);
        b++; e--;
    }
    for(int i=0; i<10; i++) printf("(%d):%d\n", i, a[i]);
    return 0;
}
