
#include <stdio.h>

int pi(int key) {
    return key/2;
}
int leftChild(int key) {
    return key *2;
}
int rightChild(int key) {
    return key*2 +1;
}
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void insert(int *arr, int value, int key) {
    arr[key] = value;
    while (arr[key] < arr[pi(key)] && key != 1) {
        swap(&arr[key], &arr[pi(key)]);
        key = pi(key);
    }

}


int main() {
    int arr[100001] = {0};

    insert(arr, 1, 10);
    printf("%d %d \n", arr[1], arr[2]);
    insert(arr, 2, 30);
    printf("%d %d \n", arr[1], arr[2]);
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