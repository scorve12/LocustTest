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

for(int i= N-1; i>=0; i--){
if(M>=arr[i]){
                count+= M/arr[i];
                M= M%arr[i];
            }

        }

        System.out.println(count);


    }

}