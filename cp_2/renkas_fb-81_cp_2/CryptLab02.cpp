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
wstring rus_alphabet = L"абвгдежзийклмнопрстуфхцчшщъыьэю€";

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
		int index = full_text[i] - L'ј';
		//using whitelist
		if (full_text[i] == L'®' || full_text[i] == L'Є')
			norm_text += L'Є';
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
	if (letter == L'Є')
		return(32);
	else if (letter == L' ')
		return(33);
	else
	{
		return(letter - L'а');
	}
}

int getting_letter_index(wchar_t s)
{
	for (int i = 0; i < rus_alphabet.length(); i++)
	{
		if (s == rus_alphabet[i])
		{
			return i;
		}
	}
	return 0;
}


wstring text_encryption(wstring my_text, wstring R, int a)
{
	wstring result;
	int j = 0;
	int c = 0;
	int sum = 0;
	for (int i = 0; i < my_text.length(); i++)
	{
		if (j > a - 1)
		{
			j = 0;
		}
		c = getting_letter_index(my_text[i]);
		sum = c;
		c = getting_letter_index(R[j]);
		sum += c;
		if (sum > 31)
			sum = sum - 31;
		result += rus_alphabet[sum];
		j++;
	}
	return result;
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

double calculating_correspondence_index(wstring text, double n)
{
	double I = 0;
	double N = 0;
	int *alphabet = new int[32];
	for (int i = 0; i < 32; i++)
	{
		alphabet[i] = 0;
	}
	count_letters_in_the_text(alphabet, text);
	for (int j = 0; j < 32; j++)
	{
		N = (double)alphabet[j] * ((double)alphabet[j] - 1);
		I += N;
	}
	return(I*(1 / (n * (n - 1))));
}

double correspondence_index_for_blocks(wstring text, int step)
{
	wstring block;
	double I;
	double max = 0;
	for (int i = 0; i < step; i++)
	{
		for (int j = i; j < text.length(); j += step)
		{
			block += text[j];
		}
		I = calculating_correspondence_index(block, block.length());
		if (max < I)
		{
			max = I;
		}
		cout << "Index for block with period  " << step << " : " << I << endl;
		block = L"";
	}
	cout << endl;
	return(max);
}

void find_key(wstring text, int step)
{
	wstring block;
	int m = 0;
	int index = 0;
	wstring key_variants[5];
	for (int i = 0; i < step; i++)
	{
		for (int j = i; j < text.length(); j += step)
		{
			block += text[j];
		}
		int *alphabet = new int[32];
		for (int i = 0; i < 32; i++)
		{
			alphabet[i] = 0;
		}
		count_letters_in_the_text(alphabet, block);
		for (int a = 0; a < 32; a++)
		{
			if (m < alphabet[a])
			{
				m = alphabet[a];
				index = a;
			}
		}
		m = (index - 14);
		if (m < 0) m += 32;
		key_variants[0] += rus_alphabet[m];
		key_variants[1] += rus_alphabet[index];
		m = (index - 5);
		if (m < 0) m += 32;
		key_variants[2] += rus_alphabet[m];
		m = (index - 8);
		if (m < 0) m += 32;
		key_variants[3] += rus_alphabet[m];
		m = (index - 13);
		if (m < 0) m += 32;
		key_variants[4] += rus_alphabet[m];
		cout << endl;
		cout << "block:  " << i + 1 << "  most popular letter index:  " << index << endl;
		wcout << rus_alphabet[index] << " ";
		block = L"";
		index = 0;
		m = 0;
	}
	wcout << endl << key_variants[0];
	wcout << endl << key_variants[1];
	wcout << endl << key_variants[2];
	wcout << endl << key_variants[3];
	wcout << endl << key_variants[4] << endl;
}
void frequencies(wstring text, int step, wstring key)
{
	wstring block;
	int m = 0;
	int index = 0;
	double diff = 0;
	for (int i = 0; i < step; i++)
	{
		for (int j = i; j < text.length(); j += step)
		{
			block += text[j];
		}
		int *alphabet = new int[32];
		for (int i = 0; i < 32; i++)
		{
			alphabet[i] = 0;
		}
		count_letters_in_the_text(alphabet, block);
		for (int a = 0; a < 32; a++)
		{
			if (m < alphabet[a])
			{
				m = alphabet[a];
				index = a;
			}
		}
		diff = index - find_letter_index(key[i]);
		if (diff < 0) diff += 32;
		if (diff != 14)
		{
			cout << "frequencies for block: " << i + 1 << endl;
			for (int b = 0; b < 32; b++)
			{
				cout << (((double)alphabet[b]) / block.length()) << "  ";
			}
			cout << endl << endl;
		}
		block = L"";
		index = 0;
		m = 0;
	}
}

void decryption(wstring text, wstring key)
{
	wstring result;
	int j = 0;
	int c = 0;
	int sum = 0;
	for (int i = 0; i < text.length(); i++)
	{
		if (j > key.length() - 1)
		{
			j = 0;
		}
		c = getting_letter_index(text[i]);
		sum = c;
		c = getting_letter_index(key[j]);
		sum -= c;
		if (sum < 0) sum += 32;
		result += rus_alphabet[sum];
		j++;
	}
	wcout << endl << result << endl;
}

int main()
{
	setlocale(LC_ALL, "ukr");
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);

	wstring my_text;
	wstring R = L"неудачливыевизитеры"; //назва од≥Їњ з глав
	wstring encrypted_text;
	wstring variant_text;
	double correspondence_index;
	double I_max = 0;
	int key_len;

	my_text = getting_full_text_in_one_string(L"D:\\my_text.txt");
	my_text = normalization_of_string(my_text);
	my_text = removing_spaces_from_text(my_text);
	variant_text = getting_full_text_in_one_string(L"D:\\variant_text.txt");
	variant_text = normalization_of_string(variant_text);
	variant_text = removing_spaces_from_text(variant_text);
	//јЅ¬√ƒ≈∆«»… ЋћЌќѕ–—“”‘’÷„ЎўЏџ№Ёёя

	correspondence_index = calculating_correspondence_index(my_text, my_text.length());
	cout << "original_text" << "  " << correspondence_index << endl;

	encrypted_text = text_encryption(my_text, R, 2);
	correspondence_index = calculating_correspondence_index(encrypted_text, encrypted_text.length());
	cout << "encrypted_text_key_2" << "  " << correspondence_index << endl;

	encrypted_text = text_encryption(my_text, R, 3);
	correspondence_index = calculating_correspondence_index(encrypted_text, encrypted_text.length());
	cout << "encrypted_text_key_3" << "  " << correspondence_index << endl;

	encrypted_text = text_encryption(my_text, R, 4);
	correspondence_index = calculating_correspondence_index(encrypted_text, encrypted_text.length());
	cout << "encrypted_text_key_4" << "  " << correspondence_index << endl;

	encrypted_text = text_encryption(my_text, R, 5);
	correspondence_index = calculating_correspondence_index(encrypted_text, encrypted_text.length());
	cout << "encrypted_text_key_5" << "  " << correspondence_index << endl;

	encrypted_text = text_encryption(my_text, R, 19);
	correspondence_index = calculating_correspondence_index(encrypted_text, encrypted_text.length());
	cout << "encrypted_text_key_full" << "  " << correspondence_index << endl;

	cout << "counting CI for variant text" << endl;
	for (int i = 2; i < 31; i++)
	{
		double max = correspondence_index_for_blocks(variant_text, i);
		if (max > I_max)
		{
			I_max = max;
			key_len = i;
		}

	}
	cout << key_len << endl;

	find_key(variant_text, key_len);
	frequencies(variant_text, key_len, L"башн€€ростичерныемаки");
	decryption(variant_text, L"башн€€ростичерныемаки");

	cout << "End Of Program" << endl;
	system("pause");
	return 0;
}
