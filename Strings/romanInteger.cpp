#include <iostream>
#include <string>

using namespace std;

int romanToInt(string);

int main()
{
    cout << romanToInt("IV") << endl; // MCMXCIV
    return 0;
}

int romanToInt(string s)
{

    int intResult = 0;
    char prev = ' ';

    for (string::iterator curr = s.begin(); curr != s.end(); ++curr)
    {
        if (*curr == 'I')
            intResult += 1;
        else if (*curr == 'V')
        {
            if (prev == 'I')
                intResult += 4;
            else
                intResult += 5;
        }
        else if (*curr == 'X')
        {
            if (prev == 'I')
                intResult += 9;
            else
                intResult += 10;
        }
        else if (*curr == 'L')
        {
            if (prev == 'X')
                intResult += 40;
            else
                intResult += 50;
        }
        else if (*curr == 'C')
        {
            if (prev == 'X')
                intResult += 90;
            else
                intResult += 100;
        }
        else if (*curr == 'D')
        {
            if (prev == 'C')
                intResult += 400;
            else
                intResult += 500;
        }
        else if (*curr == 'M')
        {
            if (prev == 'C')
                intResult += 900;
            else
                intResult += 1000;
        }
        prev = *curr;
    }

    return intResult;
}