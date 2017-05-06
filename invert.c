#include <stdio.h>
#include "mkswap.h"
MKSWAP(char)

int main(){
    char redivider[] = "redivider";
    for(char *b = redivider, *e = redivider+8; e > b; b++, e--){
        printf("b:%c - e:%c\n", *b, *e);
        swap(b, e);
    }
    puts(redivider);
}
