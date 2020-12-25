#include "Header.hpp"

int fileLen(std::ifstream* in) {
	int length = 0;
	char tmp;

	for (; !in->eof(); length++) {
		*in >> tmp;
	}

	in->close();
	in->open(fileName);

	return length - 1;
}

void readFile(std::ifstream* in, char array[], int length) {
	*in >> std::noskipws;
	for (int i = 0; i < length; i++) {
		*in >> array[i];
	}
}

void filtrate(char array[], int length) {
	int delta = 32;
	char tmp;

	for (int i = 0; i < length; i++) {
		tmp = array[i];

		if (tmp == '¨' || tmp == '¸') {
			array[i] = 'å';
			//    	std::cout << array[i];
		}
		else if (tmp >= 'À' && tmp <= 'ß') {
			array[i] += delta;
		}
		else if (tmp < 'à' || tmp > 'ÿ') {
			array[i] = ' ';
		}
	}
}

void filtrate(char array[], int length, char lettersArray[], int* realLength) {
	int delta = 32;
	char tmp;
	bool wasLastSpace = false;
	int j = 0;

	for (int i = 0; i < length; i++) {
		tmp = array[i];

		if (tmp == '¨' || tmp == '¸') {
			lettersArray[j] = 'å';
			j += 1;
			wasLastSpace = false;
		}
		else if (tmp == 'Ú' || tmp == 'ú') {
			lettersArray[j] = 'ü';
			j += 1;
			wasLastSpace = false;
		}
		else if (tmp >= 'À' && tmp <= 'ß') {
			lettersArray[j] = tmp + delta;
			j += 1;
			wasLastSpace = false;
		}
		else if (tmp >= 'à' && tmp <= 'ÿ') {
			lettersArray[j] = tmp;
			j += 1;
			wasLastSpace = false;
		} 
		else if (tmp == ' ' && !wasLastSpace) {
			lettersArray[j] = ' ';
			j += 1;
			wasLastSpace = true;
		}
	}
	*realLength = j;
}

void taskForTextWitoutSpaces() {
	std::ifstream in(fileName);

	int length = fileLen(&in);
	char* textArray = new char[length];
	int realLength;

	char* letters = new char[ALPHABET_LENGTH];
	int* letterAmount = new int[ALPHABET_LENGTH];
	double* letterFrequency = new double[ALPHABET_LENGTH];
	std::ofstream outLF("letterFrequencySorted.txt");

	readFile(&in, textArray, length);

	filtrate(textArray, length);

	setAlphabet(letters);

	countLetterAmount(textArray, length, letters, letterAmount);

	realLength = countRealLength(letterAmount);

	countLetterFrequency(letterAmount, letterFrequency, realLength);

	//printLetterFrequencySorted(letterFrequency, letters);

	printLetterFrequencySortedToFile(&outLF, letterFrequency, letters);

	std::cout << "Symbols entrop: " << countEntrop(letterFrequency) << std::endl;


	int realLengthBigramIntersection;
	int realLengthBigramWithoutIntersection;
	char* textBigramArray = new char[realLength];
	char bigrams[ALPHABET_LENGTH][ALPHABET_LENGTH][2];
	int bigramAmountIntersection[ALPHABET_LENGTH][ALPHABET_LENGTH];
	int bigramAmountWithoutIntersection[ALPHABET_LENGTH][ALPHABET_LENGTH];
	double bigramFrequencyIntersection[ALPHABET_LENGTH][ALPHABET_LENGTH];
	double bigramFrequencyWithoutIntersection[ALPHABET_LENGTH][ALPHABET_LENGTH];
	std::ofstream outBI("bigramFrequencyIntersection.txt");
	std::ofstream outBWI("bigramFrequencyWithoutIntersection.txt");

	filtrateArrayForBigram(textArray, length, textBigramArray);

	setBigrams(letters, bigrams);

	countBigramAmountIntersection(textBigramArray, realLength, bigramAmountIntersection, bigrams);

	countBigramAmountWithoutIntersection(textBigramArray, realLength, bigramAmountWithoutIntersection, bigrams);

	realLengthBigramIntersection = countRealLengthBigram(bigramAmountIntersection);
	realLengthBigramWithoutIntersection = countRealLengthBigram(bigramAmountWithoutIntersection);

	countBigramFrequency(bigramAmountIntersection, bigramFrequencyIntersection, realLengthBigramIntersection);
	countBigramFrequency(bigramAmountWithoutIntersection, bigramFrequencyWithoutIntersection, realLengthBigramWithoutIntersection);

	printTableToFile(&outBI, bigramFrequencyIntersection, letters);
	printTableToFile(&outBWI, bigramFrequencyWithoutIntersection, letters);

	std::cout << "Bigrams with intersection entrop: " << countEntropForBigram(bigramFrequencyIntersection) << std::endl;
	std::cout << "Bigrams without intersection entrop: " << countEntropForBigram(bigramFrequencyWithoutIntersection) << std::endl;

	in.close();
	outLF.close();
	outBI.close();
	outBWI.close();
}

void taskForTextWithSpaces() {
	std::ifstream in(fileName);

	int length = fileLen(&in);
	char* textArray = new char[length];
	char* lettersArray = new char[length];
	int realLength;

	char* letters = new char[ALPHABET_LENGTH];
	int* letterAmount = new int[ALPHABET_LENGTH];
	double* letterFrequency = new double[ALPHABET_LENGTH];
	std::ofstream outLF("letterFrequencySortedWithSpace.txt");

	readFile(&in, textArray, length);

	filtrate(textArray, length, lettersArray, &realLength);

	setAlhabetWithSpace(letters);

	countLetterAmount(lettersArray, realLength, letters, letterAmount);

	countLetterFrequency(letterAmount, letterFrequency, realLength);

	printLetterFrequencySortedToFile(&outLF, letterFrequency, letters);

	std::cout << "Symbols entrop: " << countEntrop(letterFrequency) << std::endl;

	int realLengthBigramIntersection;
	int realLengthBigramWithoutIntersection;
	char* textBigramArray = new char[realLength];
	char bigrams[ALPHABET_LENGTH][ALPHABET_LENGTH][2];
	int bigramAmountIntersection[ALPHABET_LENGTH][ALPHABET_LENGTH];
	int bigramAmountWithoutIntersection[ALPHABET_LENGTH][ALPHABET_LENGTH];
	double bigramFrequencyIntersection[ALPHABET_LENGTH][ALPHABET_LENGTH];
	double bigramFrequencyWithoutIntersection[ALPHABET_LENGTH][ALPHABET_LENGTH];
	std::ofstream outBI("bigramFrequencyIntersectionWithSpace.txt");
	std::ofstream outBWI("bigramFrequencyWithoutIntersectionWithSpace.txt");

	filtrateArrayForBigramWithSpace(textArray, length, textBigramArray);

	setBigrams(letters, bigrams);

	countBigramAmountIntersection(textBigramArray, realLength, bigramAmountIntersection, bigrams);

	countBigramAmountWithoutIntersection(textBigramArray, realLength, bigramAmountWithoutIntersection, bigrams);

	realLengthBigramIntersection = countRealLengthBigram(bigramAmountIntersection);
	realLengthBigramWithoutIntersection = countRealLengthBigram(bigramAmountWithoutIntersection);

	countBigramFrequency(bigramAmountIntersection, bigramFrequencyIntersection, realLengthBigramIntersection);
	countBigramFrequency(bigramAmountWithoutIntersection, bigramFrequencyWithoutIntersection, realLengthBigramWithoutIntersection);

	printTableToFile(&outBI, bigramFrequencyIntersection, letters);
	printTableToFile(&outBWI, bigramFrequencyWithoutIntersection, letters);

	std::cout << "Bigrams with intersection entrop: " << countEntropForBigram(bigramFrequencyIntersection) << std::endl;
	std::cout << "Bigrams without intersection entrop: " << countEntropForBigram(bigramFrequencyWithoutIntersection) << std::endl;

	in.close();
	outLF.close();
	outBI.close();
	outBWI.close();
}

int main() {
	setlocale(LC_ALL, "Russian");

	taskForTextWitoutSpaces();
	taskForTextWithSpaces();
}