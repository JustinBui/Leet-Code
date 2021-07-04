#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int romanToInt(string);

int main()
{
    cout << romanToInt("III") << endl;
    cout << romanToInt("IV") << endl;
    cout << romanToInt("IX") << endl;
    cout << romanToInt("LVIII") << endl;
    cout << romanToInt("MCMXCIV") << endl;
    return 0;
}

int romanToInt(string s)
{
    int intResult = 0;
    char prev = ' ';
    unordered_map<char, int> myMap =
        {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}};

    for (string::reverse_iterator it = s.rbegin(); it != s.rend(); ++it)
    {

        if (myMap[*it] < myMap[prev])
        {
            intResult -= myMap[*it];
        }
        else
        {
            intResult += myMap[*it];
        }

        prev = *it;
    }

    return intResult;
}