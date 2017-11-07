#include <stdio.h>


void clear(char code[80],int m){
    int i;
    for(i=0;i<m;i++){
        code[i] = (char)0;
    }
}

int main(){
    int n,l,i,j,cend;
    char code[80],c;
    for(scanf("%d",&n),getchar(); n>0; n--){
        for(l=0, c = getchar(); c!='\n'; l++,c = getchar()){ 
        }
        clear(code,l);
        for(i=0;i<8;i++){
            c = getchar();
            for(j=0;j<l-2;j++){
                c = getchar();
                if(c== '\\'){
                    code[j] |= 1<<i;
                }
            }
            c = getchar();
            c = getchar();
        }
        for(l=0, cend = getchar(); (char) cend!='\n' && cend != EOF; l++,cend = getchar()){}
        c = getchar();
        for(i=0;i<l;i++){
            printf("%c",code[i]);
        }
	if(n>1){
		printf("\n");
	}
    }
	return 0;
}