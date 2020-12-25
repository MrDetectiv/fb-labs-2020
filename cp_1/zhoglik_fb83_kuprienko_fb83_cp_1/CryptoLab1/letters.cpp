#include "Header.hpp"

void setAlphabet(char letters[]) {
	for (int i = 224; i <= 255; i++) {
		letters[i - 224] = (char)i;
	}
}

void setAlhabetWithSpace(char letters[]) {
	for (int i = 224; i < 250; i++) {
		letters[i - 224] = (char)i;
	}
	for (int i = 251; i <= 255; i++) {
		letters[i - 225] = (char)i;
	}
	letters[ALPHABET_LENGTH - 1] = ' ';
}

void printLetterAmount(char letters[], int letterAmount[]) {
	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		std::cout << letters[i] << " : " << letterAmount[i] << std::endl;
	}
}

void countLetterAmount(char array[], int length, char letters[], int letterAmount[]) {
	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		letterAmount[i] = 0;
	}

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		char tmp = letters[i];

		for (int j = 0; j < length; j++) {
			if (array[j] == tmp) {
				letterAmount[i] += 1;
			}
		}
	}
}

int countRealLength(int letterAmount[]) {
	int result = 0;

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		result += letterAmount[i];
	}

	return result;
}

void countLetterFrequency(int letterAmount[], double letterFrequency[], int realLength) {
	double dRealLength = static_cast<double>(realLength);
	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		double p = (static_cast<double>(letterAmount[i]) / dRealLength);
		letterFrequency[i] = p;
	}
}

void printLetterFrequencySorted(double letterFrequency[], char letters[]) {
	double frequencyTmp[ALPHABET_LENGTH];
	char lettersTmp[ALPHABET_LENGTH];

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		frequencyTmp[i] = letterFrequency[i];
		lettersTmp[i] = letters[i];
	}

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		for (int j = i + 1; j < ALPHABET_LENGTH; j++) {
			if (frequencyTmp[i] < frequencyTmp[j]) {
				std::swap(frequencyTmp[i], frequencyTmp[j]);
				std::swap(lettersTmp[i], lettersTmp[j]);
			}
		}
	}

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		std::cout << lettersTmp[i] << " : " << std::setprecision(6) << frequencyTmp[i] << std::endl;
	}
}

void printLetterFrequencySortedToFile(std::ofstream *out, double letterFrequency[], char letters[]) {
	double frequencyTmp[ALPHABET_LENGTH];
	char lettersTmp[ALPHABET_LENGTH];

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		frequencyTmp[i] = letterFrequency[i];
		lettersTmp[i] = letters[i];
	}

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		for (int j = i + 1; j < ALPHABET_LENGTH; j++) {
			if (frequencyTmp[i] < frequencyTmp[j]) {
				std::swap(frequencyTmp[i], frequencyTmp[j]);
				std::swap(lettersTmp[i], lettersTmp[j]);
			}
		}
	}

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		*out << lettersTmp[i] << " : " << std::setprecision(6) << frequencyTmp[i] << std::endl;
	}
}

double countEntrop(double letterFrequency[]) {
	double result = 0;

	for (int i = 0; i < ALPHABET_LENGTH; i++) {
		double p = letterFrequency[i];
		if (p > 0) {
			result += p * log2(p);
		}
	}
	result *= -1;

	return result;
}