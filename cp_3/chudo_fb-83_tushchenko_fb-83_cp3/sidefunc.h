#include "Header.h"

//void cout_map(map<string, float>& mp)
//{
//	for (map <string, float> ::iterator it = mp.begin(); it != mp.end(); it++)
//	{
//		cout <<  it->first << "    " << it->second << endl;
//	}
//}

//modulus count
int mod(int a, int b)
{
	return (a % b + b) % b;
}

// text to int conversion and vice versa
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


////frequencies
 //letters
//bigrams
void ngramm_freq_nocoverup(string& str, map <string, float>& mp, int n)
{
	string tmpstr;
	int i = 0;
	while (i < str.length() && i + n != str.length() - 1)
	{

		tmpstr = str.substr(i, n);
		mp[tmpstr] ++;
		tmpstr.clear();
		i += n;
	}

}

map<string, float> perc_freq(int length, map<string, float>& mp, bool nocover)
{
	map<string, float> map_fr;
	if (nocover == true)
	{
		length = length / 2;
	}
	else
	{
		length -= 1;
	}
	for (map<string, float>::const_iterator it = mp.begin(); it != mp.end(); ++it)
	{
		map_fr.insert({ it->first, (it->second / length) });
	}

	return map_fr;
}

//5 bigrams

string getmax(map<string, float>& mp)
{
	int m = 0;
	string maxkey;
	for (map<string, float>::iterator it = mp.begin(); it != mp.end(); it++)
	{
		if (it->second > m)
		{
			m = it->second;
			maxkey = it->first;
		}
	}

	return maxkey;
}

//map<float, string> most_freq_bigr(string& text)
//{
//	vector<string> bigr;
//	map<string, float> freq;
//	ngramm_freq_nocoverup(text, freq, 2);
//	//freq = perc_freq(text.length(), freq1, true); 
//
//	//map is sorted by keys
//	//so to get it sorted by values create reversed map where revmp.first = mp.second
//	//map requires unique kay values we will use multimap as it permits multiple entries with the same key
//
//	multimap<float, string> rev_freq;
//
//	for (map<string, float>::iterator it = freq.begin(); it != freq.end(); it++)
//	{
//		rev_freq.insert({ it->second, it->first });
//	}
//
//	//for (int i = 0; i < 5; i++)
//	//{
//	//	multimap<float, string>::iterator it = rev_freq.begin();
//	//	it += i;
//	//	string val = it->second;
//	//	bigr.push_back(val);
//	//}
//	/*for (auto& it : rev_freq)
//	{
//		bigr.push_back(it.second);
//	}*/
//
//
//	map<float, string> top5;
//		
//	for (int i=0; i < 5; i++)
//		{
//		multimap<float, string>::iterator it = rev_freq.begin();
//			cout << it->first << " " << it->second;
//			top5.insert({ it->first, it->second });
//			rev_freq.erase(it);
//			
//		}
//
//
//	return top5;
//}

map<string, float> most_freq_bigr(string& text)
{
	map<string, float> bigr;
	map<string, float> freq;
	ngramm_freq_nocoverup(text, freq, 2);
	//freq = perc_freq(text.length(), freq1, true); 
	string maxkey;



	for (int i = 0; i < 5; i++)
	{
		maxkey = getmax(freq);
		//cout << maxkey << " " << freq[maxkey] << endl;

		bigr.insert({ maxkey, freq[maxkey] });
		freq.erase(maxkey);
	}


	return bigr;
}



pair<int, int> makekey(int a, int b)
{
	return make_pair(a, b);
}

//eea

pair<int, int> eea(int a, int b)
{
	pair<int, int> res; //gcd, inv

	vector<int> Rvalues;
	Rvalues.push_back(a);
	Rvalues.push_back(b);

	vector<int> Uvalues;
	Uvalues.push_back(1);
	Uvalues.push_back(0);

	vector<int> Vvalues;
	Vvalues.push_back(0);
	Vvalues.push_back(1);

	bool flag = false;

	int r, q, u, v;

	for (int i = 2; !flag; i++)
	{

		r = Rvalues.at(i - 2) % Rvalues.at(i - 1);

		if (r == 0)
		{
			flag = true;
			break;
		}

		q = Rvalues.at(i - 2) / Rvalues.at(i - 1);

		u = Uvalues.at(i - 2) - q * Uvalues.at(i - 1);

		v = Vvalues.at(i - 2) - q * Vvalues.at(i - 1);

		Uvalues.push_back(u);
		Vvalues.push_back(v);
		Rvalues.push_back(r);

	}

	r = Rvalues.back();
	u = Uvalues.back();

	res = make_pair(r, u);

	return res;
}

int gcd(int a, int m)
{
	pair<int, int> ee = eea(a, m);
	return ee.first;
}

//Inverse Modulo
int inverse_mod(int a, int m)
{
	pair <int, int> ee; //gcd, inv
	ee = eea(a, m);

		if (ee.first != 1)
		{
			cout << a << "^-1  (mod " << m << ")  doesn`t exist" << endl;
			return 0;
		}

		else
		{
			return mod(ee.second, m);
		}

}


void writefile(string& text, ofstream& fout, string path)
{
	fout.open(path, fstream::app);
	if (!fout.fail())
	{
		fout << text;
	}
	fout.close();
}

string readfile(ifstream& fin, string path)
{
	string r;
	fin.open(path);
	//check for file open failure
	if (fin.fail())
	{
		cout << "Error opening input file" << endl;
		fin.close();
		system("PAUSE");

	}
	else
	{
		cout << "Input file is opened successfully" << endl;
	}

	//reading file
	getline(fin, r, '\0');
	cout << "file reading is completed" << endl;

	//close input stream
	fin.close();

	return r;
}




void cleanup(string& str)
//{
//
//	for (int i = 0; i < str.length(); i++)
//	{
//
//		//	//replace ¸
//		if (str.at(i) == '¸' || str.at(i) == '¨') { str.at(i) = 'å'; }
//
//
//		//set to lowercase
//		if (str.at(i) >= -64 && str.at(i) <= -33)
//		{
//			str.at(i) += 32;
//		}
//
//		//	//cleanup all non-letter symbols but spaces
//		if (!(str.at(i) >= -32 && str.at(i) <= -1))
//		{
//			str.at(i) = 127;
//		}
//
//	}
//
//
//
//	str.erase(std::remove(str.begin(), str.end(), 127), str.end());
//
{
	replace(str.begin(), str.end(), '\n', ' ');

	str.erase(remove_if(str.begin(), str.end(), isspace), str.end());
	cout << "cleaning done" << endl;

}