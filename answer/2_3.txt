import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  // Scanner 객체 생성
        
        int i = scanner.nextInt();  // 사용자로부터 정수 입력 받기
        System.out.println(i);  // 입력 받은 정수 출력
        
        scanner.close();  // Scanner 객체 닫기
    }
}