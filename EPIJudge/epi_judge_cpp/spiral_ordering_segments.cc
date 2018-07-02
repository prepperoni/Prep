#include <vector>
#include "test_framework/generic_test.h"

using std::vector;

vector<int> MatrixInSpiralOrder(vector<vector<int>> square_matrix) {
  if (square_matrix.size() == 0) {
  	return {};
  } else if (square_matrix.size() == 1) {
  	return {square_matrix[0][0]};
  }

  vector<int> result;
  int m_len = square_matrix.size();
  int length = square_matrix.size();
  for (int corner = 0; corner < m_len / 2; ++corner) {
  	for (int l = 0; l < length - 1; ++l) {
  		result.push_back(square_matrix[corner][corner + l]);
  	}
  	for (int l = 0; l < length - 1; ++l) {
  		result.push_back(square_matrix[corner + l][m_len - 1 - corner]);
  	}
  	for (int l = 0; l < length - 1; ++l) {
  		result.push_back(square_matrix[m_len - 1 - corner][m_len - 1 - corner - l]);
  	}
  	for (int l = 0; l < length - 1; ++l) {
  		result.push_back(square_matrix[m_len - 1 - corner - l][corner]);
  	}  	

  	length -= 2;
  }

  if (square_matrix.size() % 2) {
	int mid_idx = m_len / 2;
  	result.push_back(square_matrix[mid_idx][mid_idx]);
  }

  return result;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"square_matrix"};
  return GenericTestMain(args, "spiral_ordering_segments.tsv",
                         &MatrixInSpiralOrder, DefaultComparator{},
                         param_names);
}
