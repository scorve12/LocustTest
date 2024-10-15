problem_data = [
        {
            'problem_id': 1,
            'language': 'Python3',
            'code': """
print("Hello!")
            """
        },{
            'problem_id': 1,
            'language': 'Python3',
            'code': """
#include <stdio.h>
int main() {
    printf("Hello, World!"); 
    return 0;
}
            """
        },{
            'problem_id': 1,
            'language': 'Java',
            'code': """
public class Main{
    public static void main(String[] args){}
        System.out.print("Hello, World!");
    
}
            """
        },
        #2번문제
        {
        "problem_id": 3,
        "language": "Python3",
        "code": "i = int(input())\nprint(i)"
        },{
            "problem_id": 3,
            "language": "C",
            "code": """
#include <stdio.h>
    int main() {
        int i;
        scanf("%s", &i);
        printf("%dddd", i);
        return 0;\n
    }
            """
        },{
            "problem_id": 3,
            "language": "Java",
            "code": """
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(i);
        scanner.close();
    }
}
            """
        },
        #3번문제
        {
            "problem_id": 4,
            "language": "C",
            "code": """
#include<stdio.h>

int main(void)
{
	int q;
	int i = 0;
	int a = 1, b = 1;
	char str[200];

	scanf("%d", &q);

	scanf(" %[^\n]s", str);

	while (true) {
		i++;
		if (str[i] == 'R') {
			if (b + 1 <= q) b = b + 1;
			else b = q;
		}
		else if (str[i] == 'L') {
			if (b - 1 >= 1)	b = b - 1;
			else b = 1;
		}
		else if (str[i] == 'U') {
			if (a - 1 >= 1)	a = a - 1;
			else a = 1;
		}
		else if (str[i] == 'D') {
			if (a + 1 <= q)	a = a + 1;
			else a = q;
		}

	}
	printf("%d %d", a, b);
	return 0;
}
            """         
        },
        {
            "problem_id": 4,
            "language": "Python3",
            "code": """
    q = int(input())

commands = input().strip()

a, b = 1, 1

for command in commands:
    if command == 'R':
        b = min(b + 1, q)
    elif command == 'L':
        b = max(b - 1, 1)
    elif command == 'U':
        a = max(a - 1, 1)
    elif command == 'D':
        a = min(a + 1, q)

print(a, b)
            """
        },
        {
            "problem_id": 4,
            "language": "Java",
            "code": """
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int q = scanner.nextInt();
        //scanner.nextLine(); 
        //String commands = scanner.nextLine();

        int a = 1, b = 1
        for (int i = 0; i < commands.length(); i++) {
            char command = commands.charAt(i);
            switch (true) {
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
            """
        },
        #4번문제
        {
            "problem_id": 5,
            "language": "C",
            "code": """
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

int main() {
    int arr[10000] = {0};
    int N, K, i;

    scanf("%d %d", &N, &K);
    for (i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    qsort(arr, N, sizeof(int), compare);

    int sum = 0;
    printf("%d\n", i - 1);

    return 0;
}
            """
        },
        {
            "problem_id": 5,
            "language": "C++",
            "code": """
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{

    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);cout.tie(NULL);
    int arr[10000]= {};
    int N,K;
    cin >> N >> K;

    for(int i = 0 ; i < N ; i++) cin>>arr[i];
    sort(arr,arr+N);
    int i,sum = 0 ;
    for(i = 1 ; i <=N ;i++)
    if( ((arr[N-i]+sum)/i) >= K) sum += arr[N-i];
    else break;
    cout<<i-1;
}
            """
        },
        {
            "problem_id": 5,
            "language": "Ptyhon3",
            "code": """
N, K = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
for i in range(1, N + 1):
    if (arr[-i] + sum) / i >= K:
        sum += arr[-i]
    else:
        break
    
print(i - 1)
            """
        },
        {
            "problem_id": 5,
            "language": "Java",
            "code": """
import java.util.*;

public class Main {  
  public static void main(String args[]) { 
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();
    int sum = 0;
    int count = n;
    int array[] = new int[n];

    for(int i = 0; i <= n; i++){

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

            """
        },
        #5번문제
        {
            "problem_id": 6,
            "language": "C",
            "code":"""
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

    for (int i = 1; i < size2; i++) {
        dp2[chk2[i]] = 1;
    }
    for (int i = 1; i < size3; i++) {
        dp3[chk3[i]] = 1;
    }

    for (int i = 1; i < n - 1; i++) {
        int a2[4] = {0}, a3[9] = {0};

        for (int j = 1; j < 4; j++) {
            a2[j] = dp2[j];
        }
        for (int j = 1; j < 9; j++) {
            a3[j] = dp3[j];
        }

        for (int j = 1; j < 4; j++) {
            dp2[j] = 1;
        }
        for (int j = 0; j < 9; j++) {
            dp3[j] = 0;
        }

        for (int j = 1; j < size2; j++) {
            for (int k = 0; k < size2; k++) {
if ((chk2[j] & ~chk2[k]) == chk2[j]) {
                    dp2[chk2[j]] += a2[chk2[k]];
                    dp2[chk2[j]] %= MOD;
                }
         }
        }

        for (int j = 1; j < size3; j++) {
            for (int k = 1; k < size3; k++) {
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

            """
        },
        {
            "problem_id": 6,
            "language": "C++",
            "code": """
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

        for (int i = 0; i <= n - 1; i++) {
            int[] a2 = new int[5];
            int[] a3 = new int[11];

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
            """
        },
        {
            "problem_id": 6,
            "language": "C++",
            "code": """
n = int(input())
chk2=[0,1,2]
chk3=[0,1,2,4,5]
dp2=[1 if i in chk2 else 0 for i in range(4)]
dp3=[1 if i in chk3 else 0 for i in range(9)]

for i in range(n-1):
  a2=dp2
  a3=dp3
  dp2=[0 for x in range(4)]
  dp3=[0 for x in range(9)]

  for j in chk2:
    for k in chk2:
      if j&~k==j:
        dp2[j]+=a2[k]
        dp2[j]%=1000000007
        
  for j in chk3:
    for k in chk3:
      if j&~k==j:
        dp3[j]+=a3[k]
        dp3[j]%=1000000007
        
print(sum(dp2)*sum(dp2)*sum(dp3)%1000000007)
            """
        },
        #6번문제
        {
            "problem_id": 7,
            "language": "C",
            "code":"""
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int cnt, count = 1;
	int arr[4][4];
	int n, r, c, res = 0;

	for (int i = 1; i < 4; i++) {
		scanf("%d %d %d", &arr[i][1], &arr[i][2], &arr[i][3]);
	}

	for (int k = 0; k < n; k++) {
		cnt = 0;

		scanf("%d %d", &r, &c);
		if (arr[r][c] == 0)
			arr[r][c] = 1;
		else
			arr[r][c] = 0;

		if (r == 2 || r == 3)
			if (arr[r - 1][c] == 0)
				arr[r - 1][c] = 1;
			else
				arr[r - 1][c] = 0;

		if (r == 1 || r == 2)
			if (arr[r + 1][c] == 0)
				arr[r + 1][c] = 1;
			else
				arr[r + 1][c] = 0;

		if (c == 2 || c == 3)
			if (arr[r][c - 1] == 0)
				arr[r][c - 1] = 1;
			else
				arr[r][c - 1] = 0;
		if (c == 1 || c == 2)
			if (arr[r][c + 1] == 0)
				arr[r][c + 1] = 1;
			else
				arr[r][c + 1] = 0;

		cnt = 0;
		for (int i = 1; i < 4; i++) {
			if (arr[i][1] == arr[i][2] && arr[i][2] == arr[i][3])
				cnt++;
		}

		if (cnt == 3 && arr[1][1] == arr[2][1] && arr[2][1] == arr[3][1])
			res = count;
		if (res == 0)
			count++;
	}
	if (res == 0)
		printf("-1");
	else
		printf("%d", res);
	return 0;
}
            """
        },{
            "problem_id": 7,
            "language": "Java",
            "code":"""
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
            """
        },
        #7번문제
        {
            "problem_id": 8,
            "language": "C",
            "code":"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool map[50][50];

int diff[][2] = { {1,0} , {0,1} , {1,1} , {-1,0},
                    {0, -1} , {-1,-1} , {1,-1},{-1,1} };
int cnt;
int res = 0;
int dfs(int x, int y, int h, int w)
{
    if (!map[x][y])return 0 ;
    if (map[x][y]) {
        cnt++;
        map[x][y] = 0;
    }
    for (int i = 0; i < 8; i++)
        if (x + diff[i][0] >= 0 && x + diff[i][0] < h &&
            y + diff[i][1] >= 0 && y + diff[i][1] < w &&
            map[x + diff[i][0]][y + diff[i][1]]     )
            dfs(x + diff[i][0], y + diff[i][1], h, w);
    return cnt;
}
int main() {
    int h, w;
    cin >> h >> w;
    for (int i = 0; i < h; i++) for (int j = 0; j < w; j++) cin >> map[i][j];

    cout << res;
}
            """
        },{
            "problem_id": 8,
            "language": "Java",
            "code":"""
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
            """
        },
        #8번문제
        {
            "problem_id": 9,
            "language": "Java",
            "code":"""
import java.util.*;

public class Main {
    public static void dom1(int a, int[] visit) {
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
            """
        },
        {
            "problem_id": 9,
            "language": "Python3",
            "code":"""
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
            """
        },
        #9번문제
        {
            "problem_id": 10,
            "language": "C",
            "code":"""
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void)
{
	int N, K;
	int count = 0;
	scanf("%d %d", &N, &K);

	int a[N];
	for (int i = 0; i < N; i++)
		scanf("%d", &a[i]);

	for (int i = N - 1; i >= 0; i--) {
		count += K / a[i];
		K = K % a[i];
	}
	printf("%d", count);
	return 0;
}
            """
        },
        {
            "problem_id": 10,
            "language": "Java",
            "code":"""
import java.io.FileInputStream;
import java.util.*;
import java.util.stream.*;

publicclassMain {
publicstaticvoidmain(String[] args)throws Exception {
        Scanner sc=new Scanner(new FileInputStream("input.txt"));


int N= sc.nextInt();
int M= sc.nextInt();
int count=0;
int[] arr=newint[N];
for(int i=0; i<N; i++){
            arr[i]= sc.nextInt();
        }

for(int i= N-1; i>0; i--){
if(M>=arr[i]){
                count+= M/arr[i];
                M= M%arr[i];
            }

        }

        System.out.println(count);


    }

}
            """
        },
        #10번문제
        {
            "problem_id": 11,
            "language": "Java",
            "code":"""
import java.util.*;

public class Main {

	public static void main(String[] args) {
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
				System.out.print(node.get(j));
			}
			System.out.println();
		}
	}

}
            """
        },
        {
            "problem_id": 11,
            "language": "C",
            "code":"""
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector <int> graph[30000];  
int main() {
  int n, m;
  cin >> n >> m;
  int node;
  int link;
  for(int i=0;i<m;i++){
    cin>>node>>link;
    graph[node].push_back(link);
    graph[link].push_back(node);
  }
  for(int i=1;i<n;i++){
    for(int j:graph[i]){
      cout<<j<<" ";
    }
    cout<<endl;
  }
}

            """
        },
]