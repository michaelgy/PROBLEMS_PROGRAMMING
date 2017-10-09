#include <stdio.h>
#include <malloc.h>
#include <string.h>

typedef struct lover{
  struct lover *next;
  struct lover *prev;
  char country[75];
  int count,clen;
}love_list;

int country_cmp(love

void insertl(love_list ** root,love_list * element, love_list * new, int inserttype){
  if((*root) == NULL){
    (*root) = new;
  }
  else{
    struct lover * tmp;
    switch (inserttype){
    case 0: //backward to element
      tmp = element->prev;
      
    }
    

void forlist(love_list ** root, love_list * new, int * mindex){
  
}

int main(){
  int n,mindex;
  mindex = 0;
  
  char country[75];
  scanf("%i",&n);
  for(;n>0;n--){
    scanf("%s %*75[^\n]",country);
    printf("%i\n",strcmp(country,"hello"));
  }
  return 0;
}
