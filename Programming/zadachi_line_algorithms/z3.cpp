#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int capital, percent, itog_sum;
    cout << "Введите стартовый капитал, ежемес. процент, итоговую сумму: ";
    cin >> capital >> percent >> itog_sum;
    double count_months = (log(itog_sum / capital)) / (log(1.0 + (percent / 100.0)));
    double years = count_months / 12.0;
    cout << "Итоговое кол-во лет: " << years << endl;
    return 0; 
} 