import java.util.*;

public class Main {
    public static void dom1(int a, LinkedList<Integer>[] abc, int[] visit) {
        for(int i=1; i<2001; i++) {
            if(visit[a] == 0)
                dom2(a, abc, visit);
        }
    }

    public static void dom2(int a, LinkedList<Integer>[] abc, int[] visit) {
        visit[a] = 1;
        abc[a].forEach(o -> {if(visit[o]==0) dom2(o, abc, visit);});
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int p = sc.nextInt();
        int q = sc.nextInt();

        LinkedList<Integer>[] abc = new LinkedList[2001];
        int[] visit = new int[2001];
        for(int i=1; i<p+1; i++) 
            abc[i] = new LinkedList();

        for(int i=0; i<q; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            abc[a].add(b);
        }

        int c = 0;
        int s = 1;

        dom1(1, abc, visit);

        for(int i=1; i<2001; i++) {
            if(visit[i]==1)
                c++;
        }

        System.out.print(c);
        sc.close();
    }
}