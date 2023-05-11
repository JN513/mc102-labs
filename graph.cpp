#include <bits/stdc++.h>

#define ll long long int
#define nl endl

using namespace std;

#define NMAX 100005

vector<int> grafo[NMAX];

int main(void)
{
    int n;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int a, b;

        cin >> a >> b;

        grafo[a].push_back(b);
        grafo[b].push_back(a);
    }

    return 0;
}