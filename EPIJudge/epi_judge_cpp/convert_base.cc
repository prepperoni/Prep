#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include "test_framework/generic_test.h"

using std::string;
using std::unordered_map;
using std::vector;
using std::reverse;

long long StringToBase10(const string &s, int base, unordered_map<char, int> &charToInt) {
	long long result = 0;
	long long powerVal = 1;

	for (int i=s.size()-1; i >= 0; --i ) {
		result += powerVal * charToInt[s[i]];
		powerVal *= base;
	}

	std::cout << "string to base10: " << result << std::endl;
	return result;
}

string Base10ToBaseN(long long num, int base, unordered_map<int, char> &intToChar) {
	long long digits = (log(num) / log(base)) + 1;
	auto result = vector<char>(digits, '0');

	while (num) {
		long long digit = log(num) / log(base);
		long long expNum = pow(base, digit);
		int divRes = num / expNum;
		result[digit] = intToChar[divRes];
		num -= divRes * expNum;
	}

	reverse(result.begin(), result.end());
	string res = string(result.begin(), result.end());
	return res;
}

string ConvertBase(const string& num_as_string, int b1, int b2) {
  unordered_map<int, char> intToChar = {{0,'0'},{1,'1'},{2,'2'},{3,'3'},{4,'4'},{5,'5'},{6,'6'},{7,'7'},{8,'8'},{9,'9'},{10,'A'},{11,'B'},{12,'C'},{13,'D'},{14,'E'},{15,'F'}};
  unordered_map<char, int> charToInt = {{'0',0},{'1',1},{'2',2},{'3',3},{'4',4},{'5',5},{'6',6},{'7',7},{'8',8},{'9',9},{'A',10},{'B',11},{'C',12},{'D',13},{'E',14},{'F',15}};
  long long base10 = StringToBase10(num_as_string, b1, charToInt);
  return Base10ToBaseN(base10, b2, intToChar);
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"num_as_string", "b1", "b2"};
  return GenericTestMain(args, "convert_base.tsv", &ConvertBase,
                         DefaultComparator{}, param_names);
}
