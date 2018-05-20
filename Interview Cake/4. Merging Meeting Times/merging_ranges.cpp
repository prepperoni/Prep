#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Meeting
{
private:
    // number of 30 min blocks past 9:00 am
    unsigned int startTime_;
    unsigned int endTime_;

public:
    Meeting() :
        startTime_(0),
        endTime_(0)
    {
    }

    Meeting(unsigned int startTime, unsigned int endTime) :
        startTime_(startTime),
        endTime_(endTime)
    {
    }

    unsigned int getStartTime() const
    {
        return startTime_;
    }

    void setStartTime(unsigned int startTime)
    {
        startTime_ = startTime;
    }

    unsigned int getEndTime() const
    {
        return endTime_;
    }

    void setEndTime(unsigned int endTime)
    {
        endTime_ = endTime;
    }

    bool operator==(const Meeting& other) const
    {
        return
            startTime_ == other.startTime_
            && endTime_ == other.endTime_;
    }
};

bool compareMeetings(const Meeting &m1, const Meeting &m2) {
    return m1.getStartTime() < m2.getStartTime();
}

vector<Meeting> mergeRanges(const vector<Meeting>& meetings)
{
    // merge meeting ranges
    auto m = vector<Meeting>(meetings);
    auto res = vector<Meeting>();
    sort(m.begin(), m.end(), compareMeetings);

    auto range_start = m[0].getStartTime(), range_end = m[0].getEndTime();

    for (int i = 1; i < m.size(); i++) {
        if (m[i].getStartTime() <= range_end) {
            range_end = max(range_end, m[i].getEndTime());
        } else {
            res.push_back(Meeting(range_start, range_end));
            range_start = m[i].getStartTime();
            range_end = m[i].getEndTime();
        }
    }

    res.push_back(Meeting(range_start, range_end));
    return res;
}


int main(int argc, char** argv)
{
    vector<Meeting> arr = {Meeting(5, 6)};
    mergeRanges(arr);
}