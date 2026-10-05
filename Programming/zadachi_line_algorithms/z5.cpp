#include <iostream>
using namespace std;

int main(){
    int h, m, s;
    cout << "Enter the time hh, mm, ss: ";
    cin >> h >> m >> s;
    int t = h * 3600 + m * 60 + s;
    int minutes = (t + 30) / 60;
    cout << "Time in hh, mm: " << minutes / 60 << " " << minutes % 60 << endl;
    cout << "Time only in hour: " << (t + 1800) / 3600 << endl;
}