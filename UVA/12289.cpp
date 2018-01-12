#include <iostream>
#include <string>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    int n,one;
    string s;
    for(cin>>n;n>0;n--){
        cin>>s;
        if(s.length() == 5){
            cout << 3;
        }
        else{
            one = 0;
            if(s[0] == 'o'){
                one++;
            }
            if(s[1] == 'n'){
                one++;
            }
            if(s[2] == 'e'){
                one++;
            }
            if(one>1){
                cout << 1;
            }
            else{
                cout << 2;
            }
        }
        cout << endl;
    }
    return 0;
}