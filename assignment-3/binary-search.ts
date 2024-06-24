// Given a sorted list of numbers and a target number, returns the index of the
// target in the sort list if present, or otherwise null
//
// Runs in O(log n) runtime
export function binarySearchImperative(
  sortedNumbers: number[],
  target: number,
): number | null {
  let lowerBoundInclusive = 0;
  let upperBoundExclusive = sortedNumbers.length;

  while (lowerBoundInclusive < upperBoundExclusive) {
    const midpointIndex = lowerBoundInclusive +
      Math.floor((upperBoundExclusive - 1 - lowerBoundInclusive) / 2);
    if (sortedNumbers[midpointIndex] === target) {
      return midpointIndex
    } else if (target < sortedNumbers[midpointIndex]) {
      upperBoundExclusive = midpointIndex;
    } else {
      lowerBoundInclusive = midpointIndex + 1;
    }
  }

  return null;
}


export function binarySearchFunctional(
  sortedNumbers: number[],
  target: number,
): number | null {
  const binarySearchHelper = (
    lowerBoundInclusive: number,
    upperBoundExclusive: number,
  ): number | null => {
    if (upperBoundExclusive <= lowerBoundInclusive) {
      return null;
    }

    const midpointIndex = lowerBoundInclusive +
      Math.floor((upperBoundExclusive - 1 - lowerBoundInclusive) / 2);
    if (sortedNumbers[midpointIndex] === target) {
      return midpointIndex
    } else if (target < sortedNumbers[midpointIndex]) {
      return binarySearchHelper(lowerBoundInclusive, midpointIndex);
    } else {
      return binarySearchHelper(midpointIndex + 1, upperBoundExclusive);
    }
  };

  return binarySearchHelper(0, sortedNumbers.length);
}
