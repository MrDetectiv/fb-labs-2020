#include "Header.h"

//some cleanup
void clean_string(string &str)
{


	for (int i = 0; i < str.length(); i++)
	{

		//cleanup all non-letter symbols but spaces
		if ((str.at(i) > 32 && str.at(i) < 65) || (str.at(i) > 90 && str.at(i) < 97) || (str.at(i) > 127 && str.at(i) < 255) /*|| str.at(i) == char("—")*/)
		{
			str.at(i) = 127;
		}
		


		//replace ú, ¸
		if (str.at(i) == 'ú') { str.at(i) = 'ü'; }
		if (str.at(i) == '¸' || str.at(i) == '¨') { str.at(i) = 'å'; }


		//set to lowercase

		{		// ya znayu chto reshenie ne samoe elegantnoe no zato rabochee
			if (str.at(i) == 'À') { str.at(i) = 'à'; }
			if (str.at(i) == 'Á') { str.at(i) = 'á'; }
			if (str.at(i) == 'Â') { str.at(i) = 'â'; }
			if (str.at(i) == 'Ã') { str.at(i) = 'ã'; }
			if (str.at(i) == 'Ä') { str.at(i) = 'ä'; }
			if (str.at(i) == 'Å') { str.at(i) = 'å'; }
			if (str.at(i) == 'Æ') { str.at(i) = 'æ'; }
			if (str.at(i) == 'Ç') { str.at(i) = 'ç'; }
			if (str.at(i) == 'È') { str.at(i) = 'è'; }
			if (str.at(i) == 'É') { str.at(i) = 'é'; }
			if (str.at(i) == 'Ê') { str.at(i) = 'ê'; }
			if (str.at(i) == 'Ë') { str.at(i) = 'ë'; }
			if (str.at(i) == 'Ì') { str.at(i) = 'ì'; }
			if (str.at(i) == 'Í') { str.at(i) = 'í'; }
			if (str.at(i) == 'Î') { str.at(i) = 'î'; }
			if (str.at(i) == 'Ï') { str.at(i) = 'ï'; }
			if (str.at(i) == 'Ð') { str.at(i) = 'ð'; }
			if (str.at(i) == 'Ñ') { str.at(i) = 'ñ'; }
			if (str.at(i) == 'Ò') { str.at(i) = 'ò'; }
			if (str.at(i) == 'Ó') { str.at(i) = 'ó'; }
			if (str.at(i) == 'Ô') { str.at(i) = 'ô'; }
			if (str.at(i) == 'Õ') { str.at(i) = 'õ'; }
			if (str.at(i) == 'Ö') { str.at(i) = 'ö'; }
			if (str.at(i) == '×') { str.at(i) = '÷'; }
			if (str.at(i) == 'Ø') { str.at(i) = 'ø'; }
			if (str.at(i) == 'Ù') { str.at(i) = 'ù'; }
			if (str.at(i) == 'Ý') { str.at(i) = 'ý'; }
			if (str.at(i) == 'Û') { str.at(i) = 'û'; }
			if (str.at(i) == 'Ü') { str.at(i) = 'ü'; }
			if (str.at(i) == 'Þ') { str.at(i) = 'þ'; }
			if (str.at(i) == 'ß') { str.at(i) = 'ÿ'; }
		}


	}
	str.erase(std::remove(str.begin(), str.end(), char("—")), str.end());
	str.erase(std::remove(str.begin(), str.end(), 127), str.end());


	replace(str.begin(), str.end(), '\n', ' ');
	//erase double spaces
	size_t ds = str.find("  ");
	while (ds != std::string::npos)
	{
		str.erase(ds, 1);
		ds = str.find("  ");
	}
	cout << "cleaning done" << endl;
}

// nu tut nazvanie samo za sebya govorit
void erase_spaces(string& str)
{
	str.erase(remove_if(str.begin(), str.end(), isspace), str.end());
}

////count letters appereance
//void letter_freq(string &str, map<string, float> &mp)
//{
//	//count 
//	string tmpstr;
//	for (int i = 0; i < str.length(); i++)
//	{
//		if (str.at(i) != 127)
//		{
//			//mp[str.at(i)] ++;
//			tmpstr = str.substr(i, 1);
//			mp[tmpstr] ++;
//			tmpstr.clear();
//
//		}
//	}
//
//}



//count ngramm appereance
void ngramm_freq(string& str, map <string, float> &mp, int n)
{
	//bool contdel;
	string tmpstr;
	for (int i = 0; i < str.length() && i + n != str.length() - 1; i++)
	{
		
			tmpstr = str.substr(i, n);
			mp[tmpstr] ++;
			tmpstr.clear();

	}
}

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

//frequency of letter in per cents
map<string, float> perc_freq(int length, map<string, float> &mp, bool nocover)
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
		map_fr.insert({ it->first, (it->second/ length) });
	}

	return map_fr;
}

// cout map
void show_map(map<string, float> &mp)
{
	for (map<string, float>::const_iterator it = mp.begin(); it != mp.end();++it)
	{
		cout << "'" << it->first << "'" << " " << setprecision(3) << it->second << endl;
	}
}

//fout map
void fout_map(ofstream& ofs, map<string, float>& mp)
{
	for (map<string, float>::const_iterator it = mp.begin(); it != mp.end(); ++it)
	{
		ofs << "'"  << it->first << "' " << setprecision(3) << it->second << endl;
	}
}

//count enthropy
float enthropy_calc(map<string, float>& mp, float n)
{
	float H = 0;
	for (map<string, float>::const_iterator it = mp.begin(); it != mp.end(); ++it)
	{
		H -= it->second * log2(it->second);
	}
	cout << H << "		";
	H = H / n;
	cout << H << endl;

	return H;
}


//void fout_matrix_for_bigram(map <string, float>& lt, map<string, float>& fr, ofstream &fout, int m)
//{
//	map<string, float>::const_iterator it2 = fr.begin();
//	map<string, float>::const_iterator iter = lt.begin();
//	int n = 0;
//	string tmp;
//
//	//1st row
//	for (map<string, float>::const_iterator it = lt.begin(); it != lt.end(); ++it)
//	{
//		fout << it->first << "	|	";
//	}
//	fout << endl;
//
//	for (map<string, float>::const_iterator it = lt.begin(); it != lt.end(); ++it)
//	{
//		n = 0;
//		fout << it->first << "	| ";
//		for (n; n<m && it2 != fr.end(); n++)
//		{
//			tmp = string(it->first);
//			tmp += string((iter + n)->first);
//
//			if (it2->first == tmp)
//			{
//				fout << it2->second << "	";
//			}
//			else
//			{
//				fout << "		";
//			}
//				++it2;
//				iter = lt.begin();
//			
//		}
//		fout << endl;
//	}
//}