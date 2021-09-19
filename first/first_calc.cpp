#include <cmath>
#include <iostream>
using namespace std;

float first(float x, float X) 
{
	return((abs(x - X)) / X);
}

int main(float n1=0, float x1=0, float n2=0, float n22=1, float x2=0)
{
	float dx1 = 0;
	dx1 = first(x1, sqrt(n1));

	float dx2 = 0;
	dx2 = first(x2, (n2 / n22));
	
	float L_answer = 0;
	if (dx1 < dx2)
		L_answer = dx1;
	else
		L_answer = dx2;

	if (L_answer == dx1)
		return 1;
	else
		return 2;
return 0;
}