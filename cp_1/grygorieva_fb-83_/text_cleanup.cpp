#include <iostream>
#include <fstream>
#include <istream>
#include<cstdlib>

using namespace std;

char* buffer;
char* only_letters_and_spaces;
char* only_letters;
int length;

int main()
{
    setlocale(LC_ALL, "");

    std::ifstream file;
    file.open("C:\\crypto\\bulgakov.txt");

    std::ofstream file_with_spaces;
    file_with_spaces.open("C:\\crypto\\master-i-margarita.txt");

    std::ofstream file_without_spaces;
    file_without_spaces.open("C:\\crypto\\master-i-margarita_1.txt");


    if (file)
    {
        file.seekg(0, file.end);

        length = file.tellg();
        file.seekg(0, file.beg);
        int n = 0;
        int m = 0;
        buffer = new char[length];
        only_letters_and_spaces = new char[n];
        only_letters = new char[m];

        file.read(buffer, length);

        int temp = 0;
        int var = 0;
        char check = buffer[0];   //this var is used to save the value of a previous character fo r futher comparison

        for (int i = 0; i < length; i++)
        {
            temp = (int)buffer[i];

            if (buffer[i] == 10)    //search for the end of line
            {
                if ((int)check != 32)  //if the previous character is space, there is no need to add another one
                {
                    file_with_spaces << " ";
                    check = ' ';
                }
            }

            if (temp > -33 && temp < 0)   //only lower case russian letters will go
            {
                only_letters_and_spaces[n] = buffer[i];
                check = only_letters_and_spaces[n];
                only_letters[m] = buffer[i];
                file_with_spaces << only_letters_and_spaces[n];
                file_without_spaces << only_letters[m];
            }

            if (temp == 32)
            {
                if ((int)check != 32)  //if the previous character is space, there is no need to add another one
                {
                    file_with_spaces << " ";
                    check = ' ';
                }
            }

            if (temp > -65 && temp < -32)   //only upper case russian letters will go
            {
                var = (int)buffer[i];
                var = var + 32;    //transform upper case into lower
                only_letters_and_spaces[n] = (char)var;
                check = only_letters_and_spaces[n];
                only_letters[m] = (char)var;
                file_with_spaces << only_letters_and_spaces[n];
                file_without_spaces << only_letters[m];
            }
        }
    }
    file.close();
    file_with_spaces.close();
    file_without_spaces.close();
    return 0;
}