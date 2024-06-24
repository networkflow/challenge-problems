// Given an array of integers, returns the length of the longest subarray that
// has all distinct values
//
// Examples:
//   Input: [1, 3, 4, 3, 5, 2, 7]
//   Output: 5
//   (The longest subarray without duplicates is [4, 3, 5, 2, 7]
//   
//   Input: [8, 4, 3, 8, 3, 8, 4]
//   Output: 3
//   (The longest subarrays are [8, 4, 3], [4, 3, 8], or [3, 8, 4] which all
//     have length 3)
//
// Runs in O(n) time
func lengthOfLongestSubarrayWithDistinctValues(_ array: [Int]) -> Int {
  // Algorithm: we will keep track of a subarray and the elements that are in
  // it. The subarray will initially start at the beginning of the array, and
  // then we'll keep adding elements to it until we can't anymore (there would
  // be duplicate elements). If this happens, we'll move the start of the
  // subarray forward by one element and try again.
  //
  // We'll keep repeating until we run out of start indices for the subarray:
  // then we'll return the maximum size we've seen so far.

  var maxLengthSoFar = 0
  var subarrayStartIndex = array.startIndex
  // Subarray is initially empty:
  var subarrayEndIndex = subarrayStartIndex - 1
  var valuesInSubArray: Set<Int> = []

  // Iterate over every possible start index:
  while subarrayStartIndex < array.endIndex {
    // Move the end index as far as possible without introducing duplicates:
    while (
      subarrayEndIndex + 1 < array.endIndex &&
      !valuesInSubArray.contains(array[subarrayEndIndex + 1])
    ) {
      subarrayEndIndex += 1
      valuesInSubArray.insert(array[subarrayEndIndex])
    }
    // We've found the maximum possible subarray with this start index:
    maxLengthSoFar =
      max(maxLengthSoFar, subarrayEndIndex - subarrayStartIndex + 1)

    // Now increment the start index and remove the old value from the values
    // in the subarray:
    valuesInSubArray.remove(array[subarrayStartIndex])
    subarrayStartIndex += 1
  }

  return maxLengthSoFar
}
