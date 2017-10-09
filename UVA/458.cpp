#include <cstdio>
#include <string>

using namespace std;

int main(){
    char c;
    for(c=getchar();c != char_traits<char>::eof();c=getchar()){
        if(c!='\n'){
            c = (char)((int)c-7);
        }
        putchar(c);
    }
    return 0;
}