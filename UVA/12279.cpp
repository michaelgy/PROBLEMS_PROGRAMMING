#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    int c,n,i,t,v;
    for(c=1,cin>>n; n!=0;c++,cin>>n){
        t = 0;
        for(i=0;i<n;i++){
            cin>>v;
            if(v){
                t++;
            }
            else{
                t--;
            }
        }
        cout << "Case " << c << ": " << t << endl;
    }
    return 0;
}