#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

int main() {
    int arr[10000] = {0};
    int N, K, i;
    
    scanf("%d %d", &N, &K);
    for (i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    qsort(arr, N, sizeof(int), compare);

    int sum = 0;
    for (i = 1; i <= N; i++) {
        if ((arr[N - i] + sum) / i >= K) {
            sum += arr[N - i];
        } else {
            break;
        }
    printf("%d\n", i - 1);

    return 0;
}