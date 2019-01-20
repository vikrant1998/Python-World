class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        import heapq
        q = []
        for point in points:
            dist = (point[0] ** 2 + point[1] ** 2) ** 0.5
            dist *= -1
            if len(q) < K:
                heapq.heappush(q, (dist, point))
            else:
                outDist, outPoint = q[0]
                dist *= -1
                outDist *= -1
                if dist < outDist:
                    heapq.heappop(q)
                    heapq.heappush(q, (dist * -1, point))

        return [i[1] for i in q]

if __name__ == "__main__":
    pts = [[3,3],[5,-1],[-2,4]]
    K = 2
    s = Solution()
    print(s.kClosest(pts, K))