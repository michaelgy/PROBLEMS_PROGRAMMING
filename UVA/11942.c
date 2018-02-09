#include<stdio.h>

int main(){
	int N,i,ord,ac,ant,d;
	_Bool isord;
	scanf("%d",&N);
	printf("Lumberjacks:\n");
	for(;N>0;N--){
		isord = 1;
		ord = 0;
		scanf("%d",&ant);
		for(i=1;i<10;i++){
			scanf("%d",&ac);
			d = ac-ant;
			if(d>0 && ord<0){
				isord = 0;
			}
			else if(d<0 && ord>0){
				isord = 0;
			}
			else if(ord == 0){
				ord = d;
			}
			ant = ac;
		}
		printf(isord?"Ordered\n":"Unordered\n");
	}
	return 0;
}
