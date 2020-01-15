
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <algorithm>
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

struct contestant{
    int solved[11][2];
    int incorrect[11];
    bool initializes;
};

bool sortf(const vi &cnt1, const vi &cnt2){

    if(cnt2[1]<cnt1[1]){
        return true;
    }
    else if(cnt2[1]==cnt1[1]){
        if(cnt2[2]>cnt1[2]){
            return true;
        }
        else if(cnt2[2]==cnt1[2]){
            return cnt2[0]>cnt1[0];
        }
    }
    return false;
    /*
    else{
        return (cnt2[0]<cnt1[0]);
    }
    */
}

int main(){
    contestant cnts[101];
    vi kcnts;
    int tests;
    string line;
    vvi scoreboard;
    cin >> tests;
    getline(cin, line);
    getline(cin, line);
    while(tests--){
        FOR(i, 1, 101){
            cnts[i].initializes = true;
        }
        kcnts.clear();
        scoreboard.clear();
        getline(cin, line);
        while(line.length()>6 && !cin.eof()){
            stringstream ssline(line);
            int cnt, problem, stime;
            char L;
            ssline >> cnt >> problem >> stime >> L;

            if(cnts[cnt].initializes){
                cnts[cnt].initializes = false;
                kcnts.PB(cnt);
                FOR(i,1,11){
                    cnts[cnt].incorrect[i] = 0;
                    cnts[cnt].solved[i][0] = 0;
                    cnts[cnt].solved[i][1] = 0;
                }
            }
            if(L=='C'){
                if(cnts[cnt].solved[problem][0] == 0){
                    cnts[cnt].solved[problem][0] = 1;
                    cnts[cnt].solved[problem][1] = stime;
                }
            }
            else if(L=='I'){
                if(cnts[cnt].solved[problem][0] == 0){
                    cnts[cnt].incorrect[problem] += 1;
                }
            }
            getline(cin, line);
        }
        while(!kcnts.empty()){
            vi score;
            int cnt = kcnts.back();
            kcnts.pop_back();
            int total = 0, tp = 0;
            FOR(i,1,11){
                if(cnts[cnt].solved[i][0]==1){
                    total += cnts[cnt].solved[i][1];
                    total += cnts[cnt].incorrect[i]*20;
                    tp+=1;
                }
            }
            score.PB(cnt);
            score.PB(tp);
            score.PB(total);            
            scoreboard.PB(score);
        }
        sort(ALL(scoreboard), sortf);
        REP(i,scoreboard.size()){
            printf("%d %d %d\n",scoreboard[i][0],scoreboard[i][1],scoreboard[i][2]);
        }
        if(tests>0){
            printf("\n");
        }
    }
    return 0;
}