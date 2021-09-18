#include <cmath>
#include <iostream>
using namespace std;
float first(float, float) ;
float first(float x, float X) 
{
	return (abs(x -X)) / X;
}
int main(int argc, char* argv[])
{
	float x1 = 0;
	cout << "sqrt(n1) = x1 ~ X1 \n";
	cout << "Input n1 = ";
	float n1 = 0;
	cin >> n1;
	float X1 = sqrt(n1);
	cout << "Input x1 = sqrt(n1)= ";
	cin >> x1;
	float dx1 = 0;
	dx1 = first(x1, X1);
	cout << "dx1="<<dx1 << " \n";
	float n2 = 0;
	float N2 = 0;
	cout << "n2/N2 = x2 ~ X2 \n";
	cout << "Input n2 = ";
	cin >> n2;
	cout << "Input N2 = ";
	cin >> N2;
	float X2 = n2 / N2;
	cout << "Input x2 = n2/N2 = ";
	float x2 = 0;
	cin >> x2;
	float dx2 = first(x2, X2);
	cout <<"dx2="<< dx2 << "\n";
	float L_answer = 0;
	if (dx1 < dx2)
		L_answer = dx1;
	else
		L_answer = dx2;
	if (L_answer == dx1)
		cout << "sqrt(" << n1 << ")" << " is more accurate \n";
	else
		cout << n2 << "/" << N2 << " is more accurate \n";
return 0;
}