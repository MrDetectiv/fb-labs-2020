#include <string>
#include <iostream>
#include <fstream>

using namespace std;

double h0_param_with_space = 0;
double h0_param_without_space = 0;


void cleaning()
{
    ifstream input("text.txt");
    ofstream output("text_clean.txt");
    ofstream out("text_clean1.txt");
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
           
                output << str << " ";
                n++;
                out << str;
            
        }
    }
    input.close();
    out.close();
    output.close();
}

#include <map>



void monograms(std::string name_file, bool with_space)
{
    ifstream in_file(name_file);


    map<char, int> container_symbols;

    long count_symbols = 0;
    char symbol;

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
            container_symbols[symbol] += 1;

            ++count_symbols;
        }
    }

    double h_param = 0;

    for (auto& member : container_symbols)
    {
        if (member.first != '\n')
        {
            double p_param = (double)member.second / (double)count_symbols;

            if (member.first == ' ')
            {
                cout << '"'<< ' '<<'"' << " Ц " /*<< member.second << " / " << count_symbols << " = "*/ << p_param << endl;
            }
            else
            {
                cout << '"' << member.first << '"' << " Ц " /*<< member.second << " / " << count_symbols << " = "*/ << p_param << endl;
            }

            h_param += p_param * log2(p_param);
        }
    }

    cout << "≈нтропи€ монограм: " << h_param * -1.0 << endl;

    if (with_space)
    {
        cout << "»збыточность: " << 1 - (h_param * -1.0) / h0_param_with_space << endl;
    }
    else
    {
        cout << "»збыточность: " << 1 - (h_param * -1.0) / h0_param_without_space << endl;
    }

    in_file.close();
}

void bigrams_intersecting(std::string name_file, bool with_space)

{
    ifstream in_file(name_file);

    char char_current = 0, char_last = 0;

    map<std::string, int> container_bigrams;

    long count_bigrams = 0;

    while (!in_file.eof())
    {
        while (!in_file.eof())
        {
            char_current = in_file.get();

            if (char_current != '\n')
            {
                break;
            }
        }

        if (char_last != 0 && char_current != '\n')
        {
            std::string word;

            word += char_last;
            word += char_current;

            container_bigrams[word] += 1;

            ++count_bigrams;
        }

        char_last = char_current;
    }

    double h_param = 0;

    for (auto& member : container_bigrams)
    {
        double p_param = (double)member.second / (double)count_bigrams;

        cout << '"' << member.first << '"' << " Ц "/* << member.second << " / " << count_bigrams << " = "*/ << p_param << endl;

        h_param += p_param * log2(p_param);
    }

    cout << "≈нтропи€ биграм с пересечением: " << (h_param * -1.0) / 2.0 << endl;

    if (with_space)
    {
        cout << "»збыточность: " << 1 - (h_param * -1.0) / h0_param_with_space / 2.0 << endl;
    }
    else
    {
        cout << "»збыточность: " << 1 - (h_param * -1.0) / h0_param_without_space / 2.0 << endl;
    }

    in_file.close();
}

void bigrams_not_intersecting(std::string name_file, bool with_space)
{
    ifstream in_file(name_file);

    char char1, char2;

    map<std::string, int> container_bigrams;

    long count_bigrams = 0;

    while (!in_file.eof())
    {
        while (!in_file.eof())
        {
            char1 = in_file.get();

            if (char1 != '\n')
            {
                break;
            }
        }

        while (!in_file.eof())
        {
            char2 = in_file.get();

            if (char2 != '\n')
            {
                break;
            }
        }

        if (char1 == '\n')
        {
            break;
        }

        if (char2 == '\n')
        {
            char2 = ' ';
        }

        std::string word;

        word += char1;
        word += char2;

        container_bigrams[word] += 1;
        ++count_bigrams;
    }

    double h_param = 0;

    for (auto& member : container_bigrams)
    {
        double p_param = (double)member.second / (double)count_bigrams;

        cout << '"' << member.first << '"' << " Ц " /*<< member.second << " / " << count_bigrams << " = " */<< p_param << endl;

        h_param += p_param * log2(p_param);
    }

    cout << "≈нтропи€ биграм без пересечени€: " << (h_param * -1.0) / 2.0 << endl;

    if (with_space)
    {
        cout << "»збыточность: " << 1 - (h_param * -1.0) / h0_param_with_space / 2.0 << endl;
    }
    else
    {
        cout << "»збыточность: " << 1 - (h_param * -1.0) / h0_param_without_space / 2.0 << endl;
    }

    in_file.close();
}




int main()
{
    setlocale(LC_CTYPE, "rus");

    h0_param_without_space = log2(33);
    h0_param_with_space = log2(34);

   cleaning();
    cout << "“аблица монограм с пробелом: " << endl << endl << endl;
    monograms("text_clean.txt", true);
    cout << endl << endl << endl << "“аблица монограм без пробелов : " << endl << endl << endl;
    monograms("text_clean1.txt", false);

    cout << endl << endl << endl << "“аблица биграм с пересечением и пробелами: " << endl << endl << endl;
    bigrams_intersecting("text_clean.txt", true);
    cout << endl << endl << endl << "“аблица биграм с пересечением без пробелов: " << endl << endl << endl;
    bigrams_intersecting("text_clean1.txt", false);

    cout << endl << endl << endl << "“аблица биграм без пересечени€ и с пробелами: " << endl << endl << endl;
    bigrams_not_intersecting("text_clean.txt", true);
    cout << endl << endl << endl << "“аблица биграм без пересечени€ и пробелов: " << endl << endl << endl;
    bigrams_not_intersecting("text_clean1.txt", false);




    return 0;
}