import java.util.*;
import java.io.*;

public class Main {
    static Scanner s = new Scanner(System.in);
    
    static int h, w;
    static int[][] arr;
    static boolean[][] island;
    
    public static void max() {
        int max=0, result;
        
        for (int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                result = search(i,j);
                
                if (result > max) {
                    max = result;
                }
            }
        }
        
        System.out.print(max);
    }
    
    public static int search(int i, int j) {
        if ((i < 0 || i > h-1) || (j < 0 || j > w-1)) 
            return 0;
            
        if (island[i][j] == false) {
            island[i][j] = true;
            
            if (arr[i][j] == 1) {
                return search(i-1, j-1) + search(i-1, j) + search(i-1, j+1) + search(i, j-1) + arr[i][j] + search(i, j+1)
                + search(i+1, j-1) + search(i+1, j) + search(i+1, j+1);
            }
            
            return 0;
        }
        
        return 0;
    }
    
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        h = s.nextInt();
        w = s.nextInt();
        
        if (!((1 <= h && h <= 50) && (1 <= w && w <= 50))) {
            return;
        }
        
        arr = new int[h][w];
        island = new boolean[h][w];
        int temp;
        
        for (int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                temp = s.nextInt();
                arr[i][j] = temp;
            }
        }
        
        max();
    }
}