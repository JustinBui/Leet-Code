// Soluion: https://www.youtube.com/watch?v=Y0lT9Fck7qI
#include <iostream>

using namespace std;

int climbStairs(int);

int main()
{

    return 0;
}

// BOTTOM UP APPROACH
int climbStairs(int n)
{
    int oneStep = 1, twoSteps = 1;

    for (int i = 0; i < n - 1; ++i)
    {
        int temp = oneStep;
        oneStep = temp + twoSteps;
        twoSteps = temp;
    }

    return oneStep;
}