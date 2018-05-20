#include <vector>
#include <algorithm>

using namespace std;

/*
either is product of largest positive 3, or product of two most negative
and the largest positive 
*/

int highest_product_of_3(const vector<int> A) {
    if (A.size() < 3) {
        throw "needs at least 3 elements";
    }

    int largest_product_of_2 = A[0]*A[1], smallest_product_of_2=A[0]*A[1], largest_product_of_3=A[0]*A[1]*A[2], largest=max(A[0], A[1]), smallest=min(A[0], A[1]);

    for (int i = 2; i < A.size(); i++) {
        int cur = A[i];
        largest_product_of_3 = max(largest_product_of_3, max(cur*largest_product_of_2, cur*smallest_product_of_2));
        largest_product_of_2 = max(largest_product_of_2, max(cur*smallest, cur*largest));
        smallest_product_of_2 = min(smallest_product_of_2, min(cur*smallest, cur*largest));
        largest = max(largest, cur);
        smallest = min(smallest, cur);
    }

    return largest_product_of_3;
}

