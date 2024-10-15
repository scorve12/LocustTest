import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		
		int n=sc.nextInt();
		int m=sc.nextInt();
		
		ArrayList<ArrayList<Integer>> graph=new ArrayList();
		
		for(int i=0;i<=n;i++)
			graph.add(new ArrayList<Integer>());
		for(int i=0;i<m;i++) {
			int a=sc.nextInt();
			int b=sc.nextInt();
			
			graph.get(a).add(b);
			graph.get(b).add(a);
		}
		for(int i=1;i<graph.size();i++) {
			ArrayList<Integer>node=graph.get(i);
			for(int j=0;j<node.size();j++) {
				System.out.print(node.get(j)+" ");
			}
			System.out.println();
		}
	}

}