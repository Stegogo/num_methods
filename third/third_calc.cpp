#include <cmath>
#include <string>
#include <iostream>
using namespace std;
const int n=12;

double get_Y(double * y1, double * y2, double * y3, double * y4, double * y5, double t, double h)
{
    double G = (y1[0]+y2[0]*(2*t-1)/2+y3[0]*(3*t*t-6*t+2)/6+y4[0]*(4*t*t*t-18*t*t+
    22*t-6)/24+y5[0]*(5*t*t*t*t-40*t*t*t+105*t*t-100*t+24)/120)/h;  //! NEED FORMULA FOR THE LOWER PART OF THE TABLE
    cout<<"Y' = "<< G << endl;
    return G;
}

double get_YY(double * y1, double * y2, double * y3, double * y4, double * y5, double t, double h)
{
    double L = (y2[0]+y3[0]*(t-1)+y4[0]*(12*t*t-36*t+22)/24+y5[0]*(20*t*t*t-120*t*t+ 210*t-100)/120)/(h*h);
    cout<<"Y\" = " << L << endl;
    return L;
}

double * calc3(double x1, double x2, double x3, double x4, double x5, double x6,
                double x7, double x8, double x9, double x10, double x11, double x12,
                double fx1, double fx2, double fx3, double fx4, double fx5, double fx6,
                double fx7, double fx8, double fx9, double fx10, double fx11, double fx12,
                double n1, double n2)
{
    double X[] = {x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12};
    double Y[] = {fx1, fx2, fx3, fx4, fx5, fx6, fx7, fx8, fx9, fx10, fx11, fx12};
    double xx = n1;
    double h=0;
    int i=1;
    double t=0;
    int k=0;

    double xX = X[0];
    cout << "your x is " << xx << endl;
    for(int l = 0; l < n; l++)
    {
        if (xx < X[l]){
            xX = X[l-1];
            break;
        }
    }
    cout << "your xX is " << xX << endl;

    h=(X[i]-X[i-1]);
    cout << h << endl;
    t=(xx-xX)/h;
    cout << t << endl;

    double y1[n];
    for(int j=1; j<n; j++)
    {
        y1[k]=Y[j]-Y[j-1];
        k++;
    }
    k=0;

    double y2[n];
    for(int j=1; j<n-1; j++)
    {
        y2[k]=y1[j]-y1[j-1];
        k++;
    }
    k=0;

    double y3[n];
    for(int j=1; j<n-2; j++)
    {
        y3[k]=y2[j]-y2[j-1];
        k++;
    }
    k=0;

    double y4[n];
    for(int j=1; j<n-3; j++)
    {
        y4[k]=y3[j]-y3[j-1];
        k++;
    }
    k=0;

    double y5[n];
    for(int j=1; j<n-4; j++)
    {
        y5[k]=y4[j]-y4[j-1];
        k++;
    }

    double res_y = get_Y(y1, y2, y3, y4, y5, t, h);
    double res_yy = get_YY(y1, y2, y3, y4, y5, t, h);

    double * results = new double[2];
    results[0] = res_y;
    results[1] = res_yy;
    return results;
}



extern "C" {
    double * cppcalc3(double x1, double x2, double x3, double x4, double x5, double x6,
                double x7, double x8, double x9, double x10, double x11, double x12,
                double fx1, double fx2, double fx3, double fx4, double fx5, double fx6,
                double fx7, double fx8, double fx9, double fx10, double fx11, double fx12,
                double n1, double n2)
    {
        return (calc3(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12,
            fx1, fx2, fx3, fx4, fx5, fx6, fx7, fx8, fx9, fx10, fx11, fx12,
            n1, n2));
    }
}