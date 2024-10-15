#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void)
{
	int N, K;
	int count = 0;
	scanf("%d %d", &N, &K);

	int a[N];
	for (int i = 0; i < N; i++)
		scanf("%d", &a[i]);

	for (int i = N - 1; i >= 0; i--) {
		count += K / a[i];
		K = K % a[i];
	}
	printf("%d", count);
	return 0;
}