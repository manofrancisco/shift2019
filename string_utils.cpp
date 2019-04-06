//
// Created by Francisco Ferreira on 2019-04-05.
//
#include <iostream>
#include <stdio.h>
using namespace std;

#define NO_OF_CHARS 256


// A utility function to get maximum of two integers
int max(int a, int b)
{
    return (a > b) ? a : b;
}

// The preprocessing function for Boyer Moore's bad character heuristic
void badCharHeuristic(char *str, int size, int badchar[NO_OF_CHARS])
{
    int i;

    // Initialize all occurrences as -1
    for (i = 0; i < NO_OF_CHARS; i++)
        badchar[i] = -1;

    // Fill the actual value of last occurrence of a character
    for (i = 0; i < size; i++)
        badchar[(int) str[i]] = i;
}

int patsearch(char *txt, char *pat)
{
    int m = std::strlen(pat);
    int n = 10000;

    int badchar[NO_OF_CHARS];

    badCharHeuristic(pat, m, badchar);

    int s = 0; // s is shift of the pattern with respect to text
    while (s <= (n - m))
    {
        int j = m - 1;

        while (j >= 0 && pat[j] == txt[s + j])
            j--;

        if (j < 0)
        {
            return s;

            s += (s + m < n) ? m - badchar[txt[s + m]] : 1;

        }

        else
            s += max(1, j - badchar[txt[s + j]]);
    }
    return -1;


}


int test(){
    FILE *f = fopen("digits.pi", "rb");
    fseek(f, 0, SEEK_END);
    long fsize = ftell(f);
    fseek(f, 0, SEEK_SET);
    //char txt[] = "34523012323712575514058317135740048030481764261272684473550571772";
    char* txt = new char[10000];
    fread(txt, 10000, 1, f);
    char pat[] = "2575514058";
    cout << " "<<patsearch(txt,pat);

    return 0;
}