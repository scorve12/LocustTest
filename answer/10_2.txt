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
  for(int i=1;i<=n;i++){
    for(int j:graph[i]){
      cout<<j<<" ";
    }
    cout<<"\n";
  }
}
