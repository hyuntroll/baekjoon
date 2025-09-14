#include <stdio.h>

// m 을 받았을 때 잘라야 하기 때문에 특정값 초과로 잘랐을 때 되는 최소 m을 구해야함

int main() {
    long long arr[1000000];
    int n, m;
    long long min=0, max = 0, mid, sum;
    scanf("%lld %lld", &n, &m);
    for (int i=0; i<n; i++) {
        scanf("%lld", &arr[i]);
        if (max < arr[i]) max = arr[i];
    }

    while ( min <= max )
    {
        mid = min + (max-min)/2;
        sum = 0;
        for (int i=0; i<n; i++) {
            if (mid < arr[i]) sum += arr[i] - mid;
        }
        if (sum < m) {max = mid-1;}
        else {min = mid+1;}
    }

    printf("%lld", max);



    return 0; 
}