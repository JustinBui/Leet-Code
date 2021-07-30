#include <iostream>

using namespace std;

// SOLUTION: https://www.youtube.com/watch?v=wAyrtLAeWvI

class Solution
{
private:
    double myPowHelper(double x, long n)
    {
        if (n == 0)
            return 1;
        else if (n % 2 == 0)
        {
            double exp = myPow(x, n / 2);
            return exp * exp;
        }
        else
            return x * myPow(x, n - 1);
    }

public:
    double myPow(double x, int n)
    {
        double res = myPowHelper(x, abs(n));
        if (n < 0)
            return 1 / res;
        else
            return res;
    }
};

int main()
{

    return 0;
}