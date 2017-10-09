/* UNSOLVED */
#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    int b1[3],b2[3],b3[3];
    char assign[3];
    for(cin >> b1[0]; !cin.eof(); cin >> b1[0]){
        cin >> b1[1] >> b1[2];
        cin >> b2[0] >> b2[1] >> b2[2];
        cin >> b3[0] >> b3[1] >> b3[2];

        if(b3[2]>=b2[2]){
            if(b3[2]>=b1[2]){
                assign[2] = 'G';
            }
        }
    }
}
