// https://www.codewars.com/kata/report-total-allocated-memory-ii/train/c
// My solution
#include <stdlib.h>

#define __SIZE_TO_MANAGER 256
#define __CRAP_OCCURENCE __SIZE_TO_MANAGER - 1

static void* mem_allocated[__SIZE_TO_MANAGER];
static unsigned long long size_allocated[__SIZE_TO_MANAGER] = {0};

static int index_to_alloc()
{
    for ( int i = 0; i < __SIZE_TO_MANAGER; ++i )
        if ( size_allocated[i] == 0 ) return i;
    return __CRAP_OCCURENCE;
}

static int index_to_pointer( void* pointer )
{
    for ( int i = 0; i < __SIZE_TO_MANAGER; ++i )
        if ( mem_allocated[i] == pointer ) return i;
    return __CRAP_OCCURENCE;
}

unsigned long long get_currently_allocated_size( void )
{
    unsigned long long size = 0;
    for ( int i = 0; i < __CRAP_OCCURENCE; ++i )
        size += size_allocated[i];
    return size;
}

void *mem_alloc( size_t size )
{
    int i = index_to_alloc();
    mem_allocated[i] = malloc( size );
    size_allocated[i] = size;
    return mem_allocated[i++];
}

void mem_free( void* pointer )
{
    int i = index_to_pointer( pointer );
    size_allocated[i] = 0;
    free(mem_allocated[i]);
}

// ...
#include <stdlib.h>

static size_t mem_bytes = 0;
unsigned long long get_currently_allocated_size(void) {
    return mem_bytes;
}

void *mem_alloc(size_t size) {
    size_t *ptr = malloc(sizeof(size_t) + size);
    if (ptr) {
        *ptr = size;
        mem_bytes += size;
        return &ptr[1];
    } else {
        return NULL;
    }
}

void mem_free(void *ptr) {
    if (ptr) {
        mem_bytes -= ((size_t*)ptr)[-1];
        free((size_t*)ptr - 1);
    }
}

// using tagged pointer. see <http://stackoverflow.com/a/35326444/638848>
