/* Make-a-Swap Macro.
 * The macro will produce a swap function with the requested type.
 * The function will be local to the file/unit.
 * It will return the value contained in the first parameter.
 * Example:
 * MKSWAP(char) will generate:
 * static char swap(char *a, char *b) { ... return *a; }
 */
#define MKSWAP(T) \
static T swap(T *a, T *b) { T tmp = *a; *a = *b; *b = tmp; return *a; }
