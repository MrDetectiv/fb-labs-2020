#include <iostream>
#include <fstream>
#include <istream>
#include<cstdlib>
#include <map>

using namespace std;

class Letter
{
public:
    int ascii_code;
    float times_in_text;
    char symbol;
    float frequency_with_space;
    float frequency_without_space;
};

char* buffer;
int length;
float number_of_bigrams = 0;
float total_number_of_bigrams = 0;
Letter* frequency_for_each_letter;
map <string, float> bigram_and_times_in_text;

void find_bigrams();
void find_bigrams_with_move();
void entropy_for_letters_with_space();
void entropy_for_letters_without_space();
void entropy_for_bigrams();

void show_frequency_for_letters()
{
    cout << "----ASCII--------SYMBOL--------TIMES--------FREQUENCY_1--------FREQUENCY_2----" << endl;
    for (int i = 0; i < 33; i++)
    {
        cout << frequency_for_each_letter[i].ascii_code << "             " << frequency_for_each_letter[i].symbol <<"             "<< frequency_for_each_letter[i].times_in_text << "             " << frequency_for_each_letter[i].frequency_with_space << "              " << frequency_for_each_letter[i].frequency_without_space <<endl;
    }
}

void show_frequency_for_bigrams()
{
    map <string, float> ::iterator it;
    it = bigram_and_times_in_text.begin();
    for (int i = 0; it != bigram_and_times_in_text.end(); it++, i++)
    {
        cout << "." << it->first << ". ";
        printf("%.6f", it->second / total_number_of_bigrams);
            cout << endl;
    }
}

int main()
{
    setlocale(LC_ALL, "");
   
    std::ifstream file;
    int choice;
    cin >> choice;
    if (choice == 1)
    {
        file.open("C:\\crypto\\master-i-margarita.txt"); //file with spaces
    }
    if (choice == 2)
    {
        file.open("C:\\crypto\\master-i-margarita_1.txt"); //file without spaces
    }

    float** letters_array;

    letters_array = new float* [33];
    for (int i = 0; i < 33; i++) 
    {
        letters_array[i] = new float[2];
    }

    int n = -32;
    for (int i = 0; i < 33; i++)
    {
        letters_array[i][0] = n;
        letters_array[i][1] = 0;
        n++;
    }

    letters_array[32][0] = 32;

    float sum = 0;
    if (file)
    {
        file.seekg(0, file.end);

        length = file.tellg();
        file.seekg(0, file.beg);
        buffer = new char[length];

        file.read(buffer, length);

        int temp = 0;

        for (int i = 0; i < length; i++)
        {
            temp = (int)buffer[i];
            if (temp == 32) letters_array[32][1]++;

            for (int j = -32; j < 0; j++)
            {
                if (temp == j)
                {
                    letters_array[j + 32][1]++;
                }
            }
        }
        
        cout << endl;

        for (int i = 0; i < 33; i++) 
        {
            sum = sum + letters_array[i][1];
        }
    }

    else cout << "ERROR_1" << endl;
   
    cout << "SUM: " << (int)sum << endl;

    frequency_for_each_letter = new Letter[33];

    for (int i = 0; i < 33; i++)
    {
        frequency_for_each_letter[i].ascii_code = letters_array[i][0];
        frequency_for_each_letter[i].times_in_text = letters_array[i][1];
        frequency_for_each_letter[i].symbol = letters_array[i][0];
        frequency_for_each_letter[i].frequency_with_space = frequency_for_each_letter[i].times_in_text / sum;
        frequency_for_each_letter[i].frequency_without_space = frequency_for_each_letter[i].times_in_text / (sum - letters_array[32][1]);
    }
    
    //show_frequency_for_letters();
    if (choice == 1)
    {
        entropy_for_letters_with_space();
        for (int i = 0; i < 33; i++)
            cout << frequency_for_each_letter[i].symbol << " " << frequency_for_each_letter[i].frequency_with_space << endl;
    }
    if (choice == 2)
    {
        entropy_for_letters_without_space();
        for (int i = 0; i < 33; i++)
            cout << frequency_for_each_letter[i].symbol << " " << frequency_for_each_letter[i].frequency_without_space << endl;
    }
    

    find_bigrams();
    if (choice == 1) cout << endl << "TEXT WITH SPACES" << endl;
    if (choice == 2) cout << endl << "TEXT WITHOUT SPACES" << endl;
    entropy_for_bigrams();
    //show_frequency_for_bigrams();

    find_bigrams_with_move();
    if (choice == 1) cout << endl << "TEXT WITH SPACES AND MOVES" << endl;
    if (choice == 2) cout << endl << "TEXT WITHOUT SPACES AND MOVES" << endl;
    entropy_for_bigrams();
    //show_frequency_for_bigrams();
    
    file.close();
    for (int i = 0; i < 33; i++) 
    {
        delete[] letters_array[i];
    }
    delete[] letters_array;
    return 0;
}

void entropy_for_letters_with_space()
{
    float h1_with_space = 0;
    for (int i = 0; i < 33; i++)
    {
        h1_with_space = h1_with_space + frequency_for_each_letter[i].frequency_with_space * log2(frequency_for_each_letter[i].frequency_with_space);
    }
    h1_with_space = -h1_with_space;
    cout << "ENTROPY FOR LETTERS WITH SPACES H1 = " << h1_with_space << endl;
}

void entropy_for_letters_without_space()
{
    float h1_without_space = 0;
    for (int i = 0; i < 32; i++)
    {
        h1_without_space = h1_without_space + frequency_for_each_letter[i].frequency_without_space * log2(frequency_for_each_letter[i].frequency_without_space);
    }
    h1_without_space = -h1_without_space;
    cout << "ENTROPY FOR LETTERS WITHout SPACES H1 = " << h1_without_space << endl;
}

void find_bigrams()
{
    bigram_and_times_in_text = { { "",0 } };
    map <string, float> ::iterator it;
    it = bigram_and_times_in_text.begin();

    string temp_str = "";
    int j = 0;

    for (int i = 0; i < length; i = i+2)
    {
        temp_str = buffer[i];
        temp_str = temp_str + buffer[i + 1];
            if (bigram_and_times_in_text.find(temp_str) != bigram_and_times_in_text.end())
            {
                bigram_and_times_in_text[temp_str]++;
            }
    
            else
            {
                bigram_and_times_in_text[temp_str] = 1;
                number_of_bigrams++;
                if (j < 1088) j++;
            }
    }
}

void find_bigrams_with_move()
{
    number_of_bigrams = 0;
    total_number_of_bigrams = 0;
    bigram_and_times_in_text = { { "",0 } };
    map <string, float> ::iterator it;
    it = bigram_and_times_in_text.begin();

    string temp_str = "";
    int j = 0;

    for (int i = 0; i < length; i++)
    {
        temp_str = buffer[i];
        temp_str = temp_str + buffer[i + 1];
        if (bigram_and_times_in_text.find(temp_str) != bigram_and_times_in_text.end())
        {
            bigram_and_times_in_text[temp_str]++;
        }

        else
        {
            bigram_and_times_in_text[temp_str] = 1;
            number_of_bigrams++;
            if (j < 1088) j++;
        }
    }
}

void entropy_for_bigrams()
{
    map <string, float> ::iterator it;
    it = bigram_and_times_in_text.begin();
    for (int i = 0; i < number_of_bigrams; it++, i++)
    {
        total_number_of_bigrams = total_number_of_bigrams + it->second;
    }
    number_of_bigrams = number_of_bigrams - 2;

    float h2 = 0;
    it = bigram_and_times_in_text.begin();
    it++;
    for (int i = 0; i < number_of_bigrams; it++,i++)
    {
        h2 = h2 + (it->second / total_number_of_bigrams) * log2(it->second / total_number_of_bigrams);
    }

    h2 = -0.5*h2;
    cout << "ENTROPY FOR BIGRAMS H2 = " << h2 << endl;
}