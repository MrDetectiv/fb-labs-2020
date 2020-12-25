#include "header.h"



int filter_text(char* f_raw_name, char* f_plain_name, int lang, bool ignoreBlanks)
{
	FILE* f_raw_txt = fopen(f_raw_name, "r");
	if (f_raw_txt == NULL)
	{
		printf("Error opening raw text file(This file doesn`t exist).\n");
		return 1;
	}
	FILE* f_plain_txt = fopen(f_plain_name, "w");
	if (f_plain_txt == NULL)
	{
		printf("Error creating file for plain text.\n");
		return 1;
	}

	unsigned int index_lang_first, index_lang_last, lang_upper_index_offset, lang_len;
	const map<unsigned int, unsigned int>* lang_mask = NULL;
	const map<unsigned int, wchar_t>* lang_encode = NULL;
	if ((lang != 0) && (lang != 1))
	{
		printf("Error: wrong .language\n");
		return 1;
	}
	else if (lang == 0)
	{
		index_lang_first = index_eng_first;
		index_lang_last = index_eng_last;
		lang_upper_index_offset = eng_upper_index_offset;
		lang_len = eng_len;
		lang_mask = &eng_lang_mask;
		lang_encode = &eng_lang_encoding;
	}
	else
	{
		index_lang_first = index_rus_first;
		index_lang_last = index_rus_last;
		lang_upper_index_offset = rus_upper_index_offset;
		lang_len = rus_len;
		lang_mask = &rus_lang_mask;
		lang_encode = &rus_lang_encoding;
	}
	wchar_t wchar_in;
	wchar_t wchar_out;
	unsigned int index;
	bool isPrevBlank = false;
	do {
		wchar_in = fgetwc(f_raw_txt);
		index = (unsigned int)wchar_in;
		if ((lang_mask->count(index) == 0)||(index == index_blank))
		{
			if (!ignoreBlanks)
			{
				if (!isPrevBlank)
				{
					fwprintf(f_plain_txt, L"%c", lang_encode->at(index_blank));
				}
				isPrevBlank = true;
			}
		}
		else
		{
			index = lang_mask->at(index);
			wchar_out = wchar_in;
			if ((index_lang_first <= index) && (index <= index_lang_last))
			{
				wchar_out = lang_encode->at(index);
			}
			else if ((index_lang_first - lang_upper_index_offset <= index) && (index <= index_lang_last - lang_upper_index_offset))
			{
				wchar_out = lang_encode->at(index + lang_upper_index_offset);
			}
			fwprintf(f_plain_txt, L"%c", wchar_out);
			isPrevBlank = false;
		}
	} while(wchar_in != WEOF);

	fclose(f_plain_txt);
	fclose(f_raw_txt);
	return 0;
}


int generate_gramm_rate_file_MAP(char* plain_file_name, char* output_file_name_overlap, char* output_file_name_nooverlap,bool ignoreBlanks, unsigned long int text_analysis_params[5], map<wstring, float>* ensemble_overlap, map<wstring, float>* ensemble_nooverlap)
{
	if ((text_analysis_params[0] != 0) && (text_analysis_params[0] != 1))
	{
		printf("Error: wrong language.\n");
		return 1;
	}
	if (text_analysis_params[1] == 0)
	{
		printf("Error: wrong gramm length.\n");
		return 1;
	}
	unsigned int index_first = 0, index_last = 0;
	const map<unsigned int, wchar_t>* lang_encode = NULL;
	const map<unsigned int, unsigned int>* lang_mask = NULL;
	if (text_analysis_params[0] == 1)
	{
		index_first = index_rus_first, index_last = index_rus_last;
		lang_encode = &rus_lang_encoding;
		lang_mask = &rus_lang_mask;
	}
	else
	{
		index_first = index_eng_first, index_last = index_eng_last;
		lang_encode = &eng_lang_encoding;
		lang_mask = &eng_lang_mask;
	}


	unsigned int* stack = new unsigned int[text_analysis_params[1]];
	unsigned long int top = text_analysis_params[1] - 1; bool isEnd = false;
	map<wstring, unsigned long int> hash_table_overlap;
	map<wstring, unsigned long int> hash_table_nooverlap;
	for (unsigned long int i = 0; i < text_analysis_params[1]; i++)
	{
		stack[i] = index_first;
	}
	if (ignoreBlanks)
	{
		while (!isEnd)
		{
			if (stack[top] == lang_mask->at(stack[top]))
			{
				wstring gramm = L"";
				for (unsigned long int i = 0; i <= top; i++)  gramm += { lang_encode->at(stack[i]) };
				hash_table_nooverlap[gramm] = 0;
				hash_table_overlap[gramm] = 0;
			}
			if (stack[top] == index_last)
			{
				while ((stack[top] == index_last) && (top > 0))
				{
					stack[top] = index_first;
					top--;
				}
				if ((top == 0) && (stack[top] == index_last))
				{
					isEnd = true;
				}
				else
				{
					stack[top]++;
					if (stack[top] != lang_mask->at(stack[top])) stack[top]++;
					top = text_analysis_params[1] - 1;
				}
			}
			else
			{
				stack[top]++;
				if (stack[top] != lang_mask->at(stack[top])) stack[top]++;
				if (top != text_analysis_params[1] - 1)
				{
					top++;
				}
			}
		}
	}
	else
	{
		while (!isEnd)
		{
			if (stack[top] == lang_mask->at(stack[top]))
			{
				wstring gramm = L"";
				for (unsigned long int i = 0; i <= top; i++)  gramm += { lang_encode->at(stack[i]) };
				hash_table_nooverlap[gramm] = 0;
				hash_table_overlap[gramm] = 0;
			}
			if (stack[top] == index_last)
			{
				stack[top] = index_blank;
				if (top != text_analysis_params[1] - 1)
				{
					top++;
				}
			}
			else if (stack[top] == index_blank)
			{
				while ((stack[top] == index_blank) && (top > 0))
				{
					stack[top] = index_first;
					top--;
				}
				if ((top == 0) && (stack[top] == index_blank))
				{
					isEnd = true;
				}
				else
				{
					if (stack[top] == index_last)
					{
						stack[top] = index_blank;
					}
					else
					{
						stack[top]++;
						if (stack[top] != lang_mask->at(stack[top])) stack[top]++;
					}
					top = text_analysis_params[1] - 1;
				}
			}
			else
			{
				stack[top]++;
				if (stack[top] != lang_mask->at(stack[top])) stack[top]++;
				if (top != text_analysis_params[1] - 1)
				{
					top++;
				}
			}
		}
	}
	FILE* plain_file = fopen(plain_file_name, "r");
	wchar_t wchar_in;
	deque<wchar_t> current_gramm_overlap;
	deque<wchar_t>  current_gramm_nooverlap;
	unsigned int l = text_analysis_params[1];
	unsigned long int total_chars_nooverlap = 0, total_chars_overlap = 0, blanks_count = 0;
	for (unsigned int i = 0; i < text_analysis_params[1]; i++)
	{
		wchar_in = fgetwc(plain_file);
		if (wchar_in == L' ') blanks_count++;
		current_gramm_overlap.push_back(wchar_in);
		current_gramm_nooverlap.push_back(wchar_in);
	}
	do {
		wchar_in = fgetwc(plain_file);
		if (wchar_in == L' ') blanks_count++;
		if (wchar_in != WEOF)
		{
			wstring gramm = L"";
			for (deque<wchar_t>::iterator i = current_gramm_overlap.begin(); i != current_gramm_overlap.end(); i++)  gramm += { lang_encode->at(lang_mask->at(*i)) };
			hash_table_overlap[gramm]++;
			total_chars_overlap++;

			current_gramm_overlap.pop_front();
			current_gramm_overlap.push_back(wchar_in);

			if (l == text_analysis_params[1])
			{
				wstring gramm = L"";
				for (deque<wchar_t>::iterator i = current_gramm_nooverlap.begin(); i != current_gramm_nooverlap.end(); i++)  gramm += { lang_encode->at(lang_mask->at(*i)) };
				hash_table_nooverlap[gramm]++;
				total_chars_nooverlap++;
				for (unsigned int i = 0; i < text_analysis_params[1]; i++)
				{
					current_gramm_nooverlap.pop_back();
				}
				current_gramm_nooverlap.push_back(wchar_in);
				l = 1;
			}
			else
			{
				current_gramm_nooverlap.push_back(wchar_in);
				l++;
			}
		}
	} while (wchar_in != WEOF);
	fclose(plain_file);
	text_analysis_params[2] = total_chars_overlap;
	text_analysis_params[3] = total_chars_nooverlap;
	text_analysis_params[4] = blanks_count;

	//                                                                                 outputing text info for overlap
	FILE* gramm_output_overlap = fopen(output_file_name_overlap, "w");
	fprintf(gramm_output_overlap, "%d %d %d %d\n", text_analysis_params[0], text_analysis_params[1], total_chars_overlap, blanks_count);
	fclose(gramm_output_overlap);
	//                                                                                 outputing text info for nooverlap
	FILE* gramm_output_nooverlap = fopen(output_file_name_nooverlap, "w");
	fprintf(gramm_output_nooverlap, "%d %d %d %d\n", text_analysis_params[0], text_analysis_params[1], total_chars_nooverlap, blanks_count);
	fclose(gramm_output_nooverlap);

	unsigned long int  current_ngramm_count = 0;
	float current_ngramm_rate = 0.0f;
	//                                                                                     rate for overlapped
	FILE* gramm_output_new_overlap = fopen(output_file_name_overlap, "a");
	map<wstring, float> map_for_sort_overlap;
	for (map<wstring, unsigned long int>::iterator i = hash_table_overlap.begin(); i != hash_table_overlap.end(); i++)
	{
		current_ngramm_count = i->second;
		current_ngramm_rate = (float)(current_ngramm_count) / (float)(total_chars_overlap);
		map_for_sort_overlap[i->first] = current_ngramm_rate;
		ensemble_overlap->insert(pair<wstring, float>(i->first, current_ngramm_rate));
		fwprintf(gramm_output_new_overlap, L"%s %d %0.9f\n", i->first.c_str(), current_ngramm_count, current_ngramm_rate);
	}
	fclose(gramm_output_new_overlap);
	//                                                                                       rate for nooverlapped
	FILE* gramm_output_new_nooverlap = fopen(output_file_name_nooverlap, "a");
	map<wstring, float> map_for_sort_nooverlap;
	for (map<wstring, unsigned long int>::iterator i = hash_table_nooverlap.begin(); i != hash_table_nooverlap.end(); i++)
	{
		current_ngramm_count = i->second;
		current_ngramm_rate = (float)(current_ngramm_count) / (float)(total_chars_nooverlap);
		map_for_sort_nooverlap[i->first] = current_ngramm_rate;
		ensemble_nooverlap->insert(pair<wstring, float>(i->first, current_ngramm_rate));
		fwprintf(gramm_output_new_nooverlap, L"%s %d %0.9f\n", i->first.c_str(), current_ngramm_count, current_ngramm_rate);
	}
	fclose(gramm_output_new_nooverlap);

	char* f_name_overlap;
	char* f_name_nooverlap;
	if (ignoreBlanks)
	{
		f_name_overlap = filename_copy("_-gramm_rate_data_SORTED_NOblanks_overlap.txt",NULL,0);
		f_name_nooverlap = filename_copy("_-gramm_rate_data_SORTED_NOblanks_nooverlap.txt", NULL, 0);
	}
	else
	{
		f_name_overlap = filename_copy("_-gramm_rate_data_SORTED_ANDblanks_overlap.txt",NULL,0);
		f_name_nooverlap = filename_copy("_-gramm_rate_data_SORTED_ANDblanks_nooverlap.txt", NULL, 0);
	}
	f_name_overlap[0] = (char)(text_analysis_params[1] + (int)'1' - 1);
	f_name_nooverlap[0] = (char)(text_analysis_params[1] + (int)'1' - 1);
	output_ngramm_rate_sorted(text_analysis_params[0], text_analysis_params[1], ignoreBlanks, &map_for_sort_overlap, f_name_overlap);
	output_ngramm_rate_sorted(text_analysis_params[0], text_analysis_params[1], ignoreBlanks, &map_for_sort_nooverlap, f_name_nooverlap);
	return 0;
}

int sort_map_by_rate(map<wstring, float>* hash_table, vector<map<wstring, float>::iterator>& sorted_arr)
{
	if (hash_table == NULL)
	{
		printf("Error: NULL map in sort.\n");
		return 1;
	}

	for (map<wstring, float>::iterator i = hash_table->begin(); i != hash_table->end(); i++)
	{
		sorted_arr.push_back(i);
	}
	quickSort(sorted_arr, 0, sorted_arr.size() - 1);
	return 0;
}

void quickSort(vector<map<wstring, float>::iterator>& iterators_array, unsigned long int left, unsigned long int right)
{
	for (unsigned long int i = left; i < right; i++)
	{
		for (unsigned long int j = i + 1; j <= right; j++)
		{
			if (iterators_array[j]->second > iterators_array[i]->second)
			{
				map<wstring, float>::iterator tmp = iterators_array[j];
				iterators_array[j] = iterators_array[i];
				iterators_array[i] = tmp;
			}
		}
	}
}

int output_ngramm_rate_sorted(unsigned long int lang, unsigned long int n, bool ignoreBlanks, map<wstring, float>* hash_table, char* output_f_name)
{
	if (lang >= 2)
	{
		return 1;
	}
	if (n > 2)
	{
		return 1;
	}
	else if ((n == 1))
	{
		vector<map<wstring, float>::iterator> sorted_arr;
		sort_map_by_rate(hash_table, sorted_arr);
		FILE* output_file = fopen(output_f_name, "w");
		for (unsigned long int i = 0; i < sorted_arr.size(); i++)
		{
			//if (sorted_arr[i]->first.c_str()[0] == ' ') fwprintf(output_file, L"'%s' %0.9f\n", sorted_arr[i]->first.c_str(), sorted_arr[i]->second);
			fwprintf(output_file, L"%s %0.3f\n", sorted_arr[i]->first.c_str(), sorted_arr[i]->second);
		}
		fclose(output_file);
	}
	else
	{
		const map<unsigned int, wchar_t>* lang_encoding;
		const map<unsigned int, unsigned int>* lang_mask;
		unsigned int index_first, index_last;
		if (lang == 0)
		{
			lang_encoding = &eng_lang_encoding;
			lang_mask = &eng_lang_mask;
			index_first = index_eng_first;
			index_last = index_eng_last;
		}
		else
		{
			lang_encoding = &rus_lang_encoding;
			lang_mask = &rus_lang_mask;
			index_first = index_rus_first;
			index_last = index_rus_last;
		}
		FILE* output_file = fopen(output_f_name, "w");
		fwprintf(output_file, L" ");
		for (unsigned int i = index_first; i <= index_last; i++)
		{
			if (i != lang_mask->at(i)) continue;
			fwprintf(output_file, L"|   %c    ", lang_encoding->at(i));
		}
		if (!ignoreBlanks) fwprintf(output_file, L"|   %c    \n", lang_encoding->at(index_blank));
		else fwprintf(output_file, L"\n");
		//                                                                                         columns
		for (unsigned int i = index_first; i <= index_last; i++)
		{
			if (i != lang_mask->at(i)) continue;
			fwprintf(output_file, L"-");
			for (unsigned int j = index_first; j <= index_last; j++)
			{
				if (j != lang_mask->at(j)) continue;
				fwprintf(output_file, L"---------");
			}
			fwprintf(output_file, L"---------\n");
			
			fwprintf(output_file, L"%c", lang_encoding->at(i));
			for (unsigned int j = index_first; j <= index_last; j++)
			{
				if (j != lang_mask->at(j)) continue;
				wstring gramm = L"";
				gramm += { lang_encoding->at(i) };
				gramm += { lang_encoding->at(j) };
				fwprintf(output_file, L"|%0.6f", hash_table->at(gramm));
			}
			if (!ignoreBlanks)
			{
				wstring gramm = L"";
				gramm += { lang_encoding->at(i) };
				gramm += { lang_encoding->at(index_blank) };
				fwprintf(output_file, L"|%0.6f\n", hash_table->at(gramm));
			}
			else fwprintf(output_file, L"\n");
		}
		//                                                                                 low-border + floats
		fwprintf(output_file, L"-");
		for (unsigned int j = index_first; j <= index_last; j++)
		{
			if (j != lang_mask->at(j)) continue;
			fwprintf(output_file, L"---------");
		}
		fwprintf(output_file, L"----------\n");
		if (!ignoreBlanks)
		{
			fwprintf(output_file, L" ");
			for (unsigned int j = index_first; j <= index_last; j++)
			{
				if (j != lang_mask->at(j)) continue;
				wstring gramm = L"";
				gramm += { lang_encoding->at(index_blank) };
				gramm += { lang_encoding->at(j) };
				fwprintf(output_file, L"|%0.6f", hash_table->at(gramm));
			}
			fwprintf(output_file, L"|%0.6f\n", hash_table->at(L"  "));
		}
		//                                                                                 low-border + row with blanks
		fwprintf(output_file, L"-");
		for (unsigned int j = index_first; j <= index_last; j++)
		{
			if (j != lang_mask->at(j)) continue;
			fwprintf(output_file, L"---------");
		}
		fwprintf(output_file, L"---------");
		//                                                                                  final low-border
		fclose(output_file);
	}
	return 0;
}

char* filename_copy(const char* fname, const char** dir_array, unsigned int dir_len)
{
	if ((dir_array == NULL) || (dir_len == 0))
	{
		char* final_fname = new char[strlen(fname) + 1];
		for (unsigned int i = 0; i < strlen(fname); i++)
		{
			final_fname[i] = fname[i];
		}
		final_fname[strlen(fname)] = '\0';
		return final_fname;
	}
	unsigned long int final_name = 0;
	for (unsigned int i = 0; i < dir_len; i++)
	{
		final_name += strlen(dir_array[i]) + 1;
	}

	char* final_fname = new char[final_name+strlen(fname)+1];
	unsigned long int index = 0;
	for (unsigned int i = 0; i < dir_len; i++)
	{
		for (unsigned int j = 0; j < strlen(dir_array[i]); j++)
		{
			final_fname[index+j] = dir_array[i][j];
		}
		index += strlen(dir_array[i]);
		final_fname[index] = '\\';
		index++;
	}
	for (unsigned int i = 0; i < strlen(fname); i++)
	{
		final_fname[index + i] = fname[i];
	}
	final_fname[final_name] = '\0';
	return final_fname;
}
