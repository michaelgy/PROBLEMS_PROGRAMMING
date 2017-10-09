#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    long a,b,c,ra,rb,cop;
    for(cin >> a >> b; a!=0 || b!=0; cin >> a >> b){
        cop = 0;
        c = 0;
        while(a!=0 || b!=0){
            ra = a%10;
            rb = b%10;
            a /= 10;
            b /= 10;
            c = (c+ra+rb)/10;
            cop += c > 0 ? 1: 0;
        }
        if(cop){
            cout << cop << " carry ";
            if(cop==1){
                cout << "operation.";
            }
            else{
                cout << "operations.";
            }
        }
        else{
            cout << "No carry operation.";
        }
        cout << endl;
    }
    return 0;
}