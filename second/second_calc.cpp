#include <iomanip>
#include <iostream>
using namespace std;

float first(float x, float X) 
{
	return((abs(x - X)) / X);
}

int calc(float n1=0, float x1=0, float n2=0, float n22=1, float x2=0)
{
	double arrX[4] = {0.0, 2.0, 3.0, 5.0};
	double arrFX[4] = {1.0, 3.0, 2.0, 5.0};
	
	return 0;
}

extern "C" {
    int cppcalc2(float n1=0, float x1=0, float n2=0, float n22=1, float x2=0)
    {
        if (calc(n1, x1, n2, n22, x2) == 1)
			return 1;
		else
			return 2;
		return 0;
    }
}