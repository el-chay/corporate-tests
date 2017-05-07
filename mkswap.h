#define MKSWAP(T) \
static T *swap(T *a, T *b) { T tmp = *a; *a = *b; *b = tmp; return a; }
