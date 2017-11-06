#include <iostream>
#include <cstdlib>

using namespace std;

#define a psc[0]
#define b psc[1]
#define c psc[2]
#define x pc[0]
#define y pc[1]

int compare(const void *m, const void *n){
    return ( *(int*)m -  *(int*)n );
}

int main(){
    ios::sync_with_stdio(false);
    int psc[3],pc[2],sol;
    cin >> a >> b >> c >> x >> y;
    while (psc[0]){
        qsort(psc,3,sizeof(int),compare);
        qsort(pc,2,sizeof(int),compare);
        
        if(  (y < b) || (x<b && y<c) ){
            sol = -1;
        }
        else if(x<b && c<y){
            sol = c+1;
            if(sol == y){
                sol++;
            }
        }
        else if(b<x && x<c){
            sol = b+1;
            if(sol == x){
                sol++;
            }
            if(sol == c || sol == y){
                sol++;
            }
            if(sol == y || sol == c){
                sol++;
            }
        }
        else{
            sol = 1;
            if(sol == a){
                sol++;
            }
            if(sol == b){
                sol++;
            }
            if(sol == x){
                sol++;
            }
            if(sol == c){
                sol++;
            }
            if(sol == y){
                sol++;
            }

        }
        if(sol == 53){
            sol = -1;
        }
        cout << sol << endl;
        cin >> a >> b >> c >> x >> y;
    }
}