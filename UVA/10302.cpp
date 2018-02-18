#include <iostream>
#include <cmath>

using namespace std;

int main(){
	unsigned long long int i;
	for(cin>>i;!cin.eof();cin>>i){
		cout << ((i*i*(i+1)*(i+1))/4) << endl;
	}
	return 0;
}
