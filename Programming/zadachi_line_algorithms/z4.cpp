#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int a, b, c;
    cout << "Введите a, b, c: ";
    cin >> a >> b >> c;
    float verh_x = (-b / (2 * a));
    float verh_y = c - ((pow(b, 2)) / (4 * a));
    cout << "Вершина параболы (" << verh_x 
    << ";" << verh_y << ")" << endl;
    return 0;
}