#include <iostream>
#include <vector>
#include <cctype>

using namespace std;

#define vb vector<int>
#define vvb vector<vb>

bool inside(int a, int b,int x){ //x in [a,b)
    return a<=x && x<b;
}

bool intable(int x){
    return inside(0,8,x);
}

void put_ifnemp(vvb &table, int r, int c){
    if(!table[r][c]){
        table[r][c] = 2;
    }
}

void pawn_movement(vvb &table, char p, int r, int c){
    table[r][c] = 1;
    if(p == 'P'){
        if(intable(r-1)){
            if(intable(c-1)){
                put_ifnemp(table, r-1,c-1);
            }
            if(intable(c+1)){
                put_ifnemp(table, r-1,c+1);
            }
        }
    }
    if(p == 'p'){
        if(intable(r+1)){
            if(intable(c-1)){
                put_ifnemp(table, r+1,c-1);
            }
            if(intable(c+1)){
                put_ifnemp(table, r+1,c+1);
            }
        }
    }
}

void rook_movement(vvb &table, int r, int c){
    int i;
    table[r][c] = true;
    bool nb = true;
    for(i=r+1; intable(i) & nb;i++){
        if(table[i][c] != 1){
            table[i][c] = 2;
        }
        else{
            nb = false;
        }
    }
    nb = true;
    for(i=r-1; intable(i) & nb;i--){
        if(table[i][c] != 1){
            table[i][c] = 2;
        }
        else{
            nb = false;
        }
    }
    nb = true;
    for(i=c-1; intable(i) & nb;i--){
        if(table[r][i] != 1){
            table[r][i] = 2;
        }
        else{
            nb = false;
        }
    }
    nb = true;
    for(i=c+1; intable(i) & nb ;i++){
        if(table[r][i] != 1){
            table[r][i] = 2;
        }
        else{
            nb = false;
        }
    }
    
}

void bishop_movement(vvb &table, int r, int c){
    int i,j;
    table[r][c] =true;
    bool nb;
    nb = true;
    for(i=r+1,j=c+1; intable(i) & intable(j) & nb;i++,j++){
        if(table[i][j]!=1){
            table[i][j] = 2;
        }
        else{
            nb = false;
        }
    }
    nb = true;
    for(i=r-1,j=c+1; intable(i) & intable(j) & nb;i--,j++){
        if(table[i][j]!=1){
            table[i][j] = 2;
        }
        else{
            nb = false;
        }
    }
    nb = true;
    for(i=r-1,j=c-1; intable(i) & intable(j) & nb;i--,j--){
        if(table[i][j]!=1){
            table[i][j] = 2;
        }
        else{
            nb = false;
        }
    }
    nb = true;
    for(i=r+1,j=c-1; intable(i) & intable(j) & nb;i++,j--){
        if(table[i][j]!=1){
            table[i][j] = 2;
        }
        else{
            nb = false;
        }
    }
}

void knight_movement(vvb &table, int r, int c){
    if(intable(r-2)){
        if(intable(c-1)){
            put_ifnemp(table,r-2,c-1);
        }
        if(intable(c+1)){
            put_ifnemp(table,r-2,c+1);
        }
    }
    if(intable(r-1)){
        if(intable(c-2)){
            put_ifnemp(table,r-1,c-2);
        }
        if(intable(c+2)){
            put_ifnemp(table,r-1,c+2);
        }
    }
    if(intable(r+1)){
        if(intable(c-2)){
            put_ifnemp(table,r+1,c-2);
        }
        if(intable(c+2)){
            put_ifnemp(table,r+1,c+2);
        }
    }
    if(intable(r+2)){
        if(intable(c-1)){
            put_ifnemp(table,r+2,c-1);
        }
        if(intable(c+1)){
            put_ifnemp(table,r+2,c+1);
        }
    }
}

void queen_movement(vvb &table, int r, int c){
    bishop_movement(table, r, c);
    rook_movement(table, r, c);
}

void king_movement(vvb &table, int r, int c){
    table[r][c] = true;
    if(intable(r-1)){
        if(intable(c-1)){
            put_ifnemp(table,r-1,c-1);
        }
        put_ifnemp(table,r-1,c);
        if(intable(c+1)){
            put_ifnemp(table,r-1,c+1);
        }
    }
    if(intable(c-1)){
        put_ifnemp(table,r,c-1);
    }
    if(intable(c+1)){
        put_ifnemp(table,r,c+1);
    }
    if(intable(r+1)){
        if(intable(c-1)){
            put_ifnemp(table,r+1,c-1);
        }
        put_ifnemp(table,r+1,c);
        if(intable(c+1)){
            put_ifnemp(table,r+1,c+1);
        }
    }
}

void show(vvb table){
    for(int i = 0; i< 8; i++){
        for(int j = 0; j< 8; j++){
            cout << table[i][j];
        }
        cout << endl;
    }

}
void showc(char ctable[8][8]){
    for(int i = 0; i< 8; i++){
        for(int j = 0; j< 8; j++){
            cout << ctable[i][j];
        }
        cout << endl;
    }
}

void clearts(char ctable[8][8],vvb &table){
    for(int i = 0; i< 8; i++){
        for(int j = 0; j< 8; j++){
            ctable[i][j] = '0';
            table[i][j] = false;
        }
    }
}

void positioning(char ctable[8][8], vvb &table){
    int i,j;
    char v;
    for(i=0;i<8;i++){
        for(j=0;j<8;j++){
            v = ctable[i][j];
            if(v != '0'){
                if(v == 'p' || v == 'P'){
                    pawn_movement(table,v,i,j);
                }
                v = tolower(v);
                if(v == 'r'){
                    rook_movement(table,i,j);
                }
                else if(v == 'n'){
                    knight_movement(table,i,j);
                }
                else if(v == 'b'){
                    bishop_movement(table,i,j);
                }
                else if(v == 'q'){
                    queen_movement(table,i,j);
                }
                else if(v == 'k'){
                    king_movement(table,i,j);
                }
            }
        }
    }
}

int main(){
    vvb table(8,*(new vb(8,false)));
    char ctable[8][8];
    char c,ns[2];
    ns[1] = '\0';
    int i,j,count,k;
    for(cin >> c;!cin.eof();){
        clearts(ctable,table);
        for(i=0;i<8;i++){
            for(j=0;j<8;){
                if(isdigit(c)){
                    ns[0] = c;
                    k = atoi(ns);
                    j += k;
                }
                else{
                    ctable[i][j]=c;
                    table[i][j] = true;
                    j++;
                }
                cin >> c;
            }
            if(i<7){
                cin >> c;
            }
            //cout << "end c " << c  << " ---" << endl;
        }
        positioning(ctable,table);
        /*
        cout << "salida " << endl;
        showc(ctable);
        cout << endl;
        show(table);
        cout << endl;
        */
        count = 0;
        for(i=0;i<8;i++){
            for(j=0;j<8;j++){
                !table[i][j] ? count++:0;
            }
        }
        cout << count << endl;
    }    
    return 0;
}