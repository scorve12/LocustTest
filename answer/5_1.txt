#include <stdio.h>

#define MOD 1000000007

int main() {
    int n;
    scanf("%d", &n);

    int chk2[] = {0, 1, 2};
    int chk3[] = {0, 1, 2, 4, 5};
    int dp2[4] = {0}, dp3[9] = {0};
    int size2 = sizeof(chk2) / sizeof(chk2[0]);
    int size3 = sizeof(chk3) / sizeof(chk3[0]);

    for (int i = 0; i < size2; i++) {
        dp2[chk2[i]] = 1;
    }
    for (int i = 0; i < size3; i++) {
        dp3[chk3[i]] = 1;
    }

    for (int i = 0; i < n - 1; i++) {
        int a2[4] = {0}, a3[9] = {0};

        for (int j = 0; j < 4; j++) {
            a2[j] = dp2[j];
        }
        for (int j = 0; j < 9; j++) {
            a3[j] = dp3[j];
        }

        for (int j = 0; j < 4; j++) {
            dp2[j] = 0;
        }
        for (int j = 0; j < 9; j++) {
            dp3[j] = 0;
        }

        for (int j = 0; j < size2; j++) {
            for (int k = 0; k < size2; k++) {
                if ((chk2[j] & ~chk2[k]) == chk2[j]) {
                    dp2[chk2[j]] += a2[chk2[k]];
                    dp2[chk2[j]] %= MOD;
                }
            }
        }

        for (int j = 0; j < size3; j++) {
            for (int k = 0; k < size3; k++) {
                if ((chk3[j] & ~chk3[k]) == chk3[j]) {
                    dp3[chk3[j]] += a3[chk3[k]];
                    dp3[chk3[j]] %= MOD;
                }
            }
        }
    }

    int sum2 = 0, sum3 = 0;
    for (int i = 0; i < 4; i++) {
        sum2 += dp2[i];
        sum2 %= MOD;
    }
    for (int i = 0; i < 9; i++) {
        sum3 += dp3[i];
        sum3 %= MOD;
    }

    printf("%lld\n", ((long long)sum2 * sum2 % MOD) * sum3 % MOD);

    return 0;
}
