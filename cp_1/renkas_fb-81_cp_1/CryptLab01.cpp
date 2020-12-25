#include <iostream>
#include <fstream>
#include <string>
#include <Windows.h>
#include <sstream>
#include <codecvt>
#include <locale>
#include <cmath>
#include <iomanip>

using namespace std;

wstring getting_full_text_in_one_string(wstring filename)
{
	wifstream input(filename);	// Open file
	input.imbue(locale(locale::empty(), new codecvt_utf8<wchar_t>)); // Set file codec to utf8
	wstringstream wss;			// Open stringstream
	wss << input.rdbuf();		// file to stringstream
	return wss.str();			// stringstream to string
}


wstring normalization_of_string(wstring full_text)
{
	wstring norm_text;
	for (int i = 0; i < full_text.length(); i++)
	{
		int index = full_text[i] - L'À';
		//using whitelist
		if (full_text[i] == L'¨' || full_text[i] == L'¸')
			norm_text += L'¸';
		else if (full_text[i] == L' ' || full_text[i] == L'\n')
			norm_text += L' ';
		else if (index < 64 && index >= 0)
		{
			if (index < 32)
			{
				full_text[i] += 32;
			}
			norm_text += full_text[i];
		}
	}
	//delete extra spaces
	int position = norm_text.find(L"  ");
	while (position != string::npos)
	{
		norm_text.replace(position, 2, L" ");
		position = norm_text.find(L"  ");
	}
	return(norm_text);
}

wstring removing_spaces_from_text(wstring full_text)
{
	wstring bufer = full_text;
	int position = bufer.find(L" ");
	while (position != string::npos)
	{
		bufer.replace(position, 1, L"");
		position = bufer.find(L" ");
	}
	return(bufer);
}

int find_letter_index(wchar_t letter)
{
	if (letter == L'¸')
		return(32);
	else if (letter == L' ')
		return(33);
	else
	{
		return(letter - L'à');
	}
}

void count_letters_in_the_text(int *alphabet, wstring full_text)
{
	int j = 0;
	for (int i = 0; i < full_text.length(); i++)
	{
		j = find_letter_index(full_text[i]);
		alphabet[j]++;
	}
}

double calculating_H1(int *alphabet, int length, int spaces)
{
	double a = 0;
	double p;
	cout << "Probability of each letter" << endl;
	wcout << L"à\tá\tâ\tã\tä\tå\tæ\tç\tè\té\tê" << endl;
	for (int i = 0; i < 33 + spaces; i++)
	{
		p = (double)alphabet[i] / length;
		cout << fixed << setprecision(4) << p << "\t";
		if (i == 10)
		{
			wcout << endl << L"ë\tì\tí\tî\tï\tð\tñ\tò\tó\tô\tõ" << endl;
		}
		if (i == 21)
		{
			wcout << endl << L"ö\t÷\tø\tù\tú\tû\tü\tý\tþ\tÿ\t¸\t-" << endl;
		}
		if (p != 0)
		{
			a += (p*log2(p));
		}
	}
	cout << endl;
	return(a * (-1));
}

void count_bigrams_in_the_text(int **bigram_alphabet, wstring full_text, int step)
{
	int a = 0;
	int b = 0;
	for (int i = 0; i < full_text.length() - step; i += step)
	{
		a = find_letter_index(full_text[i]);
		b = find_letter_index(full_text[i + 1]);
		bigram_alphabet[a][b]++;
	}
}

double calculating_H2(int **bigram_alphabet, int length, int spaces, string file_name)
{
	ofstream file(file_name + ".csv");
	double a = 0;
	double p;
	wchar_t first = L'à';
	for (int i = 0; i < 33 + spaces; i++)
	{
		for (int j = 0; j < 33 + spaces; j++)
		{
			p = (double)bigram_alphabet[i][j] / length;
			file << fixed << setprecision(4) << p << ";";
			if (p != 0)
			{
				a += (p*log2(p));
			}
		}
		file << "\n";
		if (first == L'ÿ')
		{
			first = L'¸';
		}
		else if (first == L'¸')
		{
			first = L'_';
		}
		else first++;
	}
	file << endl;
	file.close();
	return((a * (-1))/2);
}

double calculating_redundancy_of_the_language(double H, int m)
{
	double R;
	R = 1 - (H / (log2(m)));
	return R;
}

int main()
{
	setlocale(LC_ALL, "ukr");
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);

	int length_with_spaces;
	int length_without_spaces;
	double H;
	wstring full_text;
	wstring full_text_without_spaces;

	wstring file_name = L"D:\\mazter_and_margarita.txt";

	cout << "Reading text...  ";
	full_text = getting_full_text_in_one_string(file_name);
	cout << "done" << endl << "Normalization of the text in process...   ";
	full_text = normalization_of_string(full_text);
	cout << "done" << endl << "Creating new string with text and removing all spaces....";
	full_text_without_spaces = removing_spaces_from_text(full_text);
	cout << "done" << endl;
	length_with_spaces = full_text.length();
	length_without_spaces = full_text_without_spaces.length();
	//àáâãäåæçèéêëìíîïðñòóôõö÷øù´ºü³þÿ¿
	int *alphabet = new int[34];
	for (int i = 0; i < 34; i++)
	{
		alphabet[i] = 0;
	}

	cout << "Counting amount of each letter of the alphabet...";
	count_letters_in_the_text(alphabet, full_text);
	cout << "done " << endl << "Calculating H1 and redundency..." << endl;
	H = calculating_H1(alphabet, length_with_spaces, 1);
	cout << "Using text with spaces: H1 = " << H << endl;
	cout << "Redundency: " << calculating_redundancy_of_the_language(H, 34) << endl;
	H = calculating_H1(alphabet, length_without_spaces, 0);
	cout << "Using text without spaces: H1 = " << H << endl;
	cout << "Redundency: " << calculating_redundancy_of_the_language(H, 33) << endl;
	cout << endl << "All caclulations for H1 done" << endl;

	int **bigram_alphabet = new int*[34];
	for (int i = 0; i < 34; i++)
	{
		bigram_alphabet[i] = new int[34];
		for (int j = 0; j < 34; j++)
		{
			bigram_alphabet[i][j] = 0;
		}
	}
	
	cout << "Counting amount of bigrams of the alphabet in text with spaces...";
	count_bigrams_in_the_text(bigram_alphabet, full_text, 1);
	cout << "done " << endl << "Calculating H2 and redundency..." << endl;
	H = calculating_H2(bigram_alphabet, length_with_spaces - 1, 1, "with spaces and intersections");
	cout << "Using text with spaces and intersections: H2 = " << H << endl;
	cout << "Redundency: " << calculating_redundancy_of_the_language(H, 34) << endl;

	for (int i = 0; i < 34; i++)
	{
		for (int j = 0; j < 34; j++)
		{
			bigram_alphabet[i][j] = 0;
		}
	}
	cout << "Counting amount of bigrams of the alphabet in text without spaces..." << endl;
	count_bigrams_in_the_text(bigram_alphabet, full_text_without_spaces, 1);
	H = calculating_H2(bigram_alphabet, length_without_spaces - 1, 0, "with intersections and without spaces");
	cout << "Using text with intersections and without spaces: H2 = " << H << endl;
	cout << "Redundency: " << calculating_redundancy_of_the_language(H, 33) << endl;
	cout << endl << "All caclulations for H2 done" << endl;

	for (int i = 0; i < 34; i++)
	{
		for (int j = 0; j < 34; j++)
		{
			bigram_alphabet[i][j] = 0;
		}
	}

	cout << "Counting amount of bigrams of the alphabet in text without spaces..." << endl;
	count_bigrams_in_the_text(bigram_alphabet, full_text, 2);
	cout << "done " << endl << "Calculating H2 and redundency..." << endl;
	H = calculating_H2(bigram_alphabet, (length_with_spaces) / 2, 1, "with spaces and without intersections");
	cout << "Using text with spaces and without intersections: H2 = " << H << endl;
	cout << "Redundency: " << calculating_redundancy_of_the_language(H, 34) << endl;

	for (int i = 0; i < 34; i++)
	{
		for (int j = 0; j < 34; j++)
		{
			bigram_alphabet[i][j] = 0;
		}
	}
	cout << "Counting amount of bigrams of the alphabet in text without spaces..."  << endl;
	count_bigrams_in_the_text(bigram_alphabet, full_text_without_spaces, 2);
	H = calculating_H2(bigram_alphabet, (length_without_spaces) / 2, 0, "without intersections and spaces");
	cout << "Using text without intersections and spaces: H2 = " << H << endl;
	cout << "Redundency: " << calculating_redundancy_of_the_language(H, 33) << endl;
	cout << endl << "All caclulations for H2 done" << endl;
	wcout << endl << "End of Program" << endl;
	system("pause");
	return 0;
}
