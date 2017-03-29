#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]){
    for(int i = 1; i <= atoi(argv[1]); ++i){
        if(!(i % 15) ? printf("fizzbuzz\n") : 0) continue;
        if(!(i % 3) ? printf("fizz\n") : 0) continue;
        if(!(i % 5) ? printf("buzz\n") : 0) continue;
        printf("%d\n", i);
    }
    return 0;
}
