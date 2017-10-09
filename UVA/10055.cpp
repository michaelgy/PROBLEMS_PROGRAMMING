#include <iostream>
#include <cstdlib>
using namespace std;

int main(){
    long n,m;
    for(cin >> n >> m; !cin.eof(); cin >> n >> m){
        cout << abs(m-n) << endl;
    }
    return 0;
}