class TempTracker {
	private:

	int min_temp, max_temp, count, total, mode, modeCount;
	unordered_map<int, int> data;

	public:

	TempTracker() : min_temp(numeric_limits<int>::max()), max_temp(numeric_limits<int>::min()), 
	count(0), total(0), mode(0), modeCount(0) {}

	void insert(int temp) {
		min_temp = min(min_temp, temp);
		max_temp = max(max_temp, temp);
		count++;
		total += temp;
		if (data.find(temp) == data.end()) {
			data[temp] = 1;
		} else {
			data[temp] += 1;
		}

		if (data[temp] > modeCount) {
			modeCount = data[temp];
			mode = temp;
		}
	}

	int getMax() {
		return max_temp;
	}

	int getMin() {
		return min_temp;
	}

	double getMean() {
		return total/(double) count;
	}

	int getMode() {
		return mode;
	}
}