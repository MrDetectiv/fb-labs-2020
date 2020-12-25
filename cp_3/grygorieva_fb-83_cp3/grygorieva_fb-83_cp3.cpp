#include <iostream>
#include <fstream>
#include <istream>
#include<cstdlib>
#include <map>
#include <vector>
#include <set>

using namespace std;

class Letter
{
public:
    int ascii_code;
    float times_in_text;
    char symbol;
    int number_in_alphabet;
};

Letter* frequency_for_each_letter = new Letter[31];
int q = 1;
int choice;
vector<vector<int> > key_array_for_test(q, vector<int>(2));
char* buffer;
char* buf;
int length;
int len;
int* open_text_bigrams = new int [5];
int* encrtypted_text_bigrams = new int[5];
std::ofstream file;

void find_most_frequent_bigrams(string path);
void decrypt_into_file(int a, int b, string path);
void comparation_solution(int a, int a1, int b, int b1);
int gcd(int a, int b);
int reverse(int a, int n);
int check_decrytped_text();
int extended_Euclids_algorithm(int a, int b, int* u, int* v, int* d);

int main()
{
    setlocale(LC_ALL, "");

    cin >> choice;
    if (choice == 1)
        find_most_frequent_bigrams("C:\\crypto\\for-test-var7.txt");
    if (choice == 2)
        find_most_frequent_bigrams("C:\\crypto\\07.txt");
    find_most_frequent_bigrams("C:\\crypto\\master-i-margarita_1.txt");
    

    cout << "OPEN TEXT BIGRAMS LOOK LIKE THIS IN Xi FORM: ";
    for (int i = 0; i < 5; i++)
    {
        cout << open_text_bigrams[i] << " ";
    }

    if (choice == 1)
        cout << endl << "ENCRYPTED TEXT BIGRAMS FROM TEST LOOK LIKE THIS IN Yi FORM: ";
    if (choice == 2)
        cout << endl << "ENCRYPTED TEXT BIGRAMS FROM VAR7 LOOK LIKE THIS IN Yi FORM: ";
    for (int i = 0; i < 5; i++)
    {
        cout << encrtypted_text_bigrams[i] << " ";
    }

    if (choice == 1)
        cout  << endl << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TEST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;
    if (choice == 2)
        cout << endl << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ VAR 7 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;
    for (int m = 0; m < 5; m++)
    {
        for (int n = 0; n < 5; n++)
        {
            for (int j = 0; j < 5; j++)
            {
                for (int i = 0; i < 5; i++)
                {
                    if (encrtypted_text_bigrams[i] - encrtypted_text_bigrams[j] != 0 && open_text_bigrams[n] - open_text_bigrams[m] != 0)
                    {
                        //cout << "CALCULATING THIS: " << encrtypted_text_bigrams[i] << "-" << encrtypted_text_bigrams[j] << " = a * " << open_text_bigrams[n] << "-" << open_text_bigrams[m] << " mod961" << endl;
                        comparation_solution(open_text_bigrams[n], open_text_bigrams[m], encrtypted_text_bigrams[i], encrtypted_text_bigrams[j]);
                    }
                }
            }
        }
    }

    //comparation_solution(54, 0, 3, 0);
    //comparation_solution(93, 0, 31, 0);

    int p = 1;
    vector<vector<int> > unique_key_array(p, vector<int>(2));

    set< set<int> > unique_keys;
    for (int i = 0; i < q - 1; i++)
    {
        set<int>row;
        for (int j = 0; j < 2; j++)
        {
            row.insert(key_array_for_test[i][0]);
            row.insert(key_array_for_test[i][1]);
        }
        unique_keys.insert(row);
    }

    int check = 0;

    for (auto const& s : unique_keys)
    {
        for (auto const& i : s)
        {
            if (check == 0)
            {
                unique_key_array.push_back(vector<int>(2));
                unique_key_array[p - 1][0] = i;
                check = 1;
            }
            else if (check == 1)
            {
                unique_key_array[p - 1][1] = i;
                p++;
                check = 0;
            }
        }
    }

    for (int i = 0; i < p- 1; i++)
    {
        cout << "(";
        for (int j = 0; j < 2; j++)
        {
            if (j == 0) cout << unique_key_array[i][j] << ", ";
            if (j == 1) cout << unique_key_array[i][j];
        }
        cout << ")  ";
    }

    cout << endl << "FOUND " << p << " KEYS" << endl;
   
    if (choice == 1)
        file.open("C:\\crypto\\test_result.txt");
    if (choice == 2)
        file.open("C:\\crypto\\var7_result.txt");
    for (int i = 0; i < p-1; i++)
    {
        int temp_A = unique_key_array[i][0];
        int temp_B = unique_key_array[i][1];
        if (choice == 1)
            decrypt_into_file(temp_A, temp_B, "C:\\crypto\\for-test-var7.txt");
        if (choice == 2)
            decrypt_into_file(temp_A, temp_B, "C:\\crypto\\07.txt");
    }

    //decrypt_into_file(35, 219, "C:\\crypto\\for-test-var7.txt");
    //decrypt_into_file(200, 900, "C:\\crypto\\07.txt");
    file.close();
    return 0;
}

int gcd(int a, int b) 
{
    if (a == b) 
    {
        return a;
    }
    if (a > b) 
    {
        int temp = a;
        a = b;
        b = temp;
    }
    return gcd(a, b - a);
}

int reverse(int a, int n)
{
    int d, reverse_a, y;
    extended_Euclids_algorithm(a, n, &reverse_a, &y, &d);
    //cout << a << " reversed is " << reverse_a << endl;
    if (d == 1) return reverse_a;
    return 0;
}

int extended_Euclids_algorithm(int a, int n, int* u, int* v, int* d)
{
    int q, r, u1, u2, v1, v2;

    if (n == 0) {
        *d = a, * u = 1, * v = 0;
        return -1;
    }
    u2 = 1, u1 = 0, v2 = 0, v1 = 1;

    while (n > 0) {
        q = a / n, r = a - q * n;
        *u = u2 - q * u1, * v = v2 - q * v1;
        a = n, n = r;
        u2 = u1, u1 = *u, v2 = v1, v1 = *v;
    }
    *d = a, * u = u2, * v = v2;
    return a;
}

void comparation_solution(int a, int a1, int b, int b1)
{
    int n = 961;
    int a_temp = a; 
    int b_temp = b;
    //cout << a << " " << b << endl;
    //cout << a1 << " " << b1 << endl;

    a = a - a1;
    b = b - b1;
    if (a < 0 && b > 0) a = 961 - abs(a);
    if (b < 0 && a < 0) { b = abs(b); a = abs(a); }

    //cout << "SOLVING: " << a << "*x = " << b << "mod" << n << endl;

    int d = gcd(a, n);
    //cout << d << endl;
    int x, y;

    if (d == 1)
    {
        x = ( reverse(a, n)  * b ) % n;
        if (x < 0) x = n - abs(x);
        //cout << "FOUND KEY:  ("<< x << ", ";
        y = (b_temp - x * a_temp) % n;
        if (y < 0) y = 961 - abs(y);
        //cout << y << ")" <<endl;
        
        int found = 0;
        if (gcd(x, n) == 1)
        {
            for (int i = 0; i < q - 1; i++)
            {
                if (key_array_for_test[i][0] == x && key_array_for_test[i][1] == y)
                    found = 1;
            }
            if (found == 0)
            {
                key_array_for_test.push_back(vector<int>(2));
                key_array_for_test[q - 1][0] = x;
                key_array_for_test[q - 1][1] = y;
                q++;
            }
            found = 0;
        }
    }

    if (d > 1)
    {
        if (b % d != 0)
        {
            //cout << "ERROR, NO SOLUTIONS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" << endl;
        }
        else
        {
            //cout << "COMPARATION HAS MULTIPLE SOLUTIONS!--------------------------------------------------------------------------" << endl;
            //cout << d << " SOLUTIONS: " << endl;
            a = a / d;
            b = b / d;
            n = n / d;
            x = (reverse(a, n) * b) % n;
            if (x < 0) x = n - abs(x);
            //cout << x << endl;

            int found = 0;
            for (int i = 0; i < d; i++)
            {
                if (gcd(x + i * d, n) == 1)
                {
                    for (int i = 0; i < q - 1; i++)
                    {
                         if(((b_temp - (x + i * d) * a_temp) % (n*n)) < 0)
                         {
                             if (key_array_for_test[i][0] == x + i * d && key_array_for_test[i][1] == n * n - abs((b_temp - (x + i * d) * a_temp) % (n * n)))
                                 found = 1;
                         }
                         else
                         {
                             if (key_array_for_test[i][0] == x + i * d && key_array_for_test[i][1] == (b_temp - (x + i * d) * a_temp) % (n * n))
                                 found = 1;
                         }
                    }
                    if (found == 0)
                    {
                        key_array_for_test.push_back(vector<int>(2));
                        key_array_for_test[q - 1][0] = x + i * d;
                        key_array_for_test[q - 1][1] = (b_temp - (x + i * d) * a_temp) % (n*n);
                        if (key_array_for_test[q - 1][1] < 0) key_array_for_test[q - 1][1] = n*n - abs(key_array_for_test[q - 1][1]);
                        //cout << key_array_for_test[q - 1][1] << endl;
                        q++;
                    }
                }
                //cout << "FOUND KEY:  (" << key_array_for_test[q - 1][0] << ", ";
                //cout << key_array_for_test[q - 1][1] << ")" <<endl;
            }
            found = 0;
        }
    }
    //cout << endl;
}

void find_most_frequent_bigrams(string path)
{
    cout << "FREQUENCIES FOR FILE " << path << endl;
    float number_of_bigrams = 0;
    map <string, float> bigram_and_times_in_text;
    std::ifstream file;
    file.open(path);
    if (file)
    {
        file.seekg(0, file.end);

        length = file.tellg();
        file.seekg(0, file.beg);
        buffer = new char[length];

        file.read(buffer, length);
    }

    bigram_and_times_in_text = { { "",0 } };
    map <string, float> ::iterator it;
    it = bigram_and_times_in_text.begin();

    string temp_str = "";
    int j = 0;

    for (int i = 0; i < length; i = i + 2)
    {
        temp_str = buffer[i];
        temp_str = temp_str + buffer[i + 1];
        if (bigram_and_times_in_text.find(temp_str) != bigram_and_times_in_text.end())
        {
            bigram_and_times_in_text[temp_str]++;
            number_of_bigrams++;
        }

        else
        {
            bigram_and_times_in_text[temp_str] = 1;
            number_of_bigrams++;
            if (j < 1088) j++;
        }
    }

    map<float, string> reverse_bigram_and_times_in_text;
    for (pair<string, float> pair : bigram_and_times_in_text)
    {
        reverse_bigram_and_times_in_text[pair.second] = pair.first;
    }

    map<float, string>::reverse_iterator r_it = reverse_bigram_and_times_in_text.rbegin();

    int counter = 1;
    
    int n = 31;
    int temp1 = 0;
    int temp2 = 0;
    
    while (r_it != reverse_bigram_and_times_in_text.rend() && counter < 6)
    {
        cout << r_it->first / number_of_bigrams << " -> " << r_it->second << endl;
        temp1 = (int)r_it->second[0] + 32;
        temp2 = (int)r_it->second[1] + 32;
        if (temp1 >= 27) temp1 = temp1 - 1;
        if (temp2 >= 27) temp2 = temp2 - 1;
        if (path == "C:\\crypto\\master-i-margarita_1.txt") open_text_bigrams[counter-1] = temp1 * n + temp2;
        if (path == "C:\\crypto\\for-test-var7.txt") encrtypted_text_bigrams[counter - 1] = temp1 * n + temp2;
        if (path == "C:\\crypto\\07.txt") encrtypted_text_bigrams[counter - 1] = temp1 * n + temp2;
        r_it++;
        counter++;
    }

    //bigram_and_times_in_text.clear();
    //reverse_bigram_and_times_in_text.clear();
    file.close();
}

void decrypt_into_file(int a, int b, string path)
{
    cout << "KEY IS  (" << a << ", " << b << ")";
    std::ifstream file1;
    file1.open(path);
    if (file1)
    {
        file1.seekg(0, file1.end);

        length = file1.tellg();
        file1.seekg(0, file1.beg);
        buffer = new char[length];

        file1.read(buffer, length);
    }
    else cout << "ERROR_1" << endl;

    int n = 31;
    int encrypted_bigram = 0;
    int open_bigram = 0;
    int x1, x2;
    char x_1, x_2;

    std::ofstream file_temp;
    file_temp.open("C:\\crypto\\temp.txt");
    for (int i = 0; i < length; i = i + 2)
    {
        if ((int)buffer[i] + 32 < 26)
        {
            encrypted_bigram = ((int)buffer[i] + 32) * n;
            if ((int)buffer[i + 1] + 32 < 26)
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 32);
            else if ((int)buffer[i + 1] + 32 == 28 || ((int)buffer[i + 1] + 32 == 27))
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 32);
            else
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 31);
        }

        if ((int)buffer[i] + 32 == 28)
        {
            encrypted_bigram = 26 * n;
            if ((int)buffer[i + 1] + 32 < 26)
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 32);
            else if ((int)buffer[i + 1] + 32 == 27 || ((int)buffer[i + 1] + 32 == 28))
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 31);
            else
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 31);
        }

        if ((int)buffer[i] + 32 == 27)
        {
            encrypted_bigram = 27 * n;
            if ((int)buffer[i + 1] + 32 < 26)
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 32);
            else if ((int)buffer[i + 1] + 32 == 27 || ((int)buffer[i + 1] + 32 == 28))
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 31);
            else
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 31);
        }

        if ((int)buffer[i] + 32 > 28)
        {
            encrypted_bigram = ((int)buffer[i] + 31) * n;
            if ((int)buffer[i + 1] + 32 < 26)
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 32);
            else if ((int)buffer[i + 1] + 32 == 28 || ((int)buffer[i + 1] + 32 == 27))
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 32);
            else
                encrypted_bigram = encrypted_bigram + ((int)buffer[i + 1] + 31);
        }

        //cout << encrypted_bigram << " ";
        open_bigram = (reverse(a, 961) * (encrypted_bigram - b)) % 961;
        if (open_bigram < 0) open_bigram = 961 - abs(open_bigram);
        //cout << open_bigram << " ";

        x1 = open_bigram / 31;
        x2 = open_bigram % 31;

        if (path == "C:\\crypto\\07.txt")
        {
            if (x1 == 26) x1 = 27;
            else if (x1 == 27) x1 = 26;
            else;
            if (x2 == 26) x2 = 27;
            else if (x2 == 27) x2 = 26;
            else;
        }

        if (x1 >= 26) x1 = x1 - 31;
        else x1 = x1 - 32;
        if (x2 >= 26) x2 = x2 - 31;
        else x2 = x2 - 32;
        
        x_1 = (char)x1;
        x_2 = (char)x2;
        file_temp << x_1 << x_2;

        //cout << x_1 << " " << x_2 << endl;
    } 
    file_temp.close();

    if (check_decrytped_text() == 1)
    {
        std::ifstream file2;
        file2.open("C:\\crypto\\temp.txt");
        if (file2)
        {
            file2.seekg(0, file2.end);

            len = file2.tellg();
            file2.seekg(0, file2.beg);
            buf = new char[len];

            file2.read(buf, len);
        }
        else cout << "ERROR_1" << endl;

        for (int i = 0; i < len; i++)
        {
            file << buf[i];
        }
        file2.close();
    }
    file << endl << endl;
    file1.close();
}

int check_decrytped_text()
{
    int value = 0;
    float coincidence_index = 0;
    int n = -32;
    for (int j = 0; j < 26; j++)
    {
        frequency_for_each_letter[j].ascii_code = n;
        frequency_for_each_letter[j].symbol = (char)n;
        frequency_for_each_letter[j].times_in_text = 0;
        frequency_for_each_letter[j].number_in_alphabet = j;
        n++;
    }

        frequency_for_each_letter[26].ascii_code = -5;
        frequency_for_each_letter[26].symbol = 'ы';
        frequency_for_each_letter[26].times_in_text = 0;
        frequency_for_each_letter[26].number_in_alphabet = 26;

        frequency_for_each_letter[27].ascii_code = -4;
        frequency_for_each_letter[27].symbol = 'ь';
        frequency_for_each_letter[27].times_in_text = 0;
        frequency_for_each_letter[27].number_in_alphabet = 27;

        frequency_for_each_letter[28].ascii_code = -3;
        frequency_for_each_letter[28].symbol = 'э';
        frequency_for_each_letter[28].times_in_text = 0;
        frequency_for_each_letter[28].number_in_alphabet = 28;

        frequency_for_each_letter[29].ascii_code = -2;
        frequency_for_each_letter[29].symbol = 'ю';
        frequency_for_each_letter[29].times_in_text = 0;
        frequency_for_each_letter[29].number_in_alphabet = 29;

        frequency_for_each_letter[30].ascii_code = -1;
        frequency_for_each_letter[30].symbol = 'я';
        frequency_for_each_letter[30].times_in_text = 0;
        frequency_for_each_letter[30].number_in_alphabet = 30;

    std::ifstream file2;
    file2.open("C:\\crypto\\temp.txt");
    if (file2)
    {
        file2.seekg(0, file2.end);

        len = file2.tellg();
        file2.seekg(0, file2.beg);
        buf = new char[len];

        file2.read(buf, len);
        int temp = 0;

        for (int m = 0; m < len; m++)
        {
            temp = (int)buf[m];

            for (int j = -32; j < 0; j++)
            {
                if (temp == j)
                {
                    frequency_for_each_letter[j + 32].times_in_text++;
                }
            }
        }

    }
    else cout << "ERROR_1" << endl;

    float text_length;
    if(choice == 1)
        text_length = 5080;
    if (choice == 2)
        text_length = 7102;

    for (int j = 0; j < 31; j++)
    {
        coincidence_index = coincidence_index + (frequency_for_each_letter[j].times_in_text) * (frequency_for_each_letter[j].times_in_text - 1);
    }

    float koef = text_length * text_length - text_length;
    koef = 1 / koef;
    coincidence_index = koef * coincidence_index;
    if (coincidence_index < 0.05)
    {
        value = 0;
        cout << " COINCEDENCE INDEX = " << coincidence_index << " SO ... NO" << endl;
    }
    else
    {
        value = 1;
        cout << " COINCEDENCE INDEX = " << coincidence_index << " SO ................................................. YES!" << endl;
    }

    file2.close();
    return value;
}