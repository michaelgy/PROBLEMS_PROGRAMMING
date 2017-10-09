#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    int t,a,b,i,r;
    cin >> t;
    for(i=0;i<t;i++){
        cin >> a >> b;
        a = a%2 == 0 ? a+1:a;
        b = b%2 == 0 ? b-1:b;
        r = a;
        while(a<b){
            a = a+2;
            r = r+a;
        }
        cout << "Case " << i+1 << ": " << r << endl;
    }
    return 0;
}