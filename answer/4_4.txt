import java.util.*;

public class Main {  
  public static void main(String args[]) { 
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();
    int sum = 0;
    int count = n;
    int array[] = new int[n];
    
    for(int i = 0; i < n; i++){
    	
      array[i] = sc.nextInt();
      sum = sum + array[i];
    }
    
    Arrays.sort(array);

    for(int j = 0; j < n; j++){
      if(sum / count < k){
        sum = sum - array[j];
        count--;
      }
    }
    System.out.println(count);
    
    sc.close();
    
  } 
}
