class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        for rest in restaurants:
            if veganFriendly == 1 and rest[2] == 0:
                rest[1] = 0
            elif rest[3] > maxPrice or rest[4] > maxDistance:
                rest[1] = 0

        restaurants.sort(key = lambda x:[x[1] , x[0]] , reverse = True)
        res = []
        for rest in restaurants:
            if rest[1]:
                res.append(rest[0])
        return res
                