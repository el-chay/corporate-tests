#define MKSWAP(T) \
void swap(T *a, T *b) { T tmp = *a; *a = *b; *b = tmp; }
