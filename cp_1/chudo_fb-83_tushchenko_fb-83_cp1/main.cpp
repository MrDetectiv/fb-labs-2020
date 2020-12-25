#include "func.h"


int main()
{
	setlocale(LC_CTYPE, "rus");
	SetConsoleOutputCP(1251);
	SetConsoleCP(1251);
	
	//in-out streams
	ofstream fout;
	ifstream fin;

	//string to read into
	string txt;
	string txt_nospace;

	//creating map with letters/bigrams and their frequeces
	map<string, float> Letters;
	map<string, float> Bigrams;
	map<string, float> Bigrams_nocover;

	//enthropy map
	map<string, float> Enthropy;









	//opening input file
	fin.open(PATH_IN);
	
	//check for file open failure
	if (fin.fail())
	{
		cout << "Error opening input file" << endl;
		fin.close();
		system("PAUSE");
		return -1;
	}
	else
	{
		cout << "Input file is opened successfully" << endl;
	}

	//reading file
	getline(fin, txt, '\0');
	cout << "file reading is completed" << endl;
	
	//close input stream
	fin.close();







	//cleaning the string
	clean_string(txt);

	txt_nospace = txt;
	erase_spaces(txt_nospace);


	//fout.open("D:\\cryptolab1\\crypto_clean.txt");
	//fout << txt;
	//fout.close();








	/*------------------------------------------------------------------------*/

	//						get freq of letter
	//						with spaces
	ngramm_freq(txt, Letters, 1);
	cout << "letter frequency counted" << endl;

	ngramm_freq(txt, Bigrams, 2);
	cout << "bigram frequency counted" << endl;

	ngramm_freq_nocoverup(txt, Bigrams_nocover, 2);
	cout << "no cover bigram frequency counted" << endl;







	//						get freq of letter in per cents
	//						with spaces

	map<string, float> Let_Freq = perc_freq(txt.length(), Letters, false);
	cout << "letter frequency % counted" << endl;

	map<string, float> Bi_Freq = perc_freq(txt.length(), Bigrams, false);
	cout << "bigram frequency % counted" << endl;

	map<string, float> Bi_Freq_nocover = perc_freq(txt.length(), Bigrams_nocover, true);
	cout << "no cover bigram frequency % counted" << endl;






	//						output map to file
fout.open(PATH_WS);
if (fout.fail())
{
	cout << "Error opening output file" << endl;
}
else
	{
	fout_map(fout, Let_Freq);
	fout << endl << endl;
	fout_map(fout, Bi_Freq);
	fout << endl << endl << "no cover" << endl;
	fout_map(fout, Bi_Freq_nocover);

	//						close output stream
	fout.close();
	cout << "file output completed" << endl;
	}




Enthropy["H1ws"] = enthropy_calc(Let_Freq, 1);
Enthropy["H2ws"] = enthropy_calc(Bi_Freq, 2);
Enthropy["H2nc"] = enthropy_calc(Bi_Freq_nocover, 2);






	/*--------------------------------------------------------------------------*/
//							erase for nospace
Letters.erase(" ");
Bigrams.clear();
Bigrams_nocover.clear();
Let_Freq.clear();
Bi_Freq.clear();
Bi_Freq_nocover.clear();

//cout << "cleared maps" << endl;





ngramm_freq(txt_nospace, Bigrams, 2);
cout << "nospace bigram frequency counted" << endl;

	ngramm_freq_nocoverup(txt_nospace, Bigrams_nocover, 2);
	cout << "nospace nocover bigram frequency counted" << endl;



Let_Freq = perc_freq(txt_nospace.length(), Letters, false);
cout << "nospace letter frequency % counted" << endl;

Bi_Freq = perc_freq(txt_nospace.length(), Bigrams, false);
cout << "nospace bigram frequency % counted" << endl;

Bi_Freq_nocover = perc_freq(txt_nospace.length(), Bigrams_nocover, true);
	cout << "nospace nocover bigram frequency % counted" << endl;





	//					output map to file
fout.open(PATH_NS);

if (fout.fail())
{
	cout << "Error opening output file" << endl;
}

else
{
	fout_map(fout, Let_Freq);
	fout << endl << endl;

	fout_map(fout, Bi_Freq);
		fout << endl << endl << "no cover" << endl;

		fout_map(fout, Bi_Freq_nocover);

		//close output stream
	fout.close();
	cout << "file output completed" << endl;
}


//calc enthropy and insert to map
Enthropy["H1ns"] = enthropy_calc(Let_Freq, 1);
Enthropy["H2ns"] = enthropy_calc(Bi_Freq, 2);
Enthropy["H2ncns"] = enthropy_calc(Bi_Freq_nocover, 2);



// fout enthropy
fout.open(PATH_ENT);
if (fout.fail())
{
	cout << "Error opening output file" << endl;
}
else
{
	fout_map(fout, Enthropy);


		//close output stream
	fout.close();
	cout << "file output completed" << endl;
}

	system("PAUSE");
	return 0;
}

