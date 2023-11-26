#include<bits/stdc++.h>
#define ll long long
#define endl '\n'
#define pb push_back
#define pob pop_back
#define mp make_pair
#define ff first
#define ss second
#define fastio() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(__null)
using namespace std;
const int mod = 1000000007;

// 01101111 01101101 
// 01100111 01100001 01101110 01100101 01110011 01101000 01100001 01111001 01100001
// 01101110 01100001 01101101 01100001 01101000


int main() {
    fastio();

    ll t;
    cin >> t;

    for (int c = 1; c <= t; c++) {

        cout << "Case #" << c << ": ";

        ll m,r,n;
        cin >> m >> r >> n;
        vector<ll> V(n);
        for(int i=0;i<n;i++) {
            cin >> V[i];
        }
        int p=0;
        if(V[0]-r>0) {
            p++;
        }
        for(int i=0;i<n-1;i++){
            if(V[i]+r<V[i+1]-r) {
                p++;
                break;
            }
        }
        if(V[n-1]+r < m) {
            p++;
        }
        if(p>0) {
            cout << "IMPOSSIBLE" << endl;
        }
        else{
            int c=0;
            ll k=0;
            auto it1 = lower_bound(V.begin(),V.end(),k+r);
            if((*it1)!=k+r) {
                --it1;
            }

            c++;
            k=(*it1);

            while(k+r<m) {
                auto it = lower_bound(V.begin(),V.end(),k+2*r);
                if((*it)-k == 2*r){
                    k = (*it);
                }
                else{
                    --it;
                    k = (*it);
                }
                c++;
            }
            cout << c << endl;
        }
    }


    return 0;
}