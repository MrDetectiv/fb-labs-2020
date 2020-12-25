#include "func.h"


int main()
{
	setlocale(LC_CTYPE, "rus");
	SetConsoleOutputCP(1251);
	SetConsoleCP(1251);

	//in-out streams

	ifstream fin;
	ofstream fout;

	//string to read file, path, key	
	string text, path/*, key*/;


	path = "encode.txt";

	//read file
	{	fin.open(BASE_DIR + path);

	//check for file open failure
	if (fin.fail())
	{
		std::cout << "Error opening input file" << endl;
		fin.close();
		return -1;
	}
	else
	{
		std::cout << "Input file is opened successfully" << endl;
	}

	getline(fin, text, '\0');
	std::cout << "file reading is completed" << endl;

	//close input stream
	fin.close();
	}
	//clean text string
	cleanup(text);
	task2(text, fout);


	string decode;
	path = "decode.txt";
	//read file
	{	fin.open(BASE_DIR + path);

	//check for file open failure
	if (fin.fail())
	{
		std::cout << "Error opening input file" << endl;
		fin.close();
		return -1;
	}
	else
	{
		std::cout << "Input file is opened successfully" << endl;
	}

	getline(fin, decode, '\0');
	std::cout << "file reading is completed" << endl;

	//close input stream
	fin.close();
	}

	cleanup(decode);
	task3(decode, fout);


	system("PAUSE");
	return 0;
}