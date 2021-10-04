#include <iomanip>
#include <iostream>
using namespace std;

float first(float x, float X) 
{
	return((abs(x - X)) / X);
}

int calc(float x1=0, float x2=0, float x3=0, float x4=0,
		float fx1=1, float fx2=1, float fx3=1, float fx4=1)
{
	double arrX[] = {x1, x2, x3, x4};
	double arrFX[] = {fx1, fx2, fx3, fx4};
	double g, l, r;
	int i, j;

	cout<<"Table of values of a function:"<<endl;
	cout<<"X:";
	for(i=0; i<=3; i++)
	cout<<setw(5)<<arrX[i]<<"|";
	cout<<endl;
	cout<<"Y:";
	for(i=0; i<=3; i++)
	cout<<setw(5)<<arrFX[i]<<"|";
	cout<<endl;
	cout<<endl;
	cout<<"Enter value X: ";
	cin>>r;
	l=0;
	for(i=0; i<=3; i++)
	{
	g=1;
	for(j=0; j<=3; j++)
	{
		if(i != j)
		g = g*((r-arrX[j])/(arrX[i]-arrX[j]));
	}
	l=l+arrFX[i]*g;
	}
	cout<<"Y = "<< l;
	return 0;
}

extern "C" {
    int cppcalc2(float x1=0, float x2=0, float x3=0, float x4=0,
				float fx1=1, float fx2=1, float fx3=1, float fx4=1)
    {
        if (calc(x1, x2, x3, x4, fx1, fx2, fx3, fx4) == 1)
			return 1;
		else
			return 2;
		return 0;
    }
}