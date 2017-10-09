#include <cstdio>
#include <cctype>
#include <string>
/*Letters from 65 to 90 (A...Z) numbers from 48 to 57 (0...9)*/
char invL[] = {'A','+','+','+','3','+','+','H','I','L','+','J','M','+','O','+','+','+','2','T','U','V','W','X','Y','5'};
char invN[] = {'1','S','E','+','Z','+','+','8','+'};

using namespace std;

void invert(char from[21],char to[21],int l){
    for(int i = 0;i<l;i++){
        to[i] = from[l-i-1];
    }
}

bool replace_invert(char from[21],char to[21],int l){
    char c;
    for(int i = 0;i<l;i++){
        c = from[l-i-1];
        if((int)c >= 65){
            c = invL[(int)c-65];
        }
        else{
            c = invN[(int)c-49];
        }
        if(c!='+'){
            to[i] = c;
        }
        else{
            return false;
        }
    }
    return true;
}

bool equals(char A[21], char B[21],int l){
    for(int i=0;i<l;i++){
        if(A[i] != B[i]){
            return false;
        }
    }
    return true;
}

int main(){
    int i;
    bool m;
    char input[21],r[21],s[21],c;
    c = getchar();
    while(isspace(c)){
        c = getchar();
    }
    while (c != char_traits<char>::eof()){
        i=0;
        while(!isspace(c) && c != char_traits<char>::eof()){
            input[i] = c;
            i+=1;
            c = getchar();
        }
        input[i] = '\0';
        r[i] = '\0';
        s[i] = '\0';
        invert(input,r,i);
        m = replace_invert(input,s,i);
        printf("%s -- ",input);
        if(m){
            if(equals(input,s,i)){
                if(equals(input,r,i)){
                    printf("is a mirrored palindrome.");
                }
                else{
                    printf("is a mirrored string.");
                }
            }
            else{
                if(equals(input,r,i)){
                    printf("is a regular palindrome.");
                }
                else{
                    printf("is not a palindrome.");
                }
            }
        }
        else{
            if(equals(input,r,i)){
                printf("is a regular palindrome.");
            }
            else{
                printf("is not a palindrome.");
            }
        }
        putchar('\n');
        putchar('\n');
        while(isspace(c)){
            c = getchar();
        }
    }
    return 0;
}