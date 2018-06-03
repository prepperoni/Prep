#include <stack>
#include <exception>
#include <stdexcept>
#include <iostream>

using namespace std;

class MyQueue {
	stack<int> pushStk;
	stack<int> popStk;

public: 
	void enqueue(int x) {
		pushStk.push(x);
	}

	int dequeue() {
		if (popStk.empty()) {
			if (pushStk.empty()) {
				throw runtime_error("empty queue");
			}

			while (!pushStk.empty()) {
				int topVal = pushStk.top();
				pushStk.pop();
				popStk.push(topVal);
			}
		}

		int topVal = popStk.top();
		popStk.pop();
		return topVal;
	}
};

int main() {
	MyQueue q = MyQueue();

	q.dequeue();
}