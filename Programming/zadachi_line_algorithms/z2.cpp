#include <iostream>
#include <cmath>
using namespace std;

int main(){
    double radi;
    cout << "Введите радианы: ";
    cin >> radi;
    double total_grad = radi * 180 / M_PI;
    double grad = floor(total_grad);
    double total_minute = (total_grad - grad) * 60.0;
    double minute = floor(total_minute);
    double second = (total_minute - minute) * 60.0;
    cout << "Градусы: " << grad << " Минуты: " << minute << " Секунды: " << second
    << endl;
    return 0;
}