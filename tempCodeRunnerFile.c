#include <stdio.h>

int pi(int key) {
    return key/2;
}
int lc(int key) {
    return key *2;
}
int rc(int key) {
    return key*2 +1;
}
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void insert(int *arr, int key, int value) {
    arr[key] = value;
    while (arr[key] < arr[pi(key)] && key != 1) {
        swap(&arr[key], &arr[pi(key)]);
        key = pi(key);
    }
}
int pop(int *arr, int key, int end) {
    int root = arr[1]; // 루트꺼 뺌
    int head = 1;
    arr[1] = arr[end]; arr[end] = 0; // 루트에 맨 마지막꺼 넣음
    if (end-1 == 1) { return root;}
    while (( arr[head] > arr[lc(head)] || arr[head] > arr[rc(head)] )&& (head > pi(end)) && !head ) { // 헤드가 0인지 
        if (arr[lc(head)] > arr[rc(head)]) {
            swap(&arr[head], &arr[rc(head)]);
            head = rc(head);
        }
        else {
            swap(&arr[head], &arr[lc(head)]);
            head = lc(head);
        }
    }

    return root;
}

void printa(int* arr, int size) {
    printf("arr: ");
    for(int i =1; i <= size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[100001] = {0};
    int n, k;
    int size = 0;
    
    scanf("%d", &n);
    for (int i=0; i < n; i++) {
        scanf("%d", &k); fflush(stdin);
        if (k) {
            insert(arr, ++size, k);
        } 
        else {
            if (!size) { printf("0\n"); continue; }
            printf("%d\n", pop(arr, 1, size--));
            // printa(arr, size);
        }

    }

    return 0;
}