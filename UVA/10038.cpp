#include <iostream>
#include <bitset>
#include <cstdlib>

using namespace std;
int main(){
    ios::sync_with_stdio(false);
    bitset<3000> jol;
    jol.reset();
    int n,k,i,cur,next,d;
    bool isjol;
    for(cin >> n; !cin.eof(); cin >>n){
        isjol = true;
        cin >> cur;
        k = n-1;
        for(i=1;i<n;i++){
            cin >> next;
            if(isjol){
                d = abs(cur-next);
                if(d==0 || d>n-1){
                    isjol = false;
                }
                else if(jol[d-1]==1){
                    isjol = false;
                }
                else{
                    jol[d-1] = 1;
                    k-=1;
                }
                cur = next;
            }
        }
        if(k==0 && isjol){
            cout << "Jolly";
        }
        else{
            cout << "Not jolly";
        }
        cout << endl;
        for(i=0;i<n;i++){
            jol[i] = 0;
        }
    }
    return 0;
}