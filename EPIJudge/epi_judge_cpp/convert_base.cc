#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include "test_framework/generic_test.h"

using std::string;
using std::unordered_map;
using std::vector;
using std::reverse;

long long StringToBase10(const string &s, int base) {
	long long result = 0;
	bool isNeg = s[0] == '-';

	for (int i = isNeg ? 1 : 0; i < s.size(); ++i) {
		result *= base;
		result += isdigit(s[i]) ? s[i] - '0' : s[i] - 'A' + 10;
	}

	return isNeg ? result * -1 : result;
}

//4273672

string Base10ToBaseN(long long num, int base) {
	vector<char> res;
	bool isNeg = num < 0;

	if (!num) {
		return "0";
	}

	if (isNeg) {
		num = -num;
	}

	while (num) {
		int modVal = num % base;
		res.emplace_back(modVal < 10 ? '0' + modVal : 'A' + (modVal - 10));
		num /= base;
	}

	if (isNeg) {
		res.emplace_back('-');
	}

	reverse(res.begin(), res.end());
	string s(res.begin(), res.end());

	return s;
}

string ConvertBase(const string& num_as_string, int b1, int b2) {
  long long base10 = StringToBase10(num_as_string, b1);
  return Base10ToBaseN(base10, b2);
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"num_as_string", "b1", "b2"};
  return GenericTestMain(args, "convert_base.tsv", &ConvertBase,
                         DefaultComparator{}, param_names);
}
