#include<stdio.h>
#include<stdlib.h>


int main() {

    int arr[1001] = {0};
    arr[1] = 1; arr[2] = 3; arr[3] = 5; arr[4] = 8;
    int n = 2;
    for (int i= 5; i <n+1; i++) {
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3] + arr[i-4];
    }

    printf("%d", arr[n]);


    return 0;
}




/*
2x1, 2x1만 사용했을 때

2x1: 1
2x2: 2
2x3: 3
2x4: 5

2x2를 함께 사용했을 때

2x1: 1 + 0
2x2: 2 + 1
2x3: 3 + 2
2x4: 5 + 5
2x5:  + 


2xn이 있을 때 

2x2를 넣은 후 나눠진 만큼을 dp를 써서 ?

---

2x2인 경우 

2x2를 하나 넣었을 때 더 넣을 수 없으니 +0

2x3은 한쪽에 넣고 다른 한쪽에 넣었을 때 각각 하나씩 남으니 +2

2x4는 

*/