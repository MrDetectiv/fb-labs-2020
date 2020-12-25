#include <iostream>
#include <fstream>
#include <istream>
#include<cstdlib>

using namespace std;

class Letter
{
public:
    int ascii_code;
    float times_in_text;
    char symbol;
    int number_in_alphabet;
};

int key_array[15];
char* buffer;
int length;
Letter* frequency_for_each_letter;
float general_coincedence_index;

class Blocks
{
public:
    int key_length;
    int block_length;
    Letter frequency_for_each_letter [32];
    float coincedence_index;
};

void split_into_blocks_and_analys(int, string );
void encrypt(int* key_in_numbers_array, int key_len, string file_to_write_to);
void get_encryption_done();
void decrypt(int*);
int* form_key_array(int key_len, string key);

int main()
{
    setlocale(LC_ALL, "");

    get_encryption_done();

    cout  << endl << "OPEN TEXT COINCEDENCE INDEX CALCULATION" << endl;
    split_into_blocks_and_analys(1, "C:\\crypto\\text_to_encrypt.txt");

    cout << endl << "ENCRYPTED BY KEY WITH LENGHT 2 TEXT COINCEDENCE INDEX CALCULATION" << endl;
    split_into_blocks_and_analys(1, "C:\\crypto\\encrypted_by_key2.txt");

    cout << endl << "ENCRYPTED BY KEY WITH LENGHT 3 TEXT COINCEDENCE INDEX CALCULATION" << endl;
    split_into_blocks_and_analys(1, "C:\\crypto\\encrypted_by_key3.txt");

    cout << endl << "ENCRYPTED BY KEY WITH LENGHT 4 TEXT COINCEDENCE INDEX CALCULATION" << endl;
    split_into_blocks_and_analys(1, "C:\\crypto\\encrypted_by_key4.txt");

    cout << endl << "ENCRYPTED BY KEY WITH LENGHT 5 TEXT COINCEDENCE INDEX CALCULATION" << endl;
    split_into_blocks_and_analys(1, "C:\\crypto\\encrypted_by_key5.txt");

    cout << endl << "ENCRYPTED BY KEY WITH LENGHT 14 TEXT COINCEDENCE INDEX CALCULATION" << endl;
    split_into_blocks_and_analys(1, "C:\\crypto\\encrypted_by_key14.txt");

    /*
    for (int i = 2; i < 31; i++)
    {
        split_into_blocks_and_analys(i, "C:\\crypto\\lab2_var7.txt");
        cout << "FOR KEY LENGTH " << i << " COINCEDENCE INDEX IS " << general_coincedence_index / i << endl;
    }
   */
    split_into_blocks_and_analys(15, "C:\\crypto\\lab2_var7.txt");  //cuz key length is 15 characters
    

    cout << "SO THE KEY IS: " << endl;
    for (int i = 0; i < 15; i++)
    {
        if (i != 0) cout << ", ";
        cout << key_array[i];
    }

    key_array[6] = 14;   //change this element cuz it was wrongly calculated by algorihm

    decrypt(key_array);
    return 0;
}

int* form_key_array(int key_len, string key)
{
    cout << "KEY WITH " << key_len << " LENGTH: ";
    int* key_in_number_array = new int[key_len];
    for (int i = 0; i < key_len; i++)
    {
        key_in_number_array[i] = (int)key[i] + 32;
    }
    for (int i = 0; i < key_len; i++)
    {
        if (i != 0) cout << ", ";
       cout << key_in_number_array[i];
    }
    cout << endl;
    return key_in_number_array;
}

void encrypt(int* key_in_numbers_array, int key_len, string file_to_write_to)
{
    cout << endl << "************************************************************" << endl;
    cout << "ENCRYPTING TEXT WITH KEY LENGHT " << key_len << ": " << endl;
    std::ifstream file;
    file.open("C:\\crypto\\text_to_encrypt.txt");
    std::ofstream file_for_encrypted_text;
    file_for_encrypted_text.open(file_to_write_to);

    if (file)
    {
        file.seekg(0, file.end);

        length = file.tellg();
        file.seekg(0, file.beg);
        buffer = new char[length];

        file.read(buffer, length);

        int temp = 0;
        char encrypted_symbol = ' ';
        int p = 0;
        
            for (int m = 0; m < length; m++)
            {
                temp = (int)buffer[m];
                temp = temp + 32;
                if (p / (key_len - 1) != 1)
                {
                    temp = (temp + key_in_numbers_array[p]) % 32;
                    p++;
                }
                else
                {
                    temp = (temp + key_in_numbers_array[p]) % 32;
                    p = p - key_len + 1;
                }
                temp = temp - 32;
                encrypted_symbol = (char)temp;
                cout << encrypted_symbol;
                file_for_encrypted_text << encrypted_symbol;
            }
        
    }
    else cout << "ERROR_1" << endl;

    cout << endl;

    file.close();
    file_for_encrypted_text.close();
}

void get_encryption_done()
{
    string key_2 = "да";
    string key_3 = "нет";
    string key_4 = "идея";
    string key_5 = "мечта";
    string key_14 = "вселеннаязнает";

    int* key_2_in_numbers_array = new int[key_2.length()];
    int* key_3_in_numbers_array = new int[key_3.length()];
    int* key_4_in_numbers_array = new int[key_4.length()];
    int* key_5_in_numbers_array = new int[key_5.length()];
    int* key_14_in_numbers_array = new int[key_14.length()];

    key_2_in_numbers_array = form_key_array(key_2.length(), key_2);
    key_3_in_numbers_array = form_key_array(key_3.length(), key_3);
    key_4_in_numbers_array = form_key_array(key_4.length(), key_4);
    key_5_in_numbers_array = form_key_array(key_5.length(), key_5);
    key_14_in_numbers_array = form_key_array(key_14.length(), key_14);

    encrypt(key_2_in_numbers_array, key_2.length(), "C:\\crypto\\encrypted_by_key2.txt");
    encrypt(key_3_in_numbers_array, key_3.length(), "C:\\crypto\\encrypted_by_key3.txt");
    encrypt(key_4_in_numbers_array, key_4.length(), "C:\\crypto\\encrypted_by_key4.txt");
    encrypt(key_5_in_numbers_array, key_5.length(), "C:\\crypto\\encrypted_by_key5.txt");
    encrypt(key_14_in_numbers_array, key_14.length(), "C:\\crypto\\encrypted_by_key14.txt");
}

void split_into_blocks_and_analys(int r, string file_path)
{
    setlocale(LC_ALL, "");
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ KEY LENGTH " << r << " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;

    Blocks* block = new Blocks[r];
    int i = 0;
    for (int i = 0; i < r; i++)
    {
        if(i==0) general_coincedence_index = 0;
        std::ifstream file;
        file.open(file_path);

        block[i].block_length = 0;
        block[i].key_length = r;
        int n = -32;
        for (int j = 0; j < 32; j++)
        {
            block[i].frequency_for_each_letter[j].ascii_code = n;
            block[i].frequency_for_each_letter[j].symbol = (char)n;
            block[i].frequency_for_each_letter[j].times_in_text = 0;
            block[i].frequency_for_each_letter[j].number_in_alphabet = j;
            n++;
        }
        block[i].block_length = 0;

        if (file)
        {
            file.seekg(0, file.end);

            length = file.tellg();
            file.seekg(0, file.beg);
            buffer = new char[length];

            file.read(buffer, length);

            int temp = 0;

            for (int m = i; m < length; m = m + r)
            {
                temp = (int)buffer[m];

                for (int j = -32; j < 0; j++)
                {
                    if (temp == j)
                    {
                        block[i].frequency_for_each_letter[j + 32].times_in_text++;
                    }
                }
            }

            for (int j = 0; j < 32; j++)
            {
                cout << block[i].frequency_for_each_letter[j].symbol <<  " - " << block[i].frequency_for_each_letter[j].number_in_alphabet << " - "<< block[i].frequency_for_each_letter[j].times_in_text << endl;
            }

            cout << endl;

            for (int j = 0; j < 32; j++)
            {
                block[i].block_length = block[i].block_length + block[i].frequency_for_each_letter[j].times_in_text;
            }
        }
        else cout << "ERROR_1" << endl;

        cout << "BLOCK LENGTH " << i+1 << " IS: " << block[i].block_length << endl;
        float coincidence_index = 0;
        for (int j = 0; j < 32; j++)
        {
            coincidence_index = coincidence_index + (block[i].frequency_for_each_letter[j].times_in_text) * (block[i].frequency_for_each_letter[j].times_in_text - 1);
        }

        float koef = block[i].block_length * block[i].block_length - block[i].block_length;
        koef = 1 / koef;
        coincidence_index = koef * coincidence_index;

        cout << "COINCIDENCE INDEX FOR BLOCK " << i+1 << " = " << coincidence_index << endl;
        block[i].coincedence_index = coincidence_index;

        if (file_path == "C:\\crypto\\lab2_var7.txt")
        {
            int temp = 0;
            int the_most_frequent_character = block[i].frequency_for_each_letter[0].times_in_text;
            for (int j = 0; j < 32; j++)
            {
                if (block[i].frequency_for_each_letter[j].times_in_text > the_most_frequent_character)
                {
                    the_most_frequent_character = block[i].frequency_for_each_letter[j].times_in_text;
                    temp = j;
                }
            }

            if ((block[i].frequency_for_each_letter[temp].ascii_code + 32) >= 14)
                key_array[i] = block[i].frequency_for_each_letter[temp].ascii_code + 32 - 14;
            else
            {
                key_array[i] = block[i].frequency_for_each_letter[temp].ascii_code + 64 - 14;
            }
        }
        file.close();
        general_coincedence_index = general_coincedence_index + block[i].coincedence_index;
    }
}

void decrypt(int* key_array)
{
    cout << endl << endl << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;
    cout << "DECRYPTED TEXT:" << endl;
    std::ifstream file;
    file.open("C:\\crypto\\lab2_var7.txt");

    if (file)
    {
        file.seekg(0, file.end);

        length = file.tellg();
        file.seekg(0, file.beg);
        buffer = new char[length];

        file.read(buffer, length);

        int temp = 0;
        int p = 0;
        int y = 0;
        char open_text_letter = ' ';

        for (int m = 0; m < length; m++)
        {
            temp = (int)buffer[m];
            temp = temp + 32;
            temp = 32 + temp - key_array[p];
            temp = temp % 32;
            temp = temp - 32;
            open_text_letter = (char)temp;

            cout << open_text_letter;
            if (p / 14 == 1) p = p - 14;
            else p++;
        }
    }
    cout << endl;
    file.close();
}