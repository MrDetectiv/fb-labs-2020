#include "func.h"

int main()
{
	setlocale(LC_CTYPE, "rus");
	SetConsoleOutputCP(1251);
	SetConsoleCP(1251);

	string encoded = readfile(fin, "D:\\cryptolab3\\var.txt");

	cleanup(encoded);

	vector<int> encnum = text_to_num(encoded);

	cout << encnum.size() << endl;

	vector<pair<int, int>> keys = evalkey(encoded);


	vector<int> decnum = decode(encnum, keys.at(0));
	string dec = num_to_text(decnum);

	writefile(dec, fout, "var_decoded.txt");


	system("pause");
	return 0;

}