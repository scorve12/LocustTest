import java.util.*;

class Change{
   static int SuccessTime; 
   static int howmany[]=new int[10000];
   static int t=0;
   static void ColorChange(int[][] a,int x,int y){ 
      if(x>=0 && y>=0 &&y<a.length && x<a.length && a[x][y]==0) a[x][y]=1;
      else if(x>=0 && y>=0 &&y<a.length && x<a.length && a[x][y]==1) a[x][y]=0;      
   }
   
   static void ChangeSide(int[][] a,int x,int y) { 
      ColorChange(a,x,y);
      ColorChange(a,x-1,y);
      ColorChange(a,x+1,y);
      ColorChange(a,x,y-1);
      ColorChange(a,x,y+1);
   }
   
   static void IsAllOne(int[][] a,int Times) {
      if(a[0][0]==1 && a[0][1]==1 && a[0][2]==1 && a[1][0]==1 && a[1][1]==1 && a[1][2]==1 &&a[2][0]==1 && a[2][1]==1 && a[2][2]==1) {
         howmany[t++]=Times; 
      }
      if(a[0][0]==0 && a[0][1]==0 && a[0][2]==0 && a[1][0]==0 && a[1][1]==0 && a[1][2]==0 &&a[2][0]==0 && a[2][1]==0 && a[2][2]==0) {
         howmany[t++]=Times; 
      }
      SuccessTime=howmany[0];
   }
   static void PrintSuc() {
      if(SuccessTime>0) System.out.println(SuccessTime);
      else System.out.println(-1);
   }
   
   
}

public class Color {

   public static void main(String[] args) {
      Scanner scan=new Scanner(System.in);
      int tries; 
      int[][] grid=new int[3][3]; 
      for(int j=0; j<3; j++)
      for(int i=0; i<3; i++)
         grid[j][i]=scan.nextInt();
      
      tries=scan.nextInt();
      
      int RC[]= new int[2*tries]; 
      for(int i=0; i<RC.length; i++)
         RC[i]=scan.nextInt();
      
      for(int i=0; i<tries; i++) {
      Change.ChangeSide(grid,RC[2*i]-1,RC[2*i+1]-1); 
      Change.IsAllOne(grid, i+1); 
      }
      Change.PrintSuc(); 

      
      scan.close();

   }

}