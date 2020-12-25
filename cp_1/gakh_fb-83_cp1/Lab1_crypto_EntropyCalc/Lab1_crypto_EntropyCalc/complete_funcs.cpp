#include "complete_funcs.h"

int calculate_text_entropy_for_ngramm_MAP(unsigned int lang, unsigned int n_for_gramm, bool ignoreBlanks)
{
    if (n_for_gramm > 9)
    {
        printf("Error: too long gramm.\n");
        return 1;
    }
    if (!ignoreBlanks) printf("////////////////////////\nAnalysing text including blanks...\n////////////////////////\n");
    else printf("////////////////////////\nAnalysing text NOT including blanks...\n////////////////////////\n");
    char c = '\n';
    printf("Do you want to use custom i/o files(y/n): ");
    while (c=='\n') c = getchar();
    char* raw_file_name_buffer;
    char* plain_file_name_buffer;
    char* entropy_out_f_name_overlap;
    char* entropy_out_f_name_nooverlap;
    if (c == 'y')
    {
        raw_file_name_buffer = new char[fname_buff_size];
        plain_file_name_buffer = new char[fname_buff_size];
        entropy_out_f_name_overlap = new char[fname_buff_size];
        entropy_out_f_name_nooverlap = new char[fname_buff_size];
        printf("Enter filename|path of text file with raw text: ");
        scanf("%s", raw_file_name_buffer);
        printf("Enter filename|path for plain text file : ");
        scanf("%s", plain_file_name_buffer);
        printf("Enter filename|path for entropy_out_overlap text file : ");
        scanf("%s", entropy_out_f_name_overlap);
        printf("Enter filename|path for entropy_out_nooverlap text file : ");
        scanf("%s", entropy_out_f_name_nooverlap);
    }
    else
    {
        raw_file_name_buffer = filename_copy("raw_text.txt", NULL, 0);
        if (ignoreBlanks)
        {
            plain_file_name_buffer = filename_copy("plain_text_NOblanks.txt", NULL, 0);
        }
        else
        {
            plain_file_name_buffer = filename_copy("plain_text_ANDblanks.txt", NULL, 0);
        }

        if (ignoreBlanks)
        {
            entropy_out_f_name_overlap = filename_copy("entropy_out_NOblanks_overlap.txt", NULL, 0);
            entropy_out_f_name_nooverlap = filename_copy("entropy_out_NOblanks_nooverlap.txt", NULL, 0);
        }
        else
        {
            entropy_out_f_name_overlap = filename_copy("entropy_out_ANDblanks_overlap.txt", NULL, 0);
            entropy_out_f_name_nooverlap = filename_copy("entropy_out_ANDblanks_nooverlap.txt", NULL, 0);
        }
    }    
    //                                                                                       preparing  for entropy calculation
    printf("Text files: %s, %s, %s, %s\n", raw_file_name_buffer, plain_file_name_buffer, entropy_out_f_name_overlap, entropy_out_f_name_nooverlap);
    //                                                                                       filtering raw text from ,.? etc..
    if (filter_text(raw_file_name_buffer, plain_file_name_buffer, lang, ignoreBlanks))
    {
        printf("Error filtering raw text.\n");
        return 1;
    }
    //                                                                                       n-gramm rate calculation
    unsigned long int tmp_arr[5] = { lang, 1 , 0, 0, 0};
    char* gramm_data_f_name_overlap;
    char* gramm_data_f_name_nooverlap;
    if (ignoreBlanks)
    {
        gramm_data_f_name_overlap = filename_copy("1-gramm_data_NOblanks_overlap.txt", NULL, 0);
        gramm_data_f_name_nooverlap = filename_copy("1-gramm_data_NOblanks_nooverlap.txt", NULL, 0);
    }
    else
    {
        gramm_data_f_name_overlap = filename_copy("1-gramm_data_ANDblanks_overlap.txt", NULL, 0);
        gramm_data_f_name_nooverlap = filename_copy("1-gramm_data_ANDblanks_nooverlap.txt", NULL, 0);
    }
    FILE* entropy_file_overlap = fopen(entropy_out_f_name_overlap, "a");
    FILE* entropy_file_nooverlap = fopen(entropy_out_f_name_nooverlap, "a");
    for (unsigned int i = 1; i <= n_for_gramm; i++)
    {
        map<wstring, float>* ensemble_overlap = new map<wstring, float>();
        map<wstring, float>* ensemble_nooverlap = new map<wstring, float>();
        float entropy_overlap = 0.0f, entropy_nooverlap = 0.0f;
        tmp_arr[1] = i;
        gramm_data_f_name_overlap[0] = (char)(i + (int)'1' - 1);
        gramm_data_f_name_nooverlap[0] = (char)(i + (int)'1' - 1);
        generate_gramm_rate_file_MAP(plain_file_name_buffer, gramm_data_f_name_overlap, gramm_data_f_name_nooverlap, ignoreBlanks, tmp_arr, ensemble_overlap, ensemble_nooverlap);
        fprintf(entropy_file_overlap, "lang=%u ; N=%u ; blanks=%u\n", lang, tmp_arr[2], tmp_arr[4]);
        fprintf(entropy_file_nooverlap, "lang=%u ; N=%u ; blanks=%u\n", lang, tmp_arr[3], tmp_arr[4]);
        
        calculate_ensemble_entropy(ensemble_overlap, i, entropy_overlap);
        calculate_ensemble_entropy(ensemble_nooverlap, i, entropy_nooverlap);
        fprintf(entropy_file_overlap,"n=%u ; H=%0.12f\n",i , entropy_overlap);
        fprintf(entropy_file_nooverlap, "n=%u ; H=%0.12f\n", i, entropy_nooverlap);
    }
    fprintf(entropy_file_overlap, "------------------------------------------\n");
    fprintf(entropy_file_nooverlap, "------------------------------------------\n");
    fclose(entropy_file_overlap);
    fclose(entropy_file_nooverlap);
    
    return 0;
}
