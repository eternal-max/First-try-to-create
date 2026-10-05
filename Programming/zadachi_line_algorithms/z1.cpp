#include <iostream>
#include <cmath>
using namespace std;

int main(void){
    int grad = 120;
    int minute = 30;
    int second = 45;
    double angle_grad = grad + minute/60.0 + second/3600.0;
    double angle_rad = angle_grad * M_PI/180.0;

    cout << "Angle(grad): " << grad << " " << minute << " " << second << " = " 
    << angle_rad << " (rad)" << endl;
    return 0;
}