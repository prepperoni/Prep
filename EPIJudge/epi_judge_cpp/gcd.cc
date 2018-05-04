#include "test_framework/generic_test.h"

using namespace std;

long long Gcd(long long x, long long y) {
  // Implement this placeholder.
	if (x & 1 == 0 && y & 1 == 0) {
		return Gcd(x >> 1, y >> 1) << 1;
	} else if (x & 1 == 1 && y & 1 == 1) {
		return Gcd(min(x, y), max(x, y) - min(x, y));
	} else {
		if (x & 1 == 0) {
			x >>= 1;
		}
		if (y & 1 == 0) {
			y >>= 1;
		}

		return gcd(x, y);
	}
  return 0;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "y"};
  return GenericTestMain(args, "gcd.tsv", &Gcd, DefaultComparator{},
                         param_names);
}
