//
// Created by Alaric on 2019-09-28.
//
/**
 * Definition of Interval:
 * class Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: if a person could attend all meetings
     */
    bool canAttendMeetings(vector<Interval> &intervals) {
        auto cmp = [](Interval a, Interval b) { return a.start < b.start; };
        sort(intervals.begin() , intervals.end() , cmp);
        for (int i = 1;i<intervals.size();++i){
            if (intervals[i].start < intervals[i-1].end) return false;
        }
        return true;
    }
};
