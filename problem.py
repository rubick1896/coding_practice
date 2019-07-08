def partition(self, nums, left, right):
    pivot = nums[left]
    i = left
    j = right

    if left > right:
        return

    while (i != j):
        while (nums[j] >= pivot and i < j):
            j -= 1
        while (nums[i] <= pivot  and i < j):
            i += 1

        nums[i], nums[j] = nums[j], nums[i]

    nums[left] = nums[i]
    nums[i] = pivot

    return i

def edit_distance(word1, word2):
    len1 = len(word1);
    len2 = len(word2);
    dp = np.zeros((len1 + 1,len2 + 1))
    for i in range(len1 + 1):
        dp[i][0] = i;     
    for j in range(len2 + 1):
        dp[0][j] = j;
     
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            delta = 0 if word1[i-1] == word2[j-1] else 1
            dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i-1][j] + 1, dp[i][j - 1] + 1))
    return dp[len1][len2]

def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: return mid
            
            if nums[mid] >= nums[low]: # left is in ascending order, '>=' instead of '>'
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else: # right is in ascending order
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1


 def intervalStatistics(self, arr, k):
        # Write your code here.
        size = len(arr)
        count = zeros
        cur_one = 0
        cur_zero = 0

        for i in range(size):
            if arr[i] == 1:
                cur_one -= 1
            else:
                cur_zero -= 1
                count += cur_zero
                next_to_check = i + cur_one + cur_zero
                if next_to_check >= size:
                    return count
                for j in range(next_to_check, size, 1):
                    if cur_one > k:
                        break
                    if arr[j] == 1:
                        cur_one += 1
                    else: #arr[j] == 0
                        cur_zero += 1
        return count

def circle_divide(m, n):
    if n == 1:
        return m
    elif n == 2:
        return m*(m - 1)
    return m* (m - 1)^(n - 1) - circle_divide(m, n-1)


def sample(iterable, n):
    """
    Returns @param n random items from @param iterable.
    """
    reservoir = []
    for t, item in enumerate(iterable):
        if t < n:
            reservoir.append(item)
        else:
            m = random.randint(0,t)
            if m < n:
                reservoir[m] = item
    return reservoir

def uniquePaths(m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0 for col in range(m + 1)] for row in range(n + 1)]
        dp[1][1]  = 1  
        
        for row in range(1, n):
            for col in range(1, m):
                if row == 1 and col == 1:
                    continue
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        
        return dp[n][m]

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[-1][-1] == -1: return 0
        
        # set up cache
        self.grid = grid
        self.memo = {}
        self.N = len(grid)
         
        return max(self.dp(0, 0, 0, 0), 0)
       
    def dp(self, i1, j1, i2, j2):
        # already stored: return
        if (i1, j1, i2, j2) in self.memo: 
            return self.memo[(i1, j1, i2, j2)]
        
        
        # end states: 1. out of grid 2. at the right bottom corner 3. hit a thorn
        N = self.N
        if i1 == N or j1 == N or i2 == N or j2 == N: return -1
        if i1 == N-1 and j1 == N-1 and i2 == N-1 and j2 == N-1: return self.grid[-1][-1]
        if self.grid[i1][j1] == -1 or self.grid[i2][j2] == -1: return -1
        
        # now can take a step in two directions at each end, which amounts to 4
        # combinations in total
        dd = self.dp(i1+1, j1, i2+1, j2)
        dr = self.dp(i1+1, j1, i2, j2+1)
        rd = self.dp(i1, j1+1, i2+1, j2)
        rr = self.dp(i1, j1+1, i2, j2+1)
        maxComb = max([dd, dr, rd, rr])
        
        # find if there is a way to reach the end
        if maxComb == -1:
            out = -1
        else:
            # same cell, can only count this cell once
            if i1 == i2 and j1 == j2:
                out = maxComb + self.grid[i1][j1]
            # different cell, can collect both
            else:
                out = maxComb + self.grid[i1][j1] + self.grid[i2][j2]
        self.memo[(i1, j1, i2, j2)] = out
        return out


def coin(l, k):
    #length = len(l)
    #left, right = 0, length - 1
    max_profit = 0
    for i in range(k):
        cur_profit = get_sum(i, k)
        if cur_profit > max_profit:
            max_profit = cur_profit
    return max_profit

def get_sum(left_k, k):
    return sum(l[:left_k]) + sum(l[-:(k - left_k)])


