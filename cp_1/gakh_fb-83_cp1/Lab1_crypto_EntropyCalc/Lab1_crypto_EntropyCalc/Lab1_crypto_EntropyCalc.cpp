#include "complete_funcs.h"

int main()
{
    setlocale(LC_ALL, "Russian");
    system("cd");
    char c = '\n'; unsigned int lang = 1, n = 1;
    printf("Choose the lang of your text(rus=1|eng=0): ");
    scanf("%u",&lang);
    printf("The max n-gramm length(<9) : ");
    scanf("%u", &n);
    calculate_text_entropy_for_ngramm_MAP(lang, n, false);
    calculate_text_entropy_for_ngramm_MAP(lang, n, true);
    return 0;
}

