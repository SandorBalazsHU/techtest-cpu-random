#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

int main()
{
    char saveToFileAnswer;
    char printToConsoleAnswer;
    unsigned long long count;

    std::cout << "Szeretned fajlba menteni az eredmenyt? (i/n): ";
    std::cin >> saveToFileAnswer;

    std::cout << "Szeretned a szamokat konzolra irni? (i/n): ";
    std::cin >> printToConsoleAnswer;

    std::cout << "Hany szamot szeretnel generalni? ";
    std::cin >> count;

    bool saveToFile =
        saveToFileAnswer == 'i' ||
        saveToFileAnswer == 'I';

    bool printToConsole =
        printToConsoleAnswer == 'i' ||
        printToConsoleAnswer == 'I';

    std::ofstream outputFile;

    if (saveToFile)
    {
        outputFile.open("random.txt");

        if (!outputFile.is_open())
        {
            std::cerr << "Hiba: nem sikerult megnyitni a random.txt fajlt irasra." << std::endl;
            return 1;
        }
    }

    for (unsigned long long i = 0; i < count; ++i)
    {
        int value = std::rand();

        if (printToConsole)
        {
            std::cout << value << std::endl;
        }

        if (saveToFile)
        {
            outputFile << value << '\n';
        }
    }

    if (outputFile.is_open())
    {
        outputFile.close();
    }

    std::cout << "Kesz." << std::endl;

    return 0;
}