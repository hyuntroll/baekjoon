// 문제 접근을 근처에 있는걸 찾아야 하니까 결국 뭉탱이를 하나 찾는게 좋은 거 같음
// 한줄씩 검사하면서 1이 있고 있으면 3으로 변경, 상하좌우로 3이 없다면 +1, 있으면 그냥 1을 3으로 변경하고 지나감
#include <stdio.h>
#include <stdlib.h>

// 한줄씩 검사하면서 한줄이 연결되어 있는지 검사
// 검사하면서 위/아래로 이뤄지는지도

// 검사하는걸 한줄씩 하고 그 한줄에서 얼만큼 연결되어 있는지 검사
// 만약 검사하는 이어진 줄이 이미 다른 것과 이어져 있다 -> 카운트에서 제외

// 이렇게 하니까 한줄에서 띄어진 경우가 있고 아래에서 연결되어 있으면 카운트가 각각되는 문제가 있기 때문에
// 하나씩 다른 점수를 넣어서 서로 비교하고 비교했을 때 서로 다르다면 같게 만들어야 함 ( 위에거랑 아래거랑 비교했을 때 만약 둘이 다르다면 카운트가 되었을 거라 판단되기 때문에 -1)
// 이어졌다는 것을 알리는 temp를 통해 같다라는 것을 표시해야할듯
// 이렇게 해도 오류가 날 수 있기 때문에 오류날거 생각하고 만들어야 할듯

// 아니면 받은거 리스트로 관리해서 이거 가지고 이 주변에 있는지 없는지 확인해도 좋을 듯 1, 0 1, 1 이렇게 받으면 상하좌우 검사하면서 근처에 있는거를 모두 가져옴 
// 가는 경우를 탐색하면서 

// 탐색하면서 위쪽이랑 비교하는데 만약 위쪽이랑 값이 다르다면 -1 | 그게 아니라 그냥 값이 다르면
 

int main() {
    int** multiArr;
    int N, M, K;
    int n, m, flag;
    int count = 0, c=1, temp=0;
    int i, k, repeat;

    scanf("%d", &repeat);
    for (int ka=0; ka < repeat; ++ka) {
        count = 0;

        scanf("%d %d %d", &M, &N, &K);
        multiArr = (int**) calloc(M, sizeof(int *));
        for (i=0; i < M; i++) {
            multiArr[i] = (int*) calloc(N, sizeof(int));
        }
        for (i=0; i < K; i++) {
            scanf("%d %d", &n, &m);
            multiArr[n][m] = 1;
        }

        for (i=0; i < M; i++) {
            flag = 0; temp = 0;
            for (k=0; k < N; k++) {
                if (multiArr[i][k] == 1) { multiArr[i][k] = ++c; flag=1;} // 현재 탐색중인 원소가 1이라면 플래그 지정 (스코어를 더하기 위함)

                if (!flag && multiArr[i][k] > 1 && !temp) { temp = multiArr[i][k]; }
                
                if (multiArr[i][k] >= 1) {
                    // 오른쪽 검색
                    if ( k < N-1 ) {
                        if (multiArr[i][k+1] == 1) {
                            multiArr[i][k+1] = multiArr[i][k];
                        }
                        else if (multiArr[i][k+1] > 1) {
                            flag = 0;
                            if (!temp) {      
                                temp = multiArr[i][k+1];
                                multiArr[i][k+1] = multiArr[i][k];
                            }
                            else if (multiArr[i][k+1] == temp) {
                                multiArr[i][k+1] = multiArr[i][k+1];
                            }
                            else if (multiArr[i][k+1] != temp) {
                                temp = multiArr[i][k+1]; 
                                multiArr[i][k+1] = multiArr[i][k];
                                count--;
                            }
                        }
                    }

                    //아래 검색
                    if (i < M-1 ) {
                        if (multiArr[i+1][k]) {
                            multiArr[i+1][k] = multiArr[i][k];
                        }
                    }
                }
                else {
                    // 끊긴 것으로 판단.
                    if (flag) {
                        count++;
                        flag = 0;
                        temp = 0;
                    }
                }

            }
            if (flag) {
                count++;
            }
        }



        // print arr
        for (i=0; i < M; i++) { 
            for (k=0; k < N; k++) {
                printf("%d ", multiArr[i][k]);
            }
            printf("\n");
        }
        printf("%d\n", count);

        for (int i =0; i<M; i++) {
            free(multiArr[i]);
        }
        free(multiArr);
    }
    return 0;
}

/*


        for (i=0; i < M; i++) { 
            flag = 0; temp = 0;
            for (k =0; k < N; k++) {

                if (multiArr[i][k] > 1) { temp=multiArr[i][k]; }
                else if (multiArr[i][k] == 1) { flag = 1; multiArr[i][k] = ++c; }

                if ( multiArr[i][k] >= 1) {
                    // 오른쪽 검색
                    if ( k < N-1 ) {
                        if (multiArr[i][k+1] > 1) {
                            multiArr[i][k+1] = multiArr[i][k];
                        }
                        else if (multiArr[i][k+1] != 0 ) {
                            if (!temp) {
                                temp = multiArr[i][k+1];
                                multiArr[i][k+1] = multiArr[i][k];
                            }
                            else if (temp != multiArr[i][k+1] && multiArr[i][k+1] != 1) {
                                temp = multiArr[i][k+1];
                                multiArr[i][k+1] = multiArr[i][k];
                                count--;
                            }
                        }
                    }
                    //아래 검색
                    if (i < M-1 ) {
                        if (multiArr[i+1][k]) { multiArr[i+1][k] = multiArr[i][k];}
                    }
                }
                else {
                    if (flag) {
                        ++count;
                        flag = 0;
                    }
                }
                
            }
            if (flag) {
                ++count;
            }
        }


        
        */

/* 
for (i=0; i < M; i++) { 
    flag = 0;
    for (k =0; k < N; k++) {
        if (multiArr[i][k] == 1) {
            multiArr[i][k] = 2;
            flag = 1;
        }

        if (multiArr[i][k] != 0) {
            c++;
            //오른쪽 검색
            if ( k < N-1 ) {
                if ( multiArr[i][k+1] == 1) {
                    multiArr[i][k+1] = 2;
                } else if ( multiArr[i][k+1] == 2 && flag ) {flag = 0;}
            }
            //아래 검색
            if (i < M-1 ) {
                if (multiArr[i+1][k] == 1) {
                    multiArr[i+1][k] = 2;
                }
            }
            
        }
        else {
            c = 0;
            if (flag) { ++count; flag=0;}
        }

        
        // if (multiArr[i][k] == 1) {
        //     printf("a%d %d, %d \n", i, k, c);
        //     multiArr[i][k]++;
        //     if (!flag) {
        //         // printf("k%d %d \n", i, k);
        //         ++count;
        //     }
        // }

    }   
    if (c) {
        if (flag) { ++count;}
    }
}
*/