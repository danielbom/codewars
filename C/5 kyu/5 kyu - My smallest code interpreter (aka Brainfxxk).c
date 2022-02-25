// https://www.codewars.com/kata/my-smallest-code-interpreter-aka-brainf-star-star-k/train/c
// My solution
#include <stdlib.h>

// 'result' must contain at least one character - '\0'
char* brain_luck(char* code, char* input)
{
    unsigned char data[256] = {0};    // Memory
    unsigned char output[256] = {0};  // Output cache
    int di = 0, oi = 0, ii = 0;       // Pointers
    
    int length_code = strlen( code );
    for ( int i = 0; i < length_code; i++ ) {
        int braket = 1; // Used to ignore the block of instructions correct
        switch( code[i] ) {
            case '>': di++; break; // Ptr data increment
            case '<': di--; break; // Ptr data decrement
            case '+': data[di]++; break; // Data increment
            case '-': data[di]--; break; // Data decrement
            case '.': output[oi++] = data[di]; break; // Reserving output
            case ',': data[di] = input[ii++]; break;  // Consuming input
            case '[':
                if ( data[di] == 0 ) { // If the data is empty, then ignore the following instructions
                    while ( i < length_code && braket ) {
                        i++;
                        braket += ( code[i] == '[' ) - ( code[i] == ']' );
                    }
                    i++;
                } break;
            case ']':
                if ( data[di] != 0 ) { // If the data is not empty, then go back to reexecute the instructions
                    while ( i >= 0 && braket ) {
                        i--;
                        braket -= ( code[i] == '[' ) - ( code[i] == ']' );
                    }
                    i--;
                } break;
        } // End switch
    } // End for
    return strdup( output );
}

// ...
// xor eax, eax               31 c0
// jmp rel                    e9 xx xx xx xx
// inc byte [rbx]             fe 02
// dec byte [rbx]             fe 0a
// inc rdx                    48 ff c2
// dec rdx                    48 ff ca
// mov al, byte [rdx]         8a 02
// mov byte [rdx], al         88 02
// lodsb                      ac
// stosb                      aa
// test al, al                84 c0
// jnz re                     0f 85 xx xx xx xx
// mov rax, rdi               48 89 f8
// ret                        c3

#define _GNU_SOURCE
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>

typedef char *sptr;

char* jit(const char *program, char *code) {
    #define WRITE(str) do { \
        memcpy(code, str, sizeof(str) - 1); \
        code += sizeof(str) - 1; \
    } while (0)

    WRITE("\x31\xc0");

    sptr stack[512], *sp = stack;

    for (; *program ; program ++) {
        if (*program == '+') WRITE("\xfe\x02");
        else if (*program == '-') WRITE("\xfe\x0a");
        else if (*program == '>') WRITE("\x48\xff\xc2");
        else if (*program == '<') WRITE("\x48\xff\xca");
        else if (*program == '.') WRITE("\x8a\x02\xaa");
        else if (*program == ',') WRITE("\xac\x88\x02");
        else if (*program == '[') {
            *(sp++) = code;
            WRITE("\xe9\x00\x00\x00\x00");
        } else if (*program == ']') {
            if (stack == sp) {
                puts("Overclosed loop");
            }
            sptr top = *(-- sp), bot = code;
            WRITE("\x8a\x02\x84\xc0\x0f\x85\x00\x00\x00\x00");
            *(uint32_t *)(top + 1) = bot - (top + 5);
            *(uint32_t *)(bot + 6) = (top + 5) - (bot + 10);
        }
    }

    WRITE("\x48\x89\xf8\xc3");

    if (stack != sp) {
        puts("Unclosed loop");
    }

    return code;
}

typedef char* (*bffunc)(char *output, char *input, char *tape);

const size_t STORAGE_SIZE = 64 << 10, CODE_SIZE = 64 << 10;

char* brain_luck(char *program, char *input) {
    char *codemem = mmap(0, CODE_SIZE, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (! codemem)
        puts("mmap failed");

    char *out = calloc(1, STORAGE_SIZE);
    char *tape = calloc(1, STORAGE_SIZE);

    if (! out || ! tape)
        puts("malloc failed");

    jit(program, codemem);

    if (mprotect(codemem, CODE_SIZE, PROT_EXEC | PROT_READ))
        puts("mprotect failed");

    char *outend = ((bffunc) codemem)(out, input, tape);
    *outend = 0;

    if (munmap(codemem, CODE_SIZE))
        puts("munmap failed");

    free(tape);
    return out;
}

// ...
#include <stdlib.h>

#define STACK_SIZE 32768
#define OP(op, action) case op: do { action } while(0); break;

char* brain_luck(char* code, char* input) {
    char *data = calloc(sizeof(char), STACK_SIZE);
    char *result = calloc(sizeof(char), STACK_SIZE);
    char *os = result;
    char *is = input;

    for (char *sp = data, *ip = code; *ip; ip++) {
        switch(*ip) {
            OP('>', sp++;);
            OP('<', sp--;);
            OP('+', (*sp)++;);
            OP('-', (*sp)--;);
            OP('.', *os++ = *sp;);
            OP(',', *sp = *is++;);
            OP('[', if (*sp) break; for (size_t brackets = *ip++ == '['; brackets; brackets += (*ip == '[') - (*ip == ']'), ip++); ip--;);
            OP(']', if (!*sp) break; for (size_t brackets = *ip-- == ']'; brackets; brackets += (*ip == ']') - (*ip == '['), ip--););
        }
    }
    free(data);
    return result;
}

// ...
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct {
    int size;
    unsigned char *ptr;
} buffer_t;

void init(buffer_t *buffer, int size) {
    buffer->size = size;
    buffer->ptr = calloc(1, size);
}

void release(buffer_t *buffer) {
    if (buffer->ptr) {
        free(buffer->ptr);
        buffer->ptr = NULL;
        buffer->size = 0;
    }
}

unsigned char get(const buffer_t *buffer, int index) {
    if (index < 0 || index >= buffer->size) {
        return 0;
    }
    return buffer->ptr[index];
}

void set(buffer_t *buffer, int index, unsigned char value) {
    if (index < 0) {
        return;
    }
    if (index >= buffer->size) {
        int size1 = index + 100;
        int size2 = buffer->size * 2;
        int new_size = size1 > size2 ? size1 : size2;
        buffer->ptr = realloc(buffer->ptr, new_size);
        memset(buffer->ptr + buffer->size, 0, new_size - buffer->size);
        buffer->size = new_size;
    }
    buffer->ptr[index] = value;
}

// 'result' must contain at least one character - '\0'
char* brain_luck(char* code, char* input)
{
    buffer_t memory;
    buffer_t result;
    init(&memory, 1000);
    init(&result, 1000);

    int ip = 0;
    int ptr = 0;
    int out = 0;
    int steps = 0;
    // steps to avoid the bug in test cases
    while (ip >= 0 && code[ip] && steps++ < 100000) {
        switch (code[ip++]) {
            case '>': ptr++; break;
            case '<': ptr--; break;
            case '+': set(&memory, ptr, get(&memory, ptr) + 1); break;
            case '-': set(&memory, ptr, get(&memory, ptr) - 1); break;
            case '.': set(&result, out++, get(&memory, ptr)); break;
            case ',': set(&memory, ptr, *input); if (*input) { input++; } break;
            case '[': {
                if (!get(&memory, ptr)) {
                    for (int c = 1; code[ip] && c; ip++) {
                        if (code[ip] == '[') c++;
                        if (code[ip] == ']') c--;
                    }
                }
                break;
            }
            case ']': {
                if (get(&memory, ptr)) {
                    ip -= 2;
                    for (int c = 1; ip >= 0 && c; ip--) {
                        if (code[ip] == ']') c++;
                        if (code[ip] == '[') c--;
                    }
                    ip++;
                }
                break;
            }
        }
    }
    
    release(&memory);
    set(&result, out, 0);
    return (char *)result.ptr;
}