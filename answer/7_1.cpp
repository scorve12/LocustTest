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

    for (int i = 0; i < h; i++)
        for (int j = 0; j < w; j++)
        {
            cnt = 0;
            if (map[i][j])   res = max(res, dfs(i, j, h, w));;
           
        }
    cout << res;
}