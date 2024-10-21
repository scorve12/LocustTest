import java.util.Scanner;

public class Main {
    private static final int MOD = 1000000007;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[] chk2 = {0, 1, 2};
        int[] chk3 = {0, 1, 2, 4, 5};
        int[] dp2 = new int[4];
        int[] dp3 = new int[9];

        for (int index : chk2) {
            dp2[index] = 1;
        }
        for (int index : chk3) {
            dp3[index] = 1;
        }

        for (int i = 0; i < n - 1; i++) {
            int[] a2 = new int[4];
            int[] a3 = new int[9];

            System.arraycopy(dp2, 0, a2, 0, dp2.length);
            System.arraycopy(dp3, 0, a3, 0, dp3.length);

            java.util.Arrays.fill(dp2, 0);
            java.util.Arrays.fill(dp3, 0);

            for (int j : chk2) {
                for (int k : chk2) {
                    if ((j & ~k) == j) {
                        dp2[j] = (dp2[j] + a2[k]) % MOD;
                    }
                }
            }

            for (int j : chk3) {
                for (int k : chk3) {
                    if ((j & ~k) == j) {
                        dp3[j] = (dp3[j] + a3[k]) % MOD;
                    }
                }
            }
        }

        long sum2 = 0, sum3 = 0;
        for (int value : dp2) {
            sum2 = (sum2 + value) % MOD;
        }
        for (int value : dp3) {
            sum3 = (sum3 + value) % MOD;
        }

        long result = sum2 * sum2 % MOD * sum3 % MOD;
        System.out.println(result);

        scanner.close();
    }
}