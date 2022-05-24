// https://www.codewars.com/kata/5b24bcecd74b5be066000054/train/c
// My solution
#include <stdbool.h>
#include <stdlib.h>

// A node in our linked list
typedef struct node
{
    int data;
    struct node *next;
} Node;

// Our stack, implemented as a wrapper around our linked list
typedef struct
{
    Node *root;
} Stack;

// Modify the code below to implement the key operations for our stack
void stack_push(Stack *stack, int data)
{
    Node *newNode = malloc(sizeof(Node));
    newNode->next = stack->root;
    newNode->data = data;
    stack->root = newNode;
}
int stack_pop(Stack *stack)
{
    Node *lastRoot = stack->root;
    if (lastRoot != NULL)
    {
        int value = lastRoot->data;
        stack->root = lastRoot->next;
        free(lastRoot);
        return value;
    }
    return 0;
}
int stack_peek(const Stack *stack)
{
    if (stack->root != NULL)
    {
        return stack->root->data;
    }
    return 0;
}
bool stack_is_empty(const Stack *stack)
{
    return stack->root == NULL;
}
