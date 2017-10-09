#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    unsigned int n,s,d,w;
    for(cin >> n; n>0; n--){
        cin >> s >> d;
        if(d>s){
            cout << "impossible" << endl;
        }
        else{

            w = (d+s);
            if(w%2==0){
                w /=2;
                cout << w << " " << s-w << endl;
            }
            else{
                cout << "impossible" << endl;
            }
        }
    }
    return 0;
}