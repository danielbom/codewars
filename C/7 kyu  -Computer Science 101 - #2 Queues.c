// https://www.codewars.com/kata/5b26360bd74b5b2ea5000026/train/c
// My solution
#include <stdbool.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *next;
} Node;

typedef struct
{
    Node *front, *back;
} Queue;

// Modify the code below to implement the key operations for queues
void queue_enqueue(Queue *queue, int data)
{
    Node *newNode = malloc(sizeof(Node));
    newNode->data = data;
    if (queue->back != NULL)
    {
        queue->back->next = newNode;
    }
    else
    {
        queue->front = newNode;
    }
    queue->back = newNode;
}
int queue_dequeue(Queue *queue)
{
    if (queue->front != NULL)
    {
        Node *front = queue->front;
        int data = front->data;
        if (front == queue->back)
        {
            queue->back = NULL;
        }
        queue->front = front->next;
        free(front);
        return data;
    }
    return 0;
}
int queue_front(const Queue *queue)
{
    if (queue->front != NULL)
    {
        return queue->front->data;
    }
    return 0;
}
bool queue_is_empty(const Queue *queue)
{
    return queue->front == NULL;
}