#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct ccnt {
	int count;
	string country;
};

bool compare(ccnt& a, ccnt& b){
	return a.country.compare(b.country) <0 ? 1 : 0;
}

int main(){
	int n,i;
	string line,cname;
	getline(cin,line);
	n = stoi(line);
	vector<ccnt> lista;
	vector<ccnt>::iterator iter ;
	bool nbr = true, found;
	while (n && !cin.eof() && nbr){
		n-=1;
		getline(cin,line);
		if(line.find_first_not_of(' ') != string::npos){
			i = line.find(' ');
			cname = line.substr(0,i);
			found = false;
			for( iter = lista.begin(); iter != lista.end() && !found; iter++){
				if(cname.compare(iter->country)==0){
					found = true;
					iter->count+=1;
				}
			}
			if(!found){
				ccnt vi;
				vi.count = 1;
				vi.country = cname;
				lista.push_back(vi);
			}			
		}
		else{
			nbr = false;
		}
	}
	sort(lista.begin(),lista.end(),compare);
	for( iter = lista.begin(); iter != lista.end(); iter++){
		cout << iter->country << " " << iter->count << endl;
	}

	return 0;
}
