#include <bits/stdc++.h>
using namespace std;

#define MAXN 100001

 int main(){
     int left[MAXN],right[MAXN];
     int B,S,L,R;
     cin >> S >> B;
     while(S>0){
         left[0] = 0;
         left[1] = 0;
         for(int i = 2; i<S+1; i++){
             left[i] = i-1;
         }
         for(int i = 1; i<S; i++){
             right[i] = i+1;
         }
         right[S] = 0;
         right[0] = 0;
         while(B--){
             cin >> L >> R;
             //cout << L << "|"<< R << endl;
             cout << ((left[L]>0) ? to_string(left[L]): "*") << " " << ((right[R]>0) ? to_string(right[R]): "*") << endl;
             right[left[L]] = right[R];
             left[right[R]] = left[L];
         }
         cout << "-" << endl;
         cin >> S >> B;
     }
 }