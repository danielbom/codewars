// https://www.codewars.com/kata/5b2771fab6989dd87d0000f1/train/c
// My solution
#include <stdbool.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *prev, *next;
} Node;

typedef struct
{
    Node *front, *back;
} Deque;

// Modify the code below to implement all of the key operations
void deque_push_front(Deque *deque, int data)
{
    Node *newNode = malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = deque->front;
    newNode->prev = NULL;
    if (deque->front != NULL)
        deque->front->prev = newNode;
    if (deque->back == NULL)
        deque->back = newNode;
    deque->front = newNode;
}
int deque_pop_front(Deque *deque)
{
    if (deque->front != NULL)
    {
        Node *front = deque->front;
        int data = front->data;
        if (front->next != NULL)
        {
            front->next->prev = NULL;
        }
        else
        {
            deque->back = NULL;
        }
        deque->front = front->next;
        free(front);
        return data;
    }
    return 0;
}
int deque_peek_front(const Deque *deque)
{
    if (deque->front != NULL)
        return deque->front->data;
    return 0;
}
void deque_push_back(Deque *deque, int data)
{
    Node *newNode = malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = deque->back;
    if (deque->front == NULL)
        deque->front = newNode;
    if (deque->back != NULL)
        deque->back->next = newNode;
    deque->back = newNode;
}
int deque_pop_back(Deque *deque)
{
    if (deque->back != NULL)
    {
        Node *back = deque->back;
        int data = back->data;
        if (back->prev != NULL)
        {
            back->prev->next = NULL;
        }
        else
        {
            deque->front = NULL;
        }
        deque->back = back->prev;
        free(back);
        return data;
    }
    return 0;
}
int deque_peek_back(const Deque *deque)
{
    if (deque->back != NULL)
        return deque->back->data;
    return 0;
}
bool deque_is_empty(const Deque *deque)
{
    return deque->front == NULL;
}

// ...
#include <stdbool.h>
#define NULL 0

typedef struct node
{
    int data;
    struct node *prev, *next;
} Node;

typedef struct
{
    Node *front, *back;
} Deque;

void link_two_nodes(Node *prev, Node *next)
{
    if (prev)
    {
        prev->next = next;
    }
    if (next)
    {
        next->prev = prev;
    }
}

void unlink_two_nodes(Node *prev, Node *next)
{
    if (prev && prev->next == next)
    {
        prev->next = NULL;
    }
    if (next && next->prev == prev)
    {
        next->prev = NULL;
    }
}

Node *unlink_node(Node *current)
{
    unlink_two_nodes(current->prev, current);
    unlink_two_nodes(current, current->next);
    return current;
}

Node *link_three_nodes(Node *prev, Node *current, Node *next)
{
    link_two_nodes(prev, current);
    link_two_nodes(current, next);
    return current;
}

Node *make_node(int data)
{
    Node *node = calloc(1, sizeof(Node));
    node->data = data;
    return node;
}

Node *free_node(Node *node)
{
    int data = node->data;
    free(node);
    return data;
}

void deque_add_node(Deque *deque, Node *prev, int data, Node *next)
{
    Node *added = link_three_nodes(prev, make_node(data), next);
    if (next == deque->front)
    {
        deque->front = added;
    }
    if (prev == deque->back)
    {
        deque->back = added;
    }
}

int deque_remove_node(Deque *deque, Node *remove)
{
    if (remove == deque->back)
    {
        deque->back = remove->prev;
    }
    if (remove == deque->front)
    {
        deque->front = remove->next;
    }
    return free_node(unlink_node(remove));
}

void deque_push_front(Deque *deque, int data)
{
    deque_add_node(deque, NULL, data, deque->front);
}

int deque_pop_front(Deque *deque)
{
    return deque_remove_node(deque, deque->front);
}

int deque_peek_front(const Deque *deque)
{
    return deque->front->data;
}

void deque_push_back(Deque *deque, int data)
{
    deque_add_node(deque, deque->back, data, NULL);
}

int deque_pop_back(Deque *deque)
{
    return deque_remove_node(deque, deque->back);
}

int deque_peek_back(const Deque *deque)
{
    return deque->back->data;
}

bool deque_is_empty(const Deque *deque)
{
    return !deque->front && !deque->back;
}