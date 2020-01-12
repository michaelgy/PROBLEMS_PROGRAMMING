#include <iostream>

using namespace std;

//Note: (int)char+128 is used because characters
//of extended ASCII table will char (int)char value
//negative

int main(){
    string line;
    int test;
    cin >> test;
    long long values[256];
    for(;test>0;test--){
        for(int i=0; i<256; i++){
            values[i] = 0;
        }
        long long n, value;
        char c;
        cin >> n;
        getline(cin,line);
        for(; n>0; n--){
            cin.get(c);
            cin >> value;
            //cout << c <<" | " << (int)c+128 << " | "<< value << endl;
            getline(cin,line);
            values[(int)c+128] = value;
        }
        cin >> n;
        getline(cin,line);
        long long total = 0;
        for(;n>0;n--){
            getline(cin,line);
            for(int i = 0; i<line.length(); i++){
                //cout << "|" << line[i] << "|" << (int)line[i]+128;
                total += values[(int)line[i]+128];
            }
        }
        //cout << endl;
        printf("%lld.%02lld$\n",total/100,total%100);
    }
    
    return 0;
}