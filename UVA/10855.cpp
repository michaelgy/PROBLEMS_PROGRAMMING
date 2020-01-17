
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <bitset>
using namespace std;

typedef long long               ll;
typedef long double             ld;
typedef vector<int>             vi;
typedef vector<vi>              vvi;
typedef pair<int, int>          pii;
typedef vector<pii>             vii; // vector of integer pairs
typedef set<int>                si;
typedef map<string, int>        msi;

#define VAR(a,b)        __typeof(b) a=(b)
#define REP(i,n)        for(int i=0;i<(n);++i)     // 0 to n
#define FOR(i,a,b)      for(VAR(i,a);i<=(b);++i)  // a to b, a < b
#define FORD(i,a,b)     for(VAR(i,a);i>=(b);--i)  // a to b, a > b
#define FORE(a,b)       for(VAR(a,(b).begin());a!=(b).end();++a) // for each, e.g. FORE(iter, vect) cout << *iter << endl;
#define SIZE(a)         ((int)((a).size())) // e.g. for (int i = 0; i < SIZE(vect); ++i)
#define ALL(v)          (v).begin(),(v).end() // e.g. sort(ALL(vect))
#define FILL(x,a)       memset(x,a,sizeof(x))
#define CLR(x)          memset(x,0,sizeof(x))
#define VE              vector<int>
#define SZ(v)           ((int)(v).size())
#define PB              push_back
#define MP              make_pair
#define FI              first
#define SE              second
#define TRsi(c,it)      for(si::iterator it=(c).begin();it!=(c).end();it++) // cout << " " << *it;
#define TRvii(c,it)     for(vii::iterator it=(c).begin();it!=(c).end();it++) // cout << " " << *it;
#define TRmsi(c,it)     for(msi::iterator it=(c).begin();it!=(c).end();it++)
#define INF             2000000000 // 2 billion
#define SQ(x)           ((x)*(x))
#define getLastDigit(i) i%10
#define remLastDigit(i) i/10
#define char2int(c)     c-0
#define char2idx(c)     c-'a'

const double PI=acos(-1.0); //NOTES: PI
const double EPS=1e-11; //NOTES: EPS

// Translator
bool isUpper(char c){return c>='A' && c<='Z';} //NOTES: isUpper(
bool isLower(char c){return c>='a' && c<='z';} //NOTES: isLower(
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';} //NOTES: isLetter(
bool isDigit(char c){return c>='0' && c<='9';} //NOTES: isDigit(
char toLower(char c){return (isUpper(c))?(c+32):c;} //NOTES: toLower(
char toUpper(char c){return (isLower(c))?(c-32):c;} //NOTES: toUpper(

// Numeric functions
bool isPowOf2(int i){return (i & i-1) == 0;} //NOTES: isPowOf2

typedef vector<char> vc;
typedef vector<vc> vvc;
vvc rotate(vvc matrix){
    vvc rmatrix;
    REP(i, matrix.size()){
        vc row;
        REP(j, matrix.size()){
            row.PB(matrix[matrix.size()-1-j][i]);
        }
        rmatrix.PB(row);
    }
    return rmatrix;
}

void cmatrix(vvc matrix){
    REP(i,matrix.size()){
        REP(j,matrix.size()){
            cout << matrix[i][j];
        }
        cout << endl;
    }
}

int main(){
    int N,n,total;
    bool equal;
    cin >> N >> n;
    vvc bmatrix, smatrix;
    string line;
    while(N>0){
        bmatrix.clear();
        smatrix.clear();
        REP(i, N){
            vc row;
            cin >> line;
            FORE(itc, line){
                row.PB((*itc));
            }
            bmatrix.PB(row);
        }
        REP(i, n){
            vc row;
            cin >> line;
            FORE(itc, line){
                row.PB((*itc));
            }
            smatrix.PB(row);
        }
        REP(k,4){
            total = 0;
            REP(i,N-n+1){
                REP(j,N-n+1){
                    equal = true;
                    for(int is=0; is<n && equal; is++){
                        for(int js=0; js<n && equal; js++){
                            equal = smatrix[is][js] == bmatrix[is+i][js+j];
                        }
                    }
                    if(equal){
                        total += 1;
                    }
                }
            }
            //cmatrix(smatrix);
            //cout << endl;
            smatrix = rotate(smatrix);
            cout << total;
            if(k==3){
                cout << endl;
            }
            else{
                cout << " ";
            }
        }
        cin >> N >> n;
    }
    return 0;
}