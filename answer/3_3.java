import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int q = scanner.nextInt();
        scanner.nextLine(); // 정수 입력 후 남은 개행 문자 처리

        String commands = scanner.nextLine();

        int a = 1, b = 1
        for (int i = 0; i < commands.length(); i++) {
            char command = commands.charAt(i);
            switch (command) {
                case 'R':
                    b = (b + 1 <= q) ? b + 1 : q;
                    break;
                case 'L':
                    b = (b - 1 >= 1) ? b - 1 : 1;
                    break;
                case 'U':
                    a = (a - 1 >= 1) ? a - 1 : 1;
                    break;
                case 'D':
                    a = (a + 1 <= q) ? a + 1 : q;
                    break;
            }
        }

        System.out.println(a + " " + b);

        scanner.close();
    }
}
