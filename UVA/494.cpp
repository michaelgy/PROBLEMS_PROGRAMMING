#include <cctype>
#include <cstdio>
#include <string>

using namespace std;

int main(){
    bool p;
    int count;
    char c;
    c = getchar();
    p = false;
    count = 0;
    while(c!=char_traits<char>::eof()){
        if(isalpha(c)){
            if(!p){
                p = true;
                count +=1;
            }
        }
        else{
            p=false;
        }
        c = getchar();
        if(c=='\n'){
            printf("%d\n",count);
            count = 0;
        }
        if(c==char_traits<char>::eof()){
            printf("%d",count);
        }
    }
}