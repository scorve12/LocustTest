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