# Returns the the maximum possible sum of any subarray of the given array
# (empty subarrays are allowed)
#
# This version has O(n) runtime (and still O(n) even if parallelized):
def maxSubarraySumImperative(array: list[int]) -> int:
    # Returns the list of the prefix sums of the array (starts with 0, so will
    # have one more element than the given array):
    def getPrefixSums(array: list[int]) -> list[int]:
        prefixSums = [0]
        currentSum = 0
        for val in array:
            currentSum += val
            prefixSums.append(currentSum)
        return prefixSums
    
    # Returns the maximum possible difference (array[b] - array[a]) for any
    # indices a, b in the array (so the increase from array[a] to array[b] is as
    # large as possible)
    #
    # The given array must be nonempty or it will throw an exception
    def getLargestIncrease(array: list[int]) -> int:
        if len(array) == 0:
            raise Exception('Empty arrays not allowed')
        minArrayValueSoFar = array[0]
        largestIncrease = 0
        for val in array:
            minArrayValueSoFar = min(minArrayValueSoFar, val)
            largestIncrease = max(largestIncrease, val - minArrayValueSoFar)
        return largestIncrease
    
    # The sum of any subarray corresponds to a difference in the relevant prefix
    # sums of the array, so the maximum subarray sum is the maximum possible
    # difference of any two prefix sums:
    return getLargestIncrease(getPrefixSums(array))


from itertools import accumulate
# Returns the the maximum possible sum of any subarray of the given array
# (empty subarrays are allowed)
#
# This version has O(n) runtime (and will improve to O(log n) if completely
# parallelized, unlike the imperative version):
def maxSubarraySumFunctional(array: list[int]) -> int:
    # Returns the maximum possible difference (array[b] - array[a]) for any
    # indices a, b in the array (so the increase from array[a] to array[b] is as
    # large as possible)
    #
    # The given array must be nonempty or it will throw an exception
    def getLargestIncrease(array: list[int]) -> int:
        if len(array) == 0:
            raise Exception('Empty arrays not allowed')
        runningMinimums = accumulate(array, min)
        return max(
            val - minSoFar for val, minSoFar in zip(array, runningMinimums)
        )

    prefixSums = list(accumulate(array, lambda x, y: x + y, initial=0))
    return getLargestIncrease(prefixSums)
