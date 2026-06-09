#include <iostream>
#include <fstream>
#include <string>
#include <immintrin.h>

using namespace std;

bool GenerateRandom64(unsigned long long& value)
{
    for (int i = 0; i < 10; i++)
    {
        if (_rdrand64_step(&value))
        {
            return true;
        }
    }

    return false;
}

int main()
{
    char saveToFile;
    cout << "Mentes fajlba? (i/n): ";
    cin >> saveToFile;

    ofstream outputFile;

    if (saveToFile == 'i' || saveToFile == 'I')
    {
        outputFile.open("random.txt");

        if (!outputFile)
        {
            cerr << "Nem sikerult megnyitni a random.txt fajlt!" << endl;
            return 1;
        }
    }

    size_t count;
    cout << "Hany darab 64 bites random szamot generaljak? ";
    cin >> count;

    for (size_t i = 0; i < count; i++)
    {
        unsigned long long rnd;

        if (!GenerateRandom64(rnd))
        {
            cerr << "RDRAND hiba a(z) " << i << ". elemnel!" << endl;
            return 1;
        }

        //cout << rnd << endl;

        if (outputFile.is_open())
        {
            outputFile << rnd << endl;
        }
    }

    if (outputFile.is_open())
    {
        outputFile.close();
    }

    cout << "Kesz." << endl;

    return 0;
}