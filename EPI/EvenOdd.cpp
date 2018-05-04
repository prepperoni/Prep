#include <vector>
#include <iostream>

using namespace std;

void EvenOdd(vector<int> &vec) {
	int evenIdx = 0, oddIdx = vec.size() - 1;

	while (evenIdx < oddIdx) {
		if (vec[evenIdx] % 2 == 0) {
			evenIdx++;
		} else {
			swap(vec[evenIdx], vec[oddIdx]);
			oddIdx--;
		}
	}
}

int main() {
	vector<int> v {1, 2, 3, 4, 5, 6, 7, 8};
	EvenOdd(v);

	for (int i : v) {
		cout << i << endl;
	}
}