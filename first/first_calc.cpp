#include <cmath>
#include <iostream>
using namespace std;

float first(float x, float X) 
{
	return((abs(x - X)) / X);
}

int main(int argc, char* argv[])
{
	float n1 = 0;
	cin >> n1;

	float x1 = 0;
	cin >> x1;

	float dx1 = 0;
	dx1 = first(x1, sqrt(n1));
	
	cout << "dx1="<<dx1 << " \n";

	float n2 = 0;
	cin >> n2;
		float N2 = 0;
	cin >> N2;

	float x2 = 0;
	cin >> x2;

	float dx2 = 0;
	dx2 = first(x2, (n2 / N2));

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