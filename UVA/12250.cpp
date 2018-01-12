#include <iostream>
#include <string>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    string w;
    int i;
    for(cin>>w,i = 1;w.compare("#");cin>>w,i++){
        cout << "Case " << i << ": ";
        if(!w.compare("HELLO")){
            cout << "ENGLISH";
        }
        else if(!w.compare("HOLA")){
            cout << "SPANISH";
        }
        else if(!w.compare("HALLO")){
            cout << "GERMAN";
        }
        else if(!w.compare("BONJOUR")){
            cout << "FRENCH";
        }
        else if(!w.compare("CIAO")){
            cout << "ITALIAN";
        }
        else if(!w.compare("ZDRAVSTVUJTE")){
            cout << "RUSSIAN";
        }
        else{
            cout << "UNKNOWN";
        }
        cout << endl;
    }
    return 0;
}