#include <stdio.h>

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
        if (arr[key] > arr[key/2]) { // 부모 노드가 더 작으면
            swap(&arr[key], &arr[key/2]);
        }
        else { break ; }// 그게 아니라 자식 노드가 더 작으면 
    }
}

int pop() {
    int item = arr[1]; // 가장 상단의 값을 뽑음
    arr[1] = arr[size--]; // 상단 값을 가장 마지막 값으로 변환, 사이즈를 1 감소
    int key = 1; // 가장 상단 노드를 키로 설정
    int idx;
    while (key*2 >= size) { // 자식 노드가 있다면
        if (key*2+1 >= size && arr[key*2+1] > arr[key*2]) { // 오른쪽 자식이 있고, 그때 오른쪽 자식이 왼쪽자식보다 크다면
            idx = key*2+1;
        }
        else {
            idx = key*2;
        }

        if (arr[idx] > arr[key]) { // 자식 노드가 부모노드보다 크다면
            swap(&arr[idx], &arr[key]);  // 변환함
            key = idx;
        }
        else { break; } // 그게 아니라면 끝냄

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