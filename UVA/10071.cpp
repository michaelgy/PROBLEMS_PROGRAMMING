#include <iostream>

using namespace std;

int main(){
    int n,m;
    for(cin >> n >> m; !cin.eof(); cin >> n >> m){
        cout << n*m*2 << endl;
    }
    return 0;
}