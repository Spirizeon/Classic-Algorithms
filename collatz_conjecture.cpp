
#include <bits/stdc++.h>
using namespace std;
/*
 if n is even +> half
 if n is odd +> 3n+1
 */

int main()
{
    int c = 0;
    int i;
    cout << "enter number: ";
    cin >> i;
    while(i!=1){
        if(i%2==0){
            i = i/2;
        }
        else{
            i = 3*i + 1;
        }
        cout << i << endl;
        c++;
    }
    cout << "number of steps: " << c;
    return 0;
}