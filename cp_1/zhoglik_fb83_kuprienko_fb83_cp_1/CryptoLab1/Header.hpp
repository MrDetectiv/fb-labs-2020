#pragma once

#include <fstream>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <cstdlib>

#define ALPHABET_LENGTH 32

const std::string fileName = "task.in";

//symbols 
void setAlphabet(char letters[]);
void setAlhabetWithSpace(char letters[]);

void printLetterAmount(char letters[], int letterAmount[]);
void countLetterAmount(char array[], int length, char letters[], int letterAmount[]);
int countRealLength(int letterAmount[]);
void countLetterFrequency(int letterAmount[], double letterFrequency[], int realLength);
void printLetterFrequencySorted(double letterFrequency[], char letters[]);
void printLetterFrequencySortedToFile(std::ofstream* out, double letterFrequency[], char letters[]);
double countEntrop(double letterFrequency[]);



//bigrams
void filtrateArrayForBigram(char source[], int sourceLength, char target[]);
void filtrateArrayForBigramWithSpace(char source[], int sourceLength, char target[]);

void setBigrams(char letters[], char(&bigrams)[ALPHABET_LENGTH][ALPHABET_LENGTH][2]);
void countBigramAmountIntersection(char textBigramArray[], int realLength, int(&bigramAmountIntersection)[ALPHABET_LENGTH][ALPHABET_LENGTH], char(&bigrams)[ALPHABET_LENGTH][ALPHABET_LENGTH][2]);
void countBigramAmountWithoutIntersection(char textBigramArray[], int realLength, int(&bigramAmountWithoutIntersection)[ALPHABET_LENGTH][ALPHABET_LENGTH], char(&bigrams)[ALPHABET_LENGTH][ALPHABET_LENGTH][2]);
void countBigramFrequency(int(&bigramAmount)[ALPHABET_LENGTH][ALPHABET_LENGTH], double(&bigramFrequency)[ALPHABET_LENGTH][ALPHABET_LENGTH], int realLength);
double countEntropForBigram(double(&bigramAmount)[ALPHABET_LENGTH][ALPHABET_LENGTH]);
void printTable(int(&array)[ALPHABET_LENGTH][ALPHABET_LENGTH], char letters[]);
void printTable(double(&array)[ALPHABET_LENGTH][ALPHABET_LENGTH], char letters[]);
void printTableToFile(std::ofstream* out, double(&array)[ALPHABET_LENGTH][ALPHABET_LENGTH], char letters[]);
int countRealLengthBigram(int(&bigramAmount)[ALPHABET_LENGTH][ALPHABET_LENGTH]);