#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int main(){
    ios::sync_with_stdio(false);
    int median[999];
    int i,l;
    cin >> i;
    l=2;
    if(!cin.eof()){
        cout << i << endl;
        median[0] = i;
    }
    for(cin >> i; !cin.eof(); cin>>i,l++){
        median[l-1] = i;
        sort(median.begin(),median.end());
        if(l%2==0){
            cout << (median[l/2]+median[l/2-1])/2 << endl;
        }
        else{
            cout << median[(l-1)/2] << endl;
        }
    }
    return 0;
}