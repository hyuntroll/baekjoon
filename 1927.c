#include <stdio.h>

int pi(int key) {
    return key/2;
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
    int root = arr[key];
    int idx;

    arr[key] = arr[end--]; 

    while (key * 2 <= end) { // 자식 노드가 있다면. ( 왼쪽노드가 오른쪽 노드 -1이기 때문에 일부러 그런거임 )
        if (key*2+1 <= end && arr[key*2+1] < arr[key*2]) { // 오른쪽 노드가 있는 상태에서 오른쪽 노드보다 왼쪽노드가 크면
            idx = key*2+1;
        } else { // 반대라면 왼쪽 노드를 넣음
            idx = key*2;
        }

        if (arr[idx] < arr[key]) { // 그래서 그 값이 부모값보다 작다면 스왑
            swap(&arr[idx], &arr[key]);
            key = idx;
        } else break;
    }

    return root;
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
        }

    }

    return 0;
}


// #include <stdio.h>
// #include <stdlib.h>

// // void shit(long long* ptr, int size, int min) {
// //     for (int i=0; i < size; i++) {
// //         printf("%lld ", ptr[i]);
// //     }
// //     printf("min: %d\n", min);
// // }

// int main() {

//     long long* ptr;
//     int n;
//     int size = 0;
//     int x, key;
//     long long min=0;
//     scanf("%d", &n);
//     ptr = (long long* )calloc(n, sizeof(long long));
//     for (int i=0; i<n; i++) {
//         scanf("%d", &x);
//         if (x > 0) {
//             ptr[size++] = x;
//             if (!min) { min=x; key=size-1; }
//             else {
//                 if (x < min) {
//                     min = x;
//                     key=size-1;
//                 }
//             }
//         }
//         else {
//             if (!size) { printf("0\n"); }
//             else {
//                 printf("%lld\n", min);
//                 min = 0;
//                 for (int k=key; k < size-1; k++) { // 0 1 2 3 4 size=5 key=1 1~3
//                     ptr[k] = ptr[k+1];
//                     if (!min || (min > ptr[k+1] && ptr[k] !=0)) {
//                         min = ptr[k+1]; key=k;
//                     }
//                 }
//                 for (int k=0; k<key; k++) {
//                     if (!min || min > ptr[k]) {
//                         min = ptr[k]; key=k;
//                     }
//                 }
//                 ptr[size-1] = 0; size--;

//                 // printf("%lld\n", min);
//             }
//         }
        
//         // shit(ptr, n, min);
//     }

//     return 0;
// }