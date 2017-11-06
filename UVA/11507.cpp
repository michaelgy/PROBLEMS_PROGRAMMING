#include <iostream>
#include <string>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    int l,i;
    string dir,cdir;
    for(cin>>l;l>0;cin>>l){
        cdir = "+x";
        for(i=1;i<l;i++){
            cin >> dir;
            if(dir != "No"){
                if(cdir == "+x"){
                    cdir = dir;
                }
                else if(cdir == "-x"){
                    if(dir == "+z"){
                        cdir = "-z";
                    }
                    else if(dir == "-z"){
                        cdir = "+z";
                    }
                    else if(dir == "+y"){
                        cdir = "-y";
                    }
                    else{
                        cdir = "+y";
                    }
                }
                else if(cdir == "+y"){
                    if(dir == "+y"){
                        cdir = "-x";
                    }
                    else if(dir == "-y"){
                        cdir = "+x";
                    }
                }
                else if(cdir == "-y"){
                    if(dir == "+y"){
                        cdir = "+x";
                    }
                    else if(dir == "-y"){
                        cdir = "-x";
                    }
                }
                else if(cdir == "+z"){
                    if(dir == "+z"){
                        cdir = "-x";
                    }
                    if(dir == "-z"){
                        cdir = "+x";
                    }
                }
                else if(cdir == "-z"){
                    if(dir == "+z"){
                        cdir = "+x";
                    }
                    if(dir == "-z"){
                        cdir = "-x";
                    }
                }
            }
            //cout << dir << " " << cdir << endl;
        }
        cout << cdir << endl;
    }
    return 0;
}