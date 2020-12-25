#include "cryptography_formulas_header.h"

int calculate_ensemble_entropy(map<wstring, float>* ensemble,unsigned int& n, float& entropy)
{
	if (ensemble == NULL)
	{
		printf("Error: NULL ensemble ptr.\n");
		return 1;
	}

	entropy = 0.0f;
	for (map<wstring, float>::iterator iter = ensemble->begin(); iter != ensemble->end(); iter++)
	{
		if (iter->second > 0.0f)
		{
			entropy += -1 * iter->second * log2(iter->second);
		}
	}
	entropy = entropy / (float)n;
	return 0;
}
