#include <stdio.h>

// m 을 받았을 때 잘라야 하기 때문에 특정값 초과로 잘랐을 때 되는 최소 m을 구해야함

int main() {
    int arr[1000001];
    int n, m, sum, min, max, mid, temp;
    min = 2000000001;
    max = 0;
    scanf("%d %d", &n, &m);
    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
        if (min > arr[i]) min = arr[i];
        if (max <arr[i]) max = arr[i];
    }
    if (min != max) {
        do {
            mid = (max+min)/2;
            sum = 0;
            for (int i=0; i<n; i++) {
                if (mid < arr[i]) sum += arr[i] - mid;
            }
            if (m < sum) {min = mid;}
            else if ( m > sum) {max = mid;}
            // printf("%d %d %d \n", sum, min, max);
        } while (sum != m && min < max);
    }
    printf("%d", mid);



    return 0; 
}