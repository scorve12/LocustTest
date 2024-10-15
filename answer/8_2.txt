import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Main{
   public static void main(String args[]) {
      Scanner s = new Scanner(System.in);
      
      int x = s.nextInt();
      int y = s.nextInt();
      
      int visited[] = new int[x];
      
      ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();
      
      for(int i = 0; i < x; i++) {
         visited[i] = 0;
         arr.add(new ArrayList<Integer>());
      }
      
      for(int i = 0; i < y; i++) {
         int a = s.nextInt()-1;
         int b = s.nextInt()-1;
         arr.get(a).add(b);
      }
      
      LinkedList k = new LinkedList<Integer>();
      k.add(0);
      
      visited[0] = 1;
      int count = 0;
      
      while(!k.isEmpty()) {
         int num = (int) k.pop();
         count++;
        
         for(int i = 0; i < arr.get(num).size();) {
            int tmp = arr.get(num).remove(i);
           
            if(visited[tmp] == 0) {
               k.add(tmp);
               visited[tmp] = 1;
            }
         }
      }
      
      System.out.println(count);
   }
}