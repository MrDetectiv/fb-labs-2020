#include "Header.h"

int mod(int a, int b) // eto ne ya velosiped pridumala, ono ne schitalo <0
{
	return (a % b + b) % b;
}

void cout_vector(vector<int>& vect)
{
	for (int i = 0; i < vect.size(); i++)
	{
		cout << vect.at(i) << " ";
	}
	cout << endl;
}

void cout_vector(vector<double>& vect)
{
	for (int i = 0; i < vect.size(); i++)
	{
		cout << vect.at(i) << " ";
	}
	cout << endl;
}

void cout_vector(vector<vector<int>> vect)
{
	for (int i = 0; i < vect.size(); i++)
	{
		cout << "[" << i << "] ";
		cout_vector(vect.at(i));

	}
}

void cout_map(map<int, double>& mp)
{
	for (map <int, double> ::iterator it = mp.begin(); it != mp.end(); it++)
{
		cout << "r = " << it->first << " index = " << it->second << endl;
}
}
////////////////////////////////////////////////////////////////////

void cleanup(string& str)
{

	for (int i = 0; i < str.length(); i++)
	{

	//	//replace ё
		if (str.at(i) == 'ё' || str.at(i) == 'Ё') { str.at(i) = 'е'; }


		//set to lowercase
		if (str.at(i) >= -64 && str.at(i) <= -33)
		{
			str.at(i) += 32;
		}

		//	//cleanup all non-letter symbols but spaces
	if (!(str.at(i) >= -32 && str.at(i) <= -1))
	{
		str.at(i) = 127;
	}

	}



	str.erase(std::remove(str.begin(), str.end(), 127), str.end());


	replace(str.begin(), str.end(), '\n', ' ');
	//erase double spaces
	//size_t ds = str.find("  ");
	//while (ds != std::string::npos)
	//{
	//	str.erase(ds, 1);
	//	ds = str.find("  ");
	//}
	//str.erase(remove_if(str.begin(), str.end(), isspace), str.end());
	cout << "cleaning done" << endl;

}
//////////////////////////////////////////////////////////////////////

vector<int> text_to_num(string& text)
{
	string tmp;
	vector<int> numtext(text.length(), 0);

	for (int i = 0; i < text.length(); i++)
	{
		tmp = text.substr(i, 1);
		numtext.at(i) = AlphNum[tmp];
		tmp.clear();

	}
	return numtext;
}

string num_to_text(vector<int>& numtext)
{
	string text;
	for (int i = 0; i < numtext.size(); i++)
	{
		text += NumAlph[numtext.at(i)];
	}
	return text;
}

//inline string key_string(string& key, int text_length)
//{
//	string keystr;
//	for (int i = 0; i < text_length; i++)
//	{
//		keystr += key.at(i%key.length());
//	}
//
//	return keystr;
//}

 /////////////////////////////////////////////////////////////////////
string encode(string& text, string key)
{
	vector<int> encoded(text.length(), 0);
	vector<int> keynum = text_to_num(key);
	vector<int> textnum = text_to_num(text);
	for (int i = 0; i < textnum.size(); i++)
	{
		encoded.at(i) = (textnum.at(i) + keynum.at(i % (keynum.size())))%alpha_size;
	}

	string encodedstr = num_to_text(encoded);

	return encodedstr;
}

 string decode(string& encoded, string& key)
 {
	 vector<int> decoded(encoded.length(), 0);
	 vector<int> keynum = text_to_num(key);
	 vector<int> textnum = text_to_num(encoded);
	 for (int i = 0; i < textnum.size(); i++)
	 {
//		 cout << textnum.at(i) << " - " << keynum.at(i % (keynum.size())) << " = " << mod(textnum.at(i) - keynum.at(i % (keynum.size())), 32) << endl;
		 decoded.at(i) = mod(textnum.at(i)-keynum.at(i % (keynum.size())), alpha_size);
	 }

	 string decodedstr = num_to_text(decoded);

	 return decodedstr;

 }
 /////////////////////////////////////////////////////////////////////

 vector<int> count_freq(string& text)
 {
	 vector<int> freq(alpha_size, 0); // vect index == number of letter

		 string tmpstr;
		 int let_num;

		 for (int i = 0; i < text.length(); i++)
		 {

			 tmpstr = text.substr(i, 1); //get character from string
			 let_num = AlphNum[tmpstr]; // get number of character
			 freq.at(let_num) += 1; // add to freq
			 tmpstr.clear();

		 }

		 return freq;
 }

 vector<int> count_freq(vector<int> &textnum)
 {
	 vector<int> freq(alpha_size, 0); // vect index == number of letter


	 for (int i = 0; i < textnum.size(); i++)
	 {
		 /*
		 textnum.at(i) is letter number
		 freq index indicates letter number
		 so we take letter number from textnum and add +1 to freq at this index
		 */
		freq.at(textnum.at(i)) += 1; 
			 }

	 return freq;
 }


////////////////////////////////////////////////////////////////////////


 double conformity_index(string text)
 {
	 vector<int> textnum = text_to_num(text);
	 vector<int> freq = count_freq(text);

	 double n = text.length();
	 double index = 0.0;
	 double N;

	 for (int i = 0; i < alpha_size; i++)
	 {
		 N = freq.at(i);
		 index += N * (N - 1);
	 }

	 index /= (n * (n - 1));

	 return index;
 }

 double confirmity_index(vector<int> &textnum)
 {
	 //string text = num_to_text(textnum);
	 vector<int> freq = count_freq(textnum);
	 double n = textnum.size();
	 double index = 0.0;
	 double N;

	 for (int i = 0; i < alpha_size; i++)
	 {
		 N = freq.at(i);
		 index += N * (N - 1);
	 }

	 index /= (n * (n - 1));

	 return index;
 }
 /////////////////////////////////////////////////////////////////////////
 vector<vector<int>> group_blocks(vector<int> textnum, int r)
 {
	 vector<vector<int>> blocks;
//	 vector<int> textnum = text_to_num(text);
	 vector<int> current;

	 for (int i = 0; i < r && i < textnum.size(); i++)
	 {
		 for (int j = i; j < textnum.size(); j += r)
		 {
			 current.push_back(textnum.at(j));
		}
		 blocks.push_back(current);
		 current.clear();
	 }
	 return blocks;
 }

 vector<double> blocks_confirmity(vector<vector<int>>& blocks)
 {
	 int r = blocks.size();
	 vector<double> index;
	 vector<int> current;

	 for (int i = 0; i < r; i++)
	 {
		 current = blocks.at(i);
		 index.push_back(confirmity_index(current));
		 current.clear();
	 }
	 return index;
 }
 /////////////////////////////////////////////////////////////////////////

 double get_max(vector<double>& vect)
 {
	 double max = 0;
	 for (int i = 0; i < vect.size(); i++)
	 {
		 if (vect.at(i) > max)
		 {
			 max = vect.at(i);
		 }
	 }

	 return max;
 }

 map<int, double> get_max(map<int, double>& mp)
 {
	 map<int, double> max;
	 for (map <int, double> ::iterator it = mp.begin(); it != mp.end(); it++)
	 {
		 map <int, double> ::reverse_iterator itmx = max.rbegin();
		 if (max.empty()||it->second > itmx->second)
		 {
			 max[it->first] = it->second;
		 }
	}
	 return max;
 }

 string eval_key_letter_with_o(vector<int>& block, vector<int>& freq)
 {
	 string key_letter;

	 int max = 0;
	 int max_index = 0;

	 for (int i = 0; i < freq.size(); i++)
	 {
		 if (freq.at(i) > max)
		 {
			 max = freq.at(i);
			 max_index = i;
		 }
	 }

	 int key_let = mod(max_index - AlphNum["о"], alpha_size);
	 key_letter += NumAlph[key_let];

	 return key_letter;
 }
 /////////////////////////////////////////////////////////////////////////////
int eval_r (vector<int>& textnum, int max_r=5)
 {
	map<int, double> max_of_r;
	int guessed;

	 for (int r = 2; r <= max_r; r++)
	 {
		// cout << "r = " << r << endl;
		 vector<vector<int>> blocks = group_blocks(textnum, r);
		 vector<double> conf = blocks_confirmity(blocks);
		 max_of_r[r] = get_max(conf);
		// cout_vector(conf);
	 }
	 //cout << "All indexes for r:" << endl;
	 //cout_map(max_of_r);
	 cout << "-----------------------------------------" << endl;
	 cout << "MAx indexes: "<< endl;
	 map<int, double> maxes = get_max(max_of_r);
	 cout_map(maxes);
	 cout << "enter key length:		";
	 cin >> guessed;
	 cout << endl;

	 return guessed;
 }

string crack_key(vector<int> &textnum, int key_length)
{
	string key;
	vector<vector<int>> blocks = group_blocks(textnum, key_length);
	vector<vector<int>> freq;
	for (int i = 0; i < blocks.size(); i++)
	{
		freq.push_back(count_freq(blocks.at(i)));
	}

	//vector<int> current;
	for (int i = 0; i < blocks.size(); i++)
	{
		key += eval_key_letter_with_o(blocks.at(i), freq.at(i));
	}

//	cout << "Cracked key:	" << key << endl;
//	cout << "Frequencies" << endl;
//	cout_vector(freq);


	return key;
}


void task2 (string& enc, ofstream &fout)

{
	vector<string> keys;
	keys.push_back("еж");   
	keys.push_back("кот");
	keys.push_back("мост");
	keys.push_back("аминь");
	keys.push_back("аристократизм");

	vector<string> tofile;
	vector<double> index;

	for (int i = 0; i < keys.size(); i++)
	{
		string key = keys.at(i);
		string encd = encode(enc, key);
		double ind = conformity_index(encd);
		tofile.push_back(encd);
		index.push_back(ind);
	}

		fout.open("encoded_my.txt");
	{//	fout.open("encoded_my.txt");
	if (!fout.fail())
	{
		for (int i = 0; i < keys.size(); i++)
		{
			fout << tofile.at(i) << endl << endl;
			fout << index.at(i) << endl << endl;
		}
	}
	fout.close(); }



}


void task3(string& encr, ofstream &fout)
{
vector<int> encr_num = text_to_num(encr);

	int keylength = eval_r(encr_num, 30);

	string crackedkey = crack_key(encr_num, keylength);

	cout << "Cracked key:	"<< crackedkey << endl;
	cout << "Wanna edit cracked key?  0/1" << endl;
	int answ;
	cin >> answ;
	string variantdecoded;

	if (answ == 1)
	{
		string mykey;
		cout << "Enter edited key:	";
		cin.ignore();
		getline(cin, mykey);	
		variantdecoded = decode(encr, mykey);
	}
	else {
		variantdecoded = decode(encr, crackedkey);
	}

	{	fout.open("variantdecode_result.txt");
	if (!fout.fail())
	{
		fout << variantdecoded;
	}
	fout.close(); 
	}
}





/*
 //int kronecker(vector<int>& textnum, int r)
 //{
	// int delta = 0;
	// for (int i = 0; i < textnum.size()-1; i++)
	// {
	//	 for (int j = i; j < textnum.size() - 1; j + r)
	//	 {
	//		 if (textnum.at(i) == textnum.at(j))
	//		 {
	//			 delta += 1;
	//		 }
	//	 }
	// }
	// return delta;
 //}

 //int max_Kronecker(vector<int> &textnum, int max_r)
 //{
	// int max=0;
	// int max_delta_r=0;
	// int r = 1;

	// for (r; r <= max_r && r <= textnum.size(); r++)
	// {
	//	 vector<vector<int>> blocks = group_blocks(textnum, r);
	//	 for (int i = 0; i < r; i++)
	//	 {
	//		 cout << "blocks.at(" << i << ")" << endl;
	//		 cout_vector(blocks.at(i));
	//		 cout << "r = " << r << " delta = " << kronecker(blocks.at(i), 1) << endl;
	//		 if (kronecker(blocks.at(i), 1) > max)
	//		 {
	//			 max = kronecker(blocks.at(i), 1);
	//			 max_delta_r = r;
	//			 cout << "for r = " << r << "max_delta = " << max << endl;
	//		}
	//	 }
	// }
	// cout << "Max Kronecker value is for r = " << max_delta_r << "is " << max;
	// return max_delta_r;
 //}

*/