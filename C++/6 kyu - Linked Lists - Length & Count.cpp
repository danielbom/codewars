// https://www.codewars.com/kata/55beec7dd347078289000021/train/cpp
// My solution
int Length(Node *head) {
  int count = 0;
  while (head) {
    count++;
    head = head->next;
  }
  return count;
}

int Count(Node *head, int data) {
  int count = 0;
  while (head) {
    if (head->data == data) count++;
    head = head->next;
  }
  return count;
}
