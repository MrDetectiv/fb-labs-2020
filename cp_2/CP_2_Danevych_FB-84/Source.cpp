#include <string>
#include <iostream>
#include <fstream>
#include <map>

using namespace std;

char symbol;

void cleaning()
{
    ifstream input("text.txt");
    ofstream out("text_clean.txt");
    string upper = "јЅ¬√ƒ≈∆«»… ЋћЌќѕ–—“”‘’÷„ЎўЏџ№Ёёя®";
    int n = 0;
    string str;
    while (!input.eof())
    {
        str.clear();
        input >> str;
        size_t position = str.find_first_of("ЕЦ<>{}[]()*-_;:.,/'!~?1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm");

        while (position != std::string::npos)
        {
            str.erase(position, 1);
            position = str.find_first_of("ЕЦ<>{}[]()*-_;:.,/'!~?1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm");
        }
        for (auto& member : str)
        {
            if (find(upper.begin(), upper.end(), member) != upper.end())
            {
                member += 32;
            }

        }
        if (str != "")
        {
            n++;
            out << str;

        }
    }
    input.close();
    out.close();
}

void cipher(int key_lenght, string key, string name_file)
{
    map<int, char> container_symbols = { {0, 'а'}, {1, 'б'}, {2, 'в'}, {3, 'г'},
    {4, 'д'}, {5, 'е'}, {6, 'Є'}, {7, 'ж'}, {8, 'з'}, {9, 'и'}, {10, 'й'}, {11, 'к'}, {12, 'л'},
    {13, 'м'}, {14, 'н'}, {15, 'о'}, {16, 'п'}, {17, 'р'}, {18, 'с'}, {19, 'т'}, {20, 'у'}, {21, 'ф'},
    {22, 'х'}, {23, 'ц'}, {24, 'ч'}, {25, 'ш'}, {26, 'щ'}, {27, 'ъ'}, {28, 'ы'}, {29, 'ь'}, {30, 'э'}, {31, 'ю'}, {32, '€'} };

    ifstream in_file("text_clean.txt");
    ofstream out_file(name_file);

    int i = 0, r = 0;

    char* key_char = new char[key_lenght];
    for (auto& m : key)
    {
        key_char[i] = m;
        i++;
    }
    i = 0;
    while (!in_file.eof())
    {
        while (!in_file.eof())
        {
            symbol = in_file.get();

            if (symbol != '\n')
            {
                break;
            }
        }

        if (symbol != '\n')
        {
            for (auto& mem : container_symbols)
            {
                if (key_char[r] == mem.second)
                {
                    i = mem.first;
                    for (auto& member : container_symbols)
                    {
                        if (symbol == member.second)
                        {
                            i += member.first;
                            i %= 33;
                            out_file << container_symbols[i];

                            break;
                        }
                    }
                    r++;
                    r %= key_lenght;
                    break;
                }

            }
        }
    }

    in_file.close();
    out_file.close();
    delete[] key_char;
}

double index(string name_file)
{
    ifstream in_file_index(name_file);

    map<char, int> container_symbols;

    long count_symbols = 0;


    while (!in_file_index.eof())
    {
        while (!in_file_index.eof())
        {
            symbol = in_file_index.get();

            if (symbol != '\n')
            {
                break;
            }
        }

        if (symbol != '\n')
        {
            container_symbols[symbol] += 1;

            ++count_symbols;
        }
    }
    int size_container_symbols = 0;
    for (auto& member : container_symbols)
    {
        size_container_symbols++;
    }

    double index_;
    int* index = new int[size_container_symbols];
    int i = 0;
    double sum = 0;


    for (auto& member : container_symbols)
    {
        index[i] = member.second * (member.second - 1);
        i++;
    }

    for (int q = 0; q < size_container_symbols; q++)
    {
        sum += index[q];
    }
    index_ = sum / (count_symbols * (count_symbols - 1));
    // std::cout << index_ << endl;

    return index_;
    in_file_index.close();
    delete[] index;
}

void breaking_into_blocks()
{
    int number_of_blocks = 2;
    while (number_of_blocks <= 30)
    {
        ifstream in_file_blocks("test.txt");
        in_file_blocks.seekg(0, std::ios::beg);
        ofstream out_file_blocks1("test1.txt");
        out_file_blocks1.seekp(0, std::ios::beg);
        ofstream out_file_blocks2("test2.txt");
        out_file_blocks2.seekp(0, std::ios::beg);
        ofstream out_file_blocks3("test3.txt");
        ofstream out_file_blocks4("test4.txt");
        ofstream out_file_blocks5("test5.txt");
        ofstream out_file_blocks6("test6.txt");
        ofstream out_file_blocks7("test7.txt");
        ofstream out_file_blocks8("test8.txt");
        ofstream out_file_blocks9("test9.txt");
        ofstream out_file_blocks10("test10.txt");
        ofstream out_file_blocks11("test11.txt");
        ofstream out_file_blocks12("test12.txt");
        ofstream out_file_blocks13("test13.txt");
        ofstream out_file_blocks14("test14.txt");
        ofstream out_file_blocks15("test15.txt");
        ofstream out_file_blocks16("test16.txt");
        ofstream out_file_blocks17("test17.txt");
        ofstream out_file_blocks18("test18.txt");
        ofstream out_file_blocks19("test19.txt");
        ofstream out_file_blocks20("test20.txt");
        ofstream out_file_blocks21("test21.txt");
        ofstream out_file_blocks22("test22.txt");
        ofstream out_file_blocks23("test23.txt");
        ofstream out_file_blocks24("test24.txt");
        ofstream out_file_blocks25("test25.txt");
        ofstream out_file_blocks26("test26.txt");
        ofstream out_file_blocks27("test27.txt");
        ofstream out_file_blocks28("test28.txt");
        ofstream out_file_blocks29("test29.txt");
        ofstream out_file_blocks30("test30.txt");

        int number_of_leter = 0;

        while (!in_file_blocks.eof())
        {
            while (!in_file_blocks.eof())
            {
                symbol = in_file_blocks.get();
                number_of_leter++;

                if (symbol != '\n')
                {
                    break;
                }
            }

            if (number_of_leter == 1)
            {
                out_file_blocks1 << symbol;
            }
            if (number_of_leter == 2)
            {
                out_file_blocks2 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 3)
            {
                out_file_blocks3 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 4)
            {
                out_file_blocks4 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 5)
            {
                out_file_blocks5 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 6)
            {
                out_file_blocks6 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 7)
            {
                out_file_blocks7 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 8)
            {
                out_file_blocks8 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 9)
            {
                out_file_blocks9 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 10)
            {
                out_file_blocks10 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 11)
            {
                out_file_blocks11 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 12)
            {
                out_file_blocks12 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 13)
            {
                out_file_blocks13 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 14)
            {
                out_file_blocks14 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 15)
            {
                out_file_blocks15 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 16)
            {
                out_file_blocks16 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 17)
            {
                out_file_blocks17 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 18)
            {
                out_file_blocks18 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 19)
            {
                out_file_blocks19 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 20)
            {
                out_file_blocks20 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 21)
            {
                out_file_blocks21 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 22)
            {
                out_file_blocks22 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 23)
            {
                out_file_blocks23 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 24)
            {
                out_file_blocks24 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 25)
            {
                out_file_blocks25 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 26)
            {
                out_file_blocks26 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 27)
            {
                out_file_blocks27 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 28)
            {
                out_file_blocks28 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 29)
            {
                out_file_blocks29 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }
            if (number_of_leter == 30)
            {
                out_file_blocks30 << symbol;
                if (number_of_leter == number_of_blocks)
                {
                    number_of_leter = 0;
                }
            }

        }

        out_file_blocks1.close();
        out_file_blocks2.close();
        out_file_blocks3.close();
        out_file_blocks4.close();
        out_file_blocks5.close();
        out_file_blocks6.close();
        out_file_blocks7.close();
        out_file_blocks8.close();
        out_file_blocks9.close();
        out_file_blocks10.close();
        out_file_blocks11.close();
        out_file_blocks12.close();
        out_file_blocks13.close();
        out_file_blocks14.close();
        out_file_blocks15.close();
        out_file_blocks16.close();
        out_file_blocks17.close();
        out_file_blocks18.close();
        out_file_blocks19.close();
        out_file_blocks20.close();
        out_file_blocks21.close();
        out_file_blocks22.close();
        out_file_blocks23.close();
        out_file_blocks24.close();
        out_file_blocks25.close();
        out_file_blocks26.close();
        out_file_blocks27.close();
        out_file_blocks28.close();
        out_file_blocks29.close();
        out_file_blocks30.close();

        double* index1 = new double[number_of_blocks];
        int num_of_blocks = 1, i = 0;
        while (num_of_blocks <= number_of_blocks)
        {
            if (num_of_blocks == 1)
            {
                index1[i] = index("test1.txt");
                i++;
            }
            if (num_of_blocks == 2)
            {
                index1[i] = index("test2.txt");
                i++;
            }
            if (num_of_blocks == 3)
            {
                index1[i] = index("test3.txt");
                i++;
            }
            if (num_of_blocks == 4)
            {
                index1[i] = index("test4.txt");
                i++;
            }
            if (num_of_blocks == 5)
            {
                index1[i] = index("test5.txt");
                i++;
            }
            if (num_of_blocks == 6)
            {
                index1[i] = index("test6.txt");
                i++;
            }
            if (num_of_blocks == 7)
            {
                index1[i] = index("test7.txt");
                i++;
            }
            if (num_of_blocks == 8)
            {
                index1[i] = index("test8.txt");
                i++;
            }
            if (num_of_blocks == 9)
            {
                index1[i] = index("test9.txt");
                i++;
            }
            if (num_of_blocks == 10)
            {
                index1[i] = index("test10.txt");
                i++;
            }
            if (num_of_blocks == 11)
            {
                index1[i] = index("test11.txt");
                i++;
            }
            if (num_of_blocks == 12)
            {
                index1[i] = index("test12.txt");
                i++;
            }
            if (num_of_blocks == 13)
            {
                index1[i] = index("test13.txt");
                i++;
            }
            if (num_of_blocks == 14)
            {
                index1[i] = index("test14.txt");
                i++;
            }
            if (num_of_blocks == 15)
            {
                index1[i] = index("test15.txt");
                i++;
            }
            if (num_of_blocks == 16)
            {
                index1[i] = index("test16.txt");
                i++;
            }
            if (num_of_blocks == 17)
            {
                index1[i] = index("test17.txt");
                i++;
            }
            if (num_of_blocks == 18)
            {
                index1[i] = index("test18.txt");
                i++;
            }
            if (num_of_blocks == 19)
            {
                index1[i] = index("test19.txt");
                i++;
            }
            if (num_of_blocks == 20)
            {
                index1[i] = index("test20.txt");
                i++;
            }
            if (num_of_blocks == 21)
            {
                index1[i] = index("test21.txt");
                i++;
            }
            if (num_of_blocks == 22)
            {
                index1[i] = index("test22.txt");
                i++;
            }
            if (num_of_blocks == 23)
            {
                index1[i] = index("test23.txt");
                i++;
            }
            if (num_of_blocks == 24)
            {
                index1[i] = index("test24.txt");
                i++;
            }
            if (num_of_blocks == 25)
            {
                index1[i] = index("test25.txt");
                i++;
            }
            if (num_of_blocks == 26)
            {
                index1[i] = index("test26.txt");
                i++;
            }
            if (num_of_blocks == 27)
            {
                index1[i] = index("test27.txt");
                i++;
            }
            if (num_of_blocks == 28)
            {
                index1[i] = index("test28.txt");
                i++;
            }
            if (num_of_blocks == 29)
            {
                index1[i] = index("test29.txt");
                i++;
            }
            if (num_of_blocks == 30)
            {
                index1[i] = index("test30.txt");
                i++;
            }
            num_of_blocks++;
        }
        double index = 0, sum = 0;

        for (int i = 0; i < number_of_blocks; i++)
        {
            sum += index1[i];
        }
        index = sum / number_of_blocks;
        std::cout << "к≥льк≥сть блок≥в: " << number_of_blocks << "≥ндекс- " << index << endl;

        in_file_blocks.seekg(0, std::ios::beg);
        in_file_blocks.close();
        ofstream out_file_block1("test1.txt");
        ofstream out_file_block2("test2.txt");
        ofstream out_file_block3("test3.txt");
        ofstream out_file_block4("test4.txt");
        ofstream out_file_block5("test5.txt");
        ofstream out_file_block6("test6.txt");
        ofstream out_file_block7("test7.txt");
        ofstream out_file_block8("test8.txt");
        ofstream out_file_block9("test9.txt");
        ofstream out_file_block10("test10.txt");
        ofstream out_file_block11("test11.txt");
        ofstream out_file_block12("test12.txt");
        ofstream out_file_block13("test13.txt");
        ofstream out_file_block14("test14.txt");
        ofstream out_file_block15("test15.txt");
        ofstream out_file_block16("test16.txt");
        ofstream out_file_block17("test17.txt");
        ofstream out_file_block18("test18.txt");
        ofstream out_file_block19("test19.txt");
        ofstream out_file_block20("test20.txt");
        ofstream out_file_block21("test21.txt");
        ofstream out_file_block22("test22.txt");
        ofstream out_file_block23("test23.txt");
        ofstream out_file_block24("test24.txt");
        ofstream out_file_block25("test25.txt");
        ofstream out_file_block26("test26.txt");
        ofstream out_file_block27("test27.txt");
        ofstream out_file_block28("test28.txt");
        ofstream out_file_block29("test29.txt");
        ofstream out_file_block30("test30.txt");
        out_file_block1.clear();
        out_file_block1.close();
        out_file_block2.clear();
        out_file_block2.close();
        out_file_block3.clear();
        out_file_block3.close();
        out_file_block4.clear();
        out_file_block4.close();
        out_file_block5.clear();
        out_file_block5.close();
        out_file_block6.clear();
        out_file_block6.close();
        out_file_block7.clear();
        out_file_block7.close();
        out_file_block8.clear();
        out_file_block8.close();
        out_file_block9.clear();
        out_file_block9.close();
        out_file_block10.clear();
        out_file_block10.close();
        out_file_block11.clear();
        out_file_block11.close();
        out_file_block12.clear();
        out_file_block12.close();
        out_file_block13.clear();
        out_file_block13.close();
        out_file_block14.clear();
        out_file_block14.close();
        out_file_block15.clear();
        out_file_block15.close();
        out_file_block16.clear();
        out_file_block16.close();
        out_file_block17.clear();
        out_file_block17.close();
        out_file_block18.clear();
        out_file_block18.close();
        out_file_block19.clear();
        out_file_block19.close();
        out_file_block20.clear();
        out_file_block20.close();
        out_file_block21.clear();
        out_file_block21.close();
        out_file_block22.clear();
        out_file_block22.close();
        out_file_block23.clear();
        out_file_block23.close();
        out_file_block24.clear();
        out_file_block24.close();
        out_file_block25.clear();
        out_file_block25.close();
        out_file_block26.clear();
        out_file_block26.close();
        out_file_block27.clear();
        out_file_block27.close();
        out_file_block28.clear();
        out_file_block28.close();
        out_file_block29.clear();
        out_file_block29.close();
        out_file_block30.clear();
        out_file_block30.close();
        number_of_blocks++;
    }
}

void key_blocks()
{
    int number_of_blocks = 20;

    ifstream in_file_blocks("test.txt");
    in_file_blocks.seekg(0, std::ios::beg);
    ofstream out_file_blocks1("test1.txt");
    out_file_blocks1.seekp(0, std::ios::beg);
    ofstream out_file_blocks2("test2.txt");
    out_file_blocks2.seekp(0, std::ios::beg);
    ofstream out_file_blocks3("test3.txt");
    out_file_blocks3.seekp(0, std::ios::beg);
    ofstream out_file_blocks4("test4.txt");
    out_file_blocks4.seekp(0, std::ios::beg);
    ofstream out_file_blocks5("test5.txt");
    out_file_blocks5.seekp(0, std::ios::beg);
    ofstream out_file_blocks6("test6.txt");
    out_file_blocks6.seekp(0, std::ios::beg);
    ofstream out_file_blocks7("test7.txt");
    out_file_blocks7.seekp(0, std::ios::beg);
    ofstream out_file_blocks8("test8.txt");
    out_file_blocks8.seekp(0, std::ios::beg);
    ofstream out_file_blocks9("test9.txt");
    out_file_blocks9.seekp(0, std::ios::beg);
    ofstream out_file_blocks10("test10.txt");
    out_file_blocks10.seekp(0, std::ios::beg);
    ofstream out_file_blocks11("test11.txt");
    out_file_blocks11.seekp(0, std::ios::beg);
    ofstream out_file_blocks12("test12.txt");
    out_file_blocks12.seekp(0, std::ios::beg);
    ofstream out_file_blocks13("test13.txt");
    out_file_blocks13.seekp(0, std::ios::beg);
    ofstream out_file_blocks14("test14.txt");
    out_file_blocks14.seekp(0, std::ios::beg);
    ofstream out_file_blocks15("test15.txt");
    out_file_blocks15.seekp(0, std::ios::beg);
    ofstream out_file_blocks16("test16.txt");
    out_file_blocks16.seekp(0, std::ios::beg);
    ofstream out_file_blocks17("test17.txt");
    out_file_blocks17.seekp(0, std::ios::beg);
    ofstream out_file_blocks18("test18.txt");
    out_file_blocks18.seekp(0, std::ios::beg);
    ofstream out_file_blocks19("test19.txt");
    out_file_blocks19.seekp(0, std::ios::beg);
    ofstream out_file_blocks20("test20.txt");
    out_file_blocks20.seekp(0, std::ios::beg);

    int number_of_leter = 0;

    while (!in_file_blocks.eof())
    {
        while (!in_file_blocks.eof())
        {
            symbol = in_file_blocks.get();
            number_of_leter++;

            if (symbol != '\n')
            {
                break;
            }
        }

        if (number_of_leter == 1)
        {
            out_file_blocks1 << symbol;
        }
        if (number_of_leter == 2)
        {
            out_file_blocks2 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 3)
        {
            out_file_blocks3 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 4)
        {
            out_file_blocks4 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 5)
        {
            out_file_blocks5 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 6)
        {
            out_file_blocks6 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 7)
        {
            out_file_blocks7 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 8)
        {
            out_file_blocks8 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 9)
        {
            out_file_blocks9 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 10)
        {
            out_file_blocks10 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 11)
        {
            out_file_blocks11 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 12)
        {
            out_file_blocks12 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 13)
        {
            out_file_blocks13 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 14)
        {
            out_file_blocks14 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 15)
        {
            out_file_blocks15 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 16)
        {
            out_file_blocks16 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 17)
        {
            out_file_blocks17 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 18)
        {
            out_file_blocks18 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 19)
        {
            out_file_blocks19 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
        if (number_of_leter == 20)
        {
            out_file_blocks20 << symbol;
            if (number_of_leter == number_of_blocks)
            {
                number_of_leter = 0;
            }
        }
    }

    out_file_blocks1.close();
    out_file_blocks2.close();
    out_file_blocks3.close();
    out_file_blocks4.close();
    out_file_blocks5.close();
    out_file_blocks6.close();
    out_file_blocks7.close();
    out_file_blocks8.close();
    out_file_blocks9.close();
    out_file_blocks10.close();
    out_file_blocks11.close();
    out_file_blocks12.close();
    out_file_blocks13.close();
    out_file_blocks14.close();
    out_file_blocks15.close();
    out_file_blocks16.close();
    out_file_blocks17.close();
    out_file_blocks18.close();
    out_file_blocks19.close();
    out_file_blocks20.close();
    in_file_blocks.close();


}

char populer_leter_in_block(string name_file)
{
    ifstream in(name_file);
    char symbol;
    map<char, int> container_symbols;

    char pop_symbol;
    int haw = 0;


    while (!in.eof())
    {
        while (!in.eof())
        {
            symbol = in.get();

            if (symbol != '\n')
            {
                break;
            }
        }

        if (symbol != '\n')
        {
            container_symbols[symbol] += 1;

        }
    }
    for (auto& member : container_symbols)
    {
        if (member.second > haw)
        {
            haw = member.second;
            pop_symbol = member.first;
        }
    }

    std::cout << "ѕопул€рна буква: " << pop_symbol << " зустр≥чаЇтьс€- " << haw << " раз≥в. " << endl;
    return pop_symbol;
}

void key(char b1, char b2, char b3, char b4, char b5, char b6, char b7, char b8, char b9, char b10, char b11, char b12, char b13, char b14,
    char b15, char b16, char b17, char b18, char b19, char b20)
{
    char key[20] = { b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20 };

    char pop_symbols[8] = { 'о','е','а','и','н','т','с','р' };

    int k;
    int ke;

    map<int, char> container_symbols = { {0, 'а'}, {1, 'б'}, {2, 'в'}, {3, 'г'},
    {4, 'д'}, {5, 'е'}, {6, 'ж'}, {7, 'з'}, {8, 'и'}, {9, 'й'}, {10, 'к'}, {11, 'л'},
    {12, 'м'}, {13, 'н'}, {14, 'о'}, {15, 'п'}, {16, 'р'}, {17, 'с'}, {18, 'т'}, {19, 'у'}, {20, 'ф'},
    {21, 'х'}, {22, 'ц'}, {23, 'ч'}, {24, 'ш'}, {25, 'щ'}, {26, 'ъ'}, {27, 'ы'}, {28, 'ь'}, {29, 'э'}, {30, 'ю'}, {31, '€'} };

    for (int i = 0; i < 8; i++)
    {
        for (auto& mem : container_symbols)
        {
            if (pop_symbols[i] == mem.second)
            {
                k = mem.first;
                std::cout << "Key:" << i << " ";
                for (int j = 0; j < 20; j++)
                {
                    for (auto& member : container_symbols)
                    {

                        if (key[j] == member.second)
                        {
                            ke = member.first - k;
                            while (ke < 0)
                            {
                                ke += 32;
                            }
                            ke %= 32;
                            std::cout << container_symbols[ke] << " ";
                            break;
                        }
                    }
                }
                std::cout << endl;
                break;
            }

        }
    }
}

void decoder(string key)
{
    map<int, char> container_symbols = { {0, 'а'}, {1, 'б'}, {2, 'в'}, {3, 'г'},
    {4, 'д'}, {5, 'е'}, {6, 'ж'}, {7, 'з'}, {8, 'и'}, {9, 'й'}, {10, 'к'}, {11, 'л'},
    {12, 'м'}, {13, 'н'}, {14, 'о'}, {15, 'п'}, {16, 'р'}, {17, 'с'}, {18, 'т'}, {19, 'у'}, {20, 'ф'},
    {21, 'х'}, {22, 'ц'}, {23, 'ч'}, {24, 'ш'}, {25, 'щ'}, {26, 'ъ'}, {27, 'ы'}, {28, 'ь'}, {29, 'э'}, {30, 'ю'}, {31, '€'} };

    ifstream in_file("test.txt");
    ofstream out_file("test_clean.txt");
    in_file.seekg(0, std::ios::beg);
    out_file.seekp(0, std::ios::beg);

    int j = 0, i = 0, r = 0;


    char key_char1[20];
    for (auto& m : key)
    {
        key_char1[r] = m;
        r++;
    }
    r = 0;

    while (!in_file.eof())
    {
        while (!in_file.eof())
        {
            symbol = in_file.get();

            if (symbol != '\n')
            {
                break;
            }
        }

        if (symbol != '\n')
        {
            for (auto& mem : container_symbols)
            {
                if (key_char1[r] == mem.second)
                {
                    i = mem.first;
                    for (auto& member : container_symbols)
                    {
                        if (symbol == member.second)
                        {
                            i = member.first-i;
                            while (i < 0)
                            {
                                i += 32;
                            }
                            i %= 32;
                            out_file << container_symbols[i];

                            break;
                        }
                    }
                    r++;
                    r %= 20;
                    break;
                }

            }
        }
    }

    in_file.close();
    out_file.close();

}

int main()
{
    double i;
    char b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20;
    setlocale(LC_CTYPE, "rus");


    /* cleaning();

     cipher(2, "на", "cipher_whit_key2.txt");

     cipher(3, "ток", "cipher_whit_key3.txt");

     cipher(4, "клок", "cipher_whit_key4.txt");

     cipher(5, "наст€", "cipher_whit_key5.txt");

     cipher(12, "криптографи€", "cipher_whit_key12.txt");

     std::cout << "≥ндекс дл€ ¬“: ";
     i = index("text_clean.txt");
     std::cout << i << endl;

     std::cout << "≥ндекс дл€ Ў“2: ";
     i = index("cipher_whit_key2.txt");
     std::cout << i << endl;

     std::cout << "≥ндекс дл€ Ў“3: ";
     i = index("cipher_whit_key3.txt");
     std::cout << i << endl;

     std::cout << "≥ндекс дл€ Ў“4: ";
     i = index("cipher_whit_key4.txt");
     std::cout << i << endl;

     std::cout << "≥ндекс дл€ Ў“5: ";
     i = index("cipher_whit_key5.txt");
     std::cout << i << endl;

     std::cout << "≥ндекс дл€ Ў“12: ";
     i = index("cipher_whit_key12.txt");
     std::cout << i << endl;


     breaking_into_blocks();

     key_blocks();

     b1 = populer_leter_in_block("test1.txt");
     b2 = populer_leter_in_block("test2.txt");
     b3 = populer_leter_in_block("test3.txt");
     b4 = populer_leter_in_block("test4.txt");
     b5 = populer_leter_in_block("test5.txt");
     b6 = populer_leter_in_block("test6.txt");
     b7 = populer_leter_in_block("test7.txt");
     b8 = populer_leter_in_block("test8.txt");
     b9 = populer_leter_in_block("test9.txt");
     b10 = populer_leter_in_block("test10.txt");
     b11 = populer_leter_in_block("test11.txt");
     b12 = populer_leter_in_block("test12.txt");
     b13 = populer_leter_in_block("test13.txt");
     b14 = populer_leter_in_block("test14.txt");
     b15 = populer_leter_in_block("test15.txt");
     b16 = populer_leter_in_block("test16.txt");
     b17 = populer_leter_in_block("test17.txt");
     b18 = populer_leter_in_block("test18.txt");
     b19 = populer_leter_in_block("test19.txt");
     b20 = populer_leter_in_block("test20.txt");

     key(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20);*/

    decoder("улановсеребр€ныепули");

    return 0;
}