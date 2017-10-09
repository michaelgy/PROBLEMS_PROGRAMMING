#include <stdio.h>
#include <stdlib.h>
int cmp_ints(const void*a, const void *b){
  const int *da = (const int*)a;
  const int *db = (const int*)b;
  return (*da > *db)-(*da<*db);
}

int inv_cmp_ints(const void*a, const void *b){
  const int *da = (const int*)a;
  const int *db = (const int*)b;
  return (*db > *da)-(*db<*da);
}

int main(){
  int n,d,r,turns,k,result,morning[100],evening[100];
    scanf("%i %i %i",&n,&d,&r);
    while(n != 0){
        for(turns=0;turns<n;turns++){
            scanf("%i",morning+turns);
        }
        for(turns=0;turns<n;turns++){
            scanf("%i",evening+turns);
        }
	qsort(morning,n,sizeof(int),cmp_ints);
	qsort(evening,n,sizeof(int),inv_cmp_ints);
	result = 0;
	for(turns=0;turns<n;turns++){
	  k = morning[turns]+evening[turns]-d;
	  result +=  k>0?k:0;
        }
	printf("%i\n",result*r);
        scanf("%i %i %i",&n,&d,&r);
    }
    return 0;
}
