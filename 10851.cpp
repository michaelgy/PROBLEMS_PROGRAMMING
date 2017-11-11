#include <iostream>

using namespace std;

void clear(char s[81]){
    for(int i = 0;i<80;i++){
        s[i] = (char)0;
    }
}

int main(){
    ios::sync_with_stdio(false);
    int T,m,i,j;
    char s[81],c;
    for(cin>>T;T>0;T--){
        clear(s);
        cin.get();
        for(m=0;cin.get()!='\n';m++){}
        m-=2;
        s[m] = '\0';
        for(j=0;j<8;j++){
            cin.get();// first /
            for(i=0;i<m;i++){
                c = cin.get();
                if(c == '\\'){
                    s[i] |= (1<<j);
                }
            }
            cin.get();
            cin.get();// endl
        }
        for(;cin.get()!='\n' && !cin.eof();){}
        cout << s << endl;
    }
}