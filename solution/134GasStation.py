class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        ans , sum = 0 , 0
        cango = 0
        for i in range(len(gas)):
            cango += gas[i] - cost[i]
            if sum > 0:
                sum += gas[i] - cost[i]
            else:
                sum = gas[i] - cost[i]
                ans = i
        return ans if cango >=0 else -1