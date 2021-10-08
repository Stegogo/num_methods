#include <cmath>
#include <iomanip>
#include <iostream>
using namespace std;

float first(float x, float X) 
{
	return((abs(x - X)) / X);
}

int calc1(float n1=0, float x1=0, float n2=0, float n22=1, float x2=0)
{
	float dx1 = 0;
	dx1 = first(x1, sqrt(n1));

	float dx2 = 0;
	dx2 = first(x2, (n2 / n22));
	
	if (dx1 < dx2)
		return 1;
	else
		return 2;
	return 0;
}

double second(double * arrX, double * arrFX, double p)
{
	double l=0;
	double g = 1;
	for(int i=0; i<=3; i++)
	{
		g = 1;
		for(int j=0; j<=3; j++)
		{
			if(i != j)
			g = g*((p-arrX[j])/(arrX[i]-arrX[j]));
		}
		l=l+arrFX[i]*g;
	}
	return l;
}

double second_single_point(double x1=0, double x2=0, double x3=0, double x4=0,
		double fx1=1, double fx2=1, double fx3=1, double fx4=1, double p=0)
{
	double arrX[] = {x1, x2, x3, x4};
	double arrFX[] = {fx1, fx2, fx3, fx4};
	double l=0;
	double g = 1;
	for(int i=0; i<=3; i++)
	{
		g=1;
		for(int j=0; j<=3; j++)
		{
			if(i != j)
			g = g*((p-arrX[j])/(arrX[i]-arrX[j]));
		}
		l=l+arrFX[i]*g;
	}
	cout << l << endl;
	return l;
}

double * calc2(double x1=0, double x2=0, double x3=0, double x4=0,
		double fx1=1, double fx2=1, double fx3=1, double fx4=1,
		double point1=0, double point2=0, double point3=0, double point4=0)
{
	double arrX[] = {x1, x2, x3, x4};
	double arrFX[] = {fx1, fx2, fx3, fx4};
	double arrP[] = {point1, point2, point3, point4};
	double * arrFP = new double[4];
	double g, l, r;
	
	for(int i = 0; i <= 3; i++)
		arrFP[i] = second(arrX, arrFX, arrP[i]);
	return arrFP;
}

double calc22(double x1=0, double x2=0, double x3=0, double x4=0,
		double fx1=1, double fx2=1, double fx3=1, double fx4=1,
		double p=0)
{
	//double arrX[] = {x1, x2, x3, x4};
	//double arrFX[] = {fx1, fx2, fx3, fx4};
	//double arrP[] = {point1, point2, point3, point4};
	//double * arrFP = new double[4];
	double g, l, r;
	
	double fp = second_single_point(x1, x2, x3, x4, fx1, fx2, fx3, fx4, p);
	return fp;
}

extern "C" {
    int cppcalc1(float n1=0, float x1=0, float n2=0, float n22=1, float x2=0)
    {
        if (calc1(n1, x1, n2, n22, x2) == 1)
			return 1;
		else
			return 2;
		return 0;
    }
	double * cppcalc21(double x1=0, double x2=0, double x3=0, double x4=0,
				double fx1=0, double fx2=0, double fx3=0, double fx4=0,
				double point1=0, double point2=0, double point3=0, double point4=0)
    {
        return calc2(x1, x2, x3, x4,
				fx1, fx2, fx3, fx4,
				point1, point2, point3, point4);
    }
	double cppcalc2(double x1=0, double x2=0, double x3=0, double x4=0,
				double fx1=0, double fx2=0, double fx3=0, double fx4=0,
				double point1=0, double point2=0, double point3=0, double point4=0)
    {
        return calc22(x1, x2, x3, x4,
				fx1, fx2, fx3, fx4,
				point1);
    }
	double second2(double x1=0, double x2=0, double x3=0, double x4=0,
				double fx1=0, double fx2=0, double fx3=0, double fx4=0,
				double p=0)
	{
		return second_single_point(x1, x2, x3, x4,
				fx1, fx2, fx3, fx4,
				p);
	}
}