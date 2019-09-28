//
// Created by Alaric on 2019-09-29.
//
/**
 * Definition of Interval:
 * classs Interval {
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
     * @return: the minimum number of conference rooms required
     */
    int minMeetingRooms(vector<Interval> &intervals) {
        // Write your code here
        map<int,int> hash;
        for(auto val : intervals){
            hash[val.start]++ , hash[val.end]--;
        }
        int sum =0,ans = 0;
        for (auto val:hash)
            sum+=val.second,ans=max(ans,sum);
        return ans;
    }
};
