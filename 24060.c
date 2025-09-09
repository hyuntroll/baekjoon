#include <stdio.h>

int sorted[500001];
int arr[500001];
int k1;
int temp = 0;

void merge(int left, int middle, int right) {
    int i, j, t;
    i = left; j = middle +1; t = left;

    while (i <= middle && j <= right) {
        if (arr[j] > arr[i]) {
            sorted[t++] = arr[i++];
        }
        else {
            sorted[t++] = arr[j++];
        }
    }

    // 남는다면
    while (i <= middle) {
        sorted[t++] = arr[i++];
    }
    while (j <= right) {
        sorted[t++] = arr[j++];
    }
    for (t=left; t<=right; t++) {
        arr[t] = sorted[t];
        // printf("%d ", arr[t]);
        if (++temp == k1) {
            printf("%d\n", arr[t]);
        }
    }
}

void mergeSort(int left, int right) {
    if (left < right) {
        int middle =  (left+right)/2;
        mergeSort(left, middle);
        mergeSort(middle+1, right);
        merge(left, middle, right);
    }
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k1);
    for (int i =0; i<n; i++) {
        scanf("%d", &k);
        arr[i] = k;
    }
    mergeSort(0, n-1);
    // for (int i =0; i<n; i++) {
    //     printf("%d ", arr[i]);
    // }
    if (temp < k1) {
        printf("-1\n");
    }
    

    return 0;
}