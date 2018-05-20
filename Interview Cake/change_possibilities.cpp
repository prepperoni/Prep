int changePossibilities(int val, const vector<int>& coins)
{
    auto memo = vector<int>(val+1, 0);
    memo[0] = 1;

    for (const int &c : coins) {
    	for (int i = c; i < val+1; i++) {
    		memo[i] += memo[i-c];
    	}
    }

    return memo[val];
}
