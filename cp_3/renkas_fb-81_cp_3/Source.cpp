#include <iostream>
#include <fstream>
#include <string>
#include <Windows.h>
#include <sstream>
#include <codecvt>
#include <locale>
#include <cmath>
#include <iomanip>
#include <limits>

using namespace std;
wstring rus_alphabet = L"абвгдежзийклмнопрстуфхцчшщьыэю€";
int most_encr[5] = { -1, -1, -1, -1, -1 };
int most_real[5] = { 545, 417, 572, 403, 168 };

wstring getting_full_text_in_one_string(wstring filename)
{
	wifstream input(filename);	// Open file
	input.imbue(locale(locale::empty(), new codecvt_utf8<wchar_t>)); // Set file codec to utf8
	wstringstream wss;			// Open stringstream
	wss << input.rdbuf();		// file to stringstream
	return wss.str();			// stringstream to string
}

wstring removing_endls(wstring text)
{
	int position = text.find(L"\n");
	while (position != string::npos)
	{
		text.replace(position, 1, L"");
		position = text.find(L"\n");
	}
	return(text);
}

int gcd(int a, int b)
{
	int q, r;
	while (b > 0)
	{
		q = a / b;
		r = a - q * b;
		a = b;
		b = r;
	}
	return a;
}

int find_inverse_element(int a, int mod)
{
	int x = mod;
	int y = 0, inversed = 1;
	int z, u;
	if (mod == 1)
		return 0;

	while (a > 1)
	{
		z = a / mod;
		u = mod;
		mod = a % mod;
		a = u;
		u = y;
		y = inversed - z * y;
		inversed = u;
	}
	if (inversed < 0)
		inversed += x;

	return inversed;
}


int find_letter_index(wchar_t letter)
{
	for (int i = 0; i < rus_alphabet.length(); i++)
	{
		if (letter == rus_alphabet[i])
		{
			return i;
		}
	}
	return 0;
}

void count_bigrams_and_frequencies_in_the_text(int **bigram_alphabet, wstring full_text, int step, string file_name)
{
	ofstream file(file_name + ".csv");
	int a = 0;
	int b = 0;
	double p;
	for (int i = 0; i < full_text.length() - step; i += step)
	{
		a = find_letter_index(full_text[i]);
		b = find_letter_index(full_text[i + 1]);
		bigram_alphabet[a][b]++;
	}
	for (int i = 0; i < 31; i++)
	{
		for (int j = 0; j < 31; j++)
		{
			p = (double)bigram_alphabet[i][j]; // full_text.length();
			file << fixed << setprecision(4) << p << ";";
		}
		file << "\n";
	}
	file << endl;
	file.close();
}

void count_letters_frequencies_in_the_text(int *letter_alphabet, wstring full_text)
{
	int a = 0;
	for (int i = 0; i < full_text.length(); i++)
	{
		a = find_letter_index(full_text[i]);
		letter_alphabet[a]++;
	}
}

void find_five_most_popular(int **bigram_alphabet)
{
	for (int a = 0; a < 5; a++)
	{
		int max = bigram_alphabet[0][0];
		int index = 0;
		for (int i = 0; i < 31; i++)
		{
			for (int j = 0; j < 31; j++)
			{
				if ((31 * i + j) == most_encr[0])
				{
					continue;
				}
				if ((31 * i + j) == most_encr[1])
				{
					continue;
				}
				if ((31 * i + j) == most_encr[2])
				{
					continue;
				}
				if ((31 * i + j) == most_encr[3])
				{
					continue;
				}
				if (max < bigram_alphabet[i][j])
				{
					max = bigram_alphabet[i][j];
					index = 31 * i + j;
				}
			}
		}
		if (most_encr[0] == -1) most_encr[0] = index;
		else if (most_encr[1] == -1) most_encr[1] = index;
		else if (most_encr[2] == -1) most_encr[2] = index;
		else if (most_encr[3] == -1) most_encr[3] = index;
		else most_encr[4] = index;
	}

}

wstring decryption(int a, int b, wstring text, int mod)
{
	//wcout << a << L"   " << b << L"   " << text.substr(0, 10) << "   " << mod << endl;
	int x;
	int y;
	wstring decrypted;
	a = find_inverse_element(a, mod);
	for (int i = 0; i < text.length(); i += 2)
	{
		y = find_letter_index(text[i]) * 31 + find_letter_index(text[i + 1]);
		x = a * (y - b);
		while (x < 0) x += mod;
		if (x > mod) x = x % mod;
		decrypted += rus_alphabet[x / 31];
		decrypted += rus_alphabet[x % 31];
	}
	return(decrypted);
}

int auto_recognizing_plaintext(wstring plaintext)
{
	int *letter_frequencies = new int[31];
	int len = plaintext.length();
	int min_value = len;
	int min_index;
	int max_value = -1;
	int max_index;
	for (int i = 0; i < 31; i++)
	{
		letter_frequencies[i] = 0;
	}

	count_letters_frequencies_in_the_text(letter_frequencies, plaintext);
	for (int i = 0; i < 31; i++)
	{
		if (min_value > letter_frequencies[i])
		{
			min_value = letter_frequencies[i];
			min_index = i;
		}
		if (max_value < letter_frequencies[i])
		{
			max_value = letter_frequencies[i];
			max_index = i;
		}
	}

	if ((double)letter_frequencies[find_letter_index(L'о')] / len < 0.08)
	{
		wcout << L"Filtering Failed: ";
		wcout << L"'о' frequency -> " << (double)letter_frequencies[find_letter_index(L'о')] * 100 / len << L" %\n" << endl;
		return 0;
	}
	else if ((double)letter_frequencies[find_letter_index(L'а')] / len < 0.07)
	{
		wcout << L"Filtering Failed: ";
		wcout << L"'а' frequency -> " << (double)letter_frequencies[find_letter_index(L'а')] * 100 / len << L" %\n" << endl;
		return 0;
	}
	else if ((double)letter_frequencies[find_letter_index(L'е')] / len < 0.06)
	{
		wcout << L"Filtering Failed: ";
		wcout << L"'е' frequency -> " << (double)letter_frequencies[find_letter_index(L'е')] * 100 / len << L" %\n" << endl;
		return 0;
	}
	else if ((double)letter_frequencies[find_letter_index(L'ф')] / len > 0.01)
	{
		wcout << L"Filtering Failed: ";
		wcout << L"'ф' frequency -> " << (double)letter_frequencies[find_letter_index(L'ф')] * 100 / len << L" %\n" << endl;
		return 0;
	}
	else if ((double)letter_frequencies[find_letter_index(L'щ')] / len > 0.01)
	{
		wcout << L"Filtering Failed: ";
		wcout << L"'щ' frequency -> " << (double)letter_frequencies[find_letter_index(L'щ')] * 100 / len << L" %\n" << endl;
		return 0;
	}
	else if ((double)letter_frequencies[find_letter_index(L'ь')] / len > 0.02)
	{
		wcout << L"Filtering Failed: ";
		wcout << L"'ь' frequency -> " << (double)letter_frequencies[find_letter_index(L'ь')] * 100 / len << L" %\n" << endl;
		return 0;
	}
	wcout << L"Filtering Success" << endl;
	return 1;
}

int *solution_of_linear_equations(int a, int b, int mod)
{
	int d;
	int a1, b1, n1, x0; //зм≥нн≥ з формули, об*Їднала пункти 1) ≥ 2.2) в один, бо вони один одного перекривають 
	int inversed;
	int *solutions;
	cout << "Solution of linear equation " << b << " = x * " << a << " mod(" << mod << ")\n";
	d = gcd(a, mod);
	if (d == 1)
	{
		cout << "Solved with 1 solution!" << endl;
		solutions = new int[2];
		inversed = find_inverse_element(a, mod);
		solutions[0] = (b * inversed) % mod;
		solutions[1] = -1;
	}
	else if (d > 1 && b % d != 0)
	{
		cout << "Unsolved. 0 solutions found" << endl << endl;
		solutions = new int[1];
		solutions[0] = -1;
		return(solutions);
	}
	else
	{
		cout << "Solved with " << d << " solutions" << endl;
		solutions = new int[d + 1];
		a1 = a / d;
		b1 = b / d;
		n1 = mod / d;
		inversed = find_inverse_element(a1, n1);
		x0 = (b1 * inversed) % n1;
		for (int i = 0; i < d; i++)
		{
			solutions[i] = x0 + n1 * i;
		}
		solutions[d] = -1;
	}

	return(solutions);
}

void data_for_solution_of_linear_equations(int mod, wstring text)
{
	int *solutions;
	int a, b, X, Y, x1, x2;
	int y1 = most_encr[0];
	int y2 = most_encr[1];
	wstring real_text;
	for (int i = 0; i < 5; i++)
	{
		x1 = most_real[i];
		for (int j = 0; j < 5; j++)
		{
			if (i == j) continue;
			x2 = most_real[j];
			Y = y1 - y2;
			if (Y < 0) Y += mod;
			X = x1 - x2;
			if (X < 0) X += mod;
			solutions = solution_of_linear_equations(X, Y, mod);
			int index = 0;
			while (solutions[index] != -1)
			{
				a = solutions[index];
				if (a < 0) continue;
				else b = (y1 - a * x1);
				while (b < 0) b += mod;
				real_text = decryption(a, b, text, mod);
				cout << "Trying Key: (" << a << ", " << b << ")" << endl;
				if (auto_recognizing_plaintext(real_text) == 1)
				{
					cout << "Decrypted:" << endl;
					wcout << real_text << endl;
					return;
				}
				index++;
			}
		}
	}
}

int main()
{
	setlocale(LC_ALL, "ukr");
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	wstring encrypted_text;
	encrypted_text = getting_full_text_in_one_string(L"D:\\16.txt");
	encrypted_text = removing_endls(encrypted_text);

	int x = 0;

	int **bigram_alphabet = new int*[31];
	for (int i = 0; i < 31; i++)
	{
		bigram_alphabet[i] = new int[31];
		for (int j = 0; j < 31; j++)
		{
			bigram_alphabet[i][j] = 0;
		}
	}
	count_bigrams_and_frequencies_in_the_text(bigram_alphabet, encrypted_text, 2, "bigram's_frequencies");
	find_five_most_popular(bigram_alphabet);
	for (int i = 0; i < 5; i++)
	{
		cout << most_encr[i] << "  ";
	}
	cout << endl << endl;
	data_for_solution_of_linear_equations(31 * 31, encrypted_text);

	cout << "End Of Program" << endl;
	system("pause");
	return 0;
}
