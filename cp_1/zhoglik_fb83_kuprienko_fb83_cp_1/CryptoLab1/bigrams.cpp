#include "Header.hpp"

void filtrateArrayForBigram(char source[], int sourceLength, char target[]) {
	for (int i = 0, j = 0; i < sourceLength; i++) {
		char tmp = source[i];
		if (tmp >= 'à' && tmp <= 'ÿ') {
			target[j] = tmp;
			j += 1;
		}
	}
}

void filtrateArrayForBigramWithSpace(char source[], int sourceLength, char target[]) {
	for (int i = 0, j = 0; i < sourceLength; i++) {
		char tmp = source[i];
		if (tmp >= 'à' && tmp <= 'ÿ' || tmp == ' ') {
			target[j] = tmp;
			j += 1;
		}
	}
}

void setBigrams(char letters[], char(&bigrams)[ALPHABET_LENGTH][ALPHABET_LENGTH][2]) {
	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			bigrams[i][j][0] = letters[i];
			bigrams[i][j][1] = letters[j];
		}
	}
}

void countBigramAmountIntersection(char textBigramArray[], int realLength, int(&bigramAmountIntersection)[ALPHABET_LENGTH][ALPHABET_LENGTH], char(&bigrams)[ALPHABET_LENGTH][ALPHABET_LENGTH][2]) {
	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			bigramAmountIntersection[i][j] = 0;
		}
	}

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			char tmp[2];
			tmp[0] = bigrams[i][j][0];
			tmp[1] = bigrams[i][j][1];

			for (int k = 0; k < realLength; k++) {
				if (tmp[0] == textBigramArray[k] && tmp[1] == textBigramArray[k + 1]) {
					bigramAmountIntersection[i][j] += 1;
				}
			}
		}
	}
}

void countBigramAmountWithoutIntersection(char textBigramArray[], int realLength, int(&bigramAmountWithoutIntersection)[ALPHABET_LENGTH][ALPHABET_LENGTH], char(&bigrams)[ALPHABET_LENGTH][ALPHABET_LENGTH][2]) {
	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			bigramAmountWithoutIntersection[i][j] = 0;
		}
	}

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			char tmp[2];
			tmp[0] = bigrams[i][j][0];
			tmp[1] = bigrams[i][j][1];

			for (int k = 0; k < realLength; k += 2) {
				if (tmp[0] == textBigramArray[k] && tmp[1] == textBigramArray[k + 1]) {
					bigramAmountWithoutIntersection[i][j] += 1;
				}
			}
		}
	}
}

void countBigramFrequency(int(&bigramAmount)[ALPHABET_LENGTH][ALPHABET_LENGTH], double(&bigramFrequency)[ALPHABET_LENGTH][ALPHABET_LENGTH], int realLength) {
	double dRealLength = static_cast<double>(realLength);
	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			bigramFrequency[i][j] = static_cast<double>(bigramAmount[i][j]) / dRealLength;
		}
	}
}

double countEntropForBigram(double(&bigramFrequency)[ALPHABET_LENGTH][ALPHABET_LENGTH]) {
	double result = 0;

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			if (bigramFrequency[i][j] > 0) {
				double p = bigramFrequency[i][j];
				result += p * log2(p) / 2;
			}
		}
	}
	result *= -1;

	return result;
}

void printTable(int(&array)[ALPHABET_LENGTH][ALPHABET_LENGTH], char letters[]) {
	std::cout << "  ";
	for (int k = 0; k < ALPHABET_LENGTH; k++) {
		std::cout << std::setw(3) << letters[k] << " ";
	}
	std::cout << std::endl;
	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		std::cout << letters[i] << " ";
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			std::cout << std::setw(3) << array[i][j] << " ";
		}
		std::cout << std::endl;
	}
}

void printTable(double(&array)[ALPHABET_LENGTH][ALPHABET_LENGTH], char letters[]) {
	std::cout.precision(4);
	std::cout << std::fixed;

	std::cout << "  ";
	for (int k = 0; k < ALPHABET_LENGTH; k++) {
		std::cout << std::setw(6) << letters[k] << " ";
	}
	std::cout << std::endl;

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		std::cout << letters[i] << " ";
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			std::cout << std::setw(6) << (array[i][j]*1000) << " ";
		}
		std::cout << std::endl;
	}
}

void printTableToFile(std::ofstream *out ,double(&array)[ALPHABET_LENGTH][ALPHABET_LENGTH], char letters[]) {
	out->setf(std::ios::fixed);
	*out << std::setprecision(8);

	for (int k = 0; k < ALPHABET_LENGTH; k++) {
		*out << std::setw(10) << letters[k] << " ";
	}
	*out << std::endl;

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		*out << letters[i] << " ";
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			*out << std::setw(10) << (array[i][j]) << " ";
		}
		*out << std::endl;
	}
}

int countRealLengthBigram(int(&bigramAmount)[ALPHABET_LENGTH][ALPHABET_LENGTH]) {
	int result = 0;
	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		for (int j = 0; j < ALPHABET_LENGTH; j++) {
			result += bigramAmount[i][j];
		}
	}
	return result;
}
