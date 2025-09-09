#include <stdio.h>
#include <stdlib.h>

int arr[100001];
int size = 0;

void swap(int* p1, int* p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void insert(int value) {
    arr[++size] = value;
    int key = size;
    while (key > 1) {
        if (abs(arr[key]) < abs(arr[key/2]) || (abs(arr[key]) == abs(arr[key/2]) && arr[key] < arr[key/2]   )) { 
            swap(&arr[key], &arr[key/2]);
            key = key/2;
        }
        else { break ; }
    }
}

int pop() {
    int item = arr[1]; 
    arr[1] = arr[size--]; 
    int key = 1; 
    int idx;
    while (key*2 <= size) { 
        if (key*2+1 <= size && ( abs(arr[key*2+1]) < abs(arr[key*2]) || (abs(arr[key*2+1]) == abs(arr[key*2]) && arr[key*2+1] < arr[key*2]))) { 
            idx = key*2+1;
        }
        else {
            idx = key*2;
        }

        if (abs(arr[idx]) < abs(arr[key]) || (abs(arr[idx]) == abs(arr[key]) && arr[idx] < arr[key]   )) { 
            swap(&arr[idx], &arr[key]);  
            key = idx;
        }
        else { break; } 

    }

    return item;
}


int main() {
    int n, k;
    scanf("%d", &n);
    for (int i = 0; i<n; i++) {
        scanf("%d", &k);
        if (!k) {
            if (!size) { printf("0\n"); }
            else { printf("%d\n", pop()); }
        }
        else {
            insert(k);
        }
    }

    return 0;
}