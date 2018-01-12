#include <iostream>

using namespace std;

int main(){
    int x,y,z,t,f;
    long count;
    for(cin>>t;t>0;t--){
        count = 0;
        for(cin>>f;f>0;f--){
            cin >> x >> y >> z;
            count += x*z;
        }
        cout << count << endl;
    }
    return 0;
}