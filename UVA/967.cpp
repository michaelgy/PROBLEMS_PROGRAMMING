#include <cmath>
#include <cstdio>
#include<cstdlib>
#include <string>
#define MAX 1e6

int compareints(const void *a, const void *b){
	return (*(int*)a-*(int*)b);
}

using namespace std;

int main(){
	int numbers[(int)MAX/2];
	int primes[(int)(2*MAX/log(MAX))];
	int *pItem;
	int i,j,pcount,k,valor,contador;
	char c;
	string is;
	primes[0] = 2;
	pcount = 1;
	for(i=0;i<MAX/2;i++){
		numbers[i] = 0;
	}
	for(i=0;i<MAX/2;i++){
		if(numbers[i] == 0){
			primes[pcount] = 2*i+3;
			pcount++;
			for(j=3*i+3;j<MAX/2;j+=2*i+3){
				numbers[j]=1;
			}
		}
	}
	int inf,supe;
	for(scanf("%d",&inf);inf>-1;scanf("%d",&inf)){
		contador = 0;
		scanf("%d",&supe);
		for(inf = inf%2==0?inf+1:inf;inf<=supe;inf+=2){
			pItem = (int*)bsearch(&inf,primes,pcount,sizeof(int),compareints);
			if(pItem!=NULL){
				bool esP = true;
				is = to_string(inf);
				for(k=1;k<(int)is.size() && esP;k++){
					c = is[is.size()-1];
					is.pop_back();
					is.insert(0,1,c);
					valor = stoi(is,nullptr);
					pItem = (int*)bsearch(&valor,primes,pcount,sizeof(int),compareints);
					esP = pItem!=NULL;
				}
				if(esP){
					contador++;
					printf("%d\n",inf);
				}
			}
		}
		if(contador == 0){
			printf("No Circular Primes");
		}
		else if (contador == 1){
			printf("%d Circular Prime",contador);
		}
		else{
			printf("%d Circular Primes",contador);
		}
		printf(".\n");
	}
	return 0;
}
