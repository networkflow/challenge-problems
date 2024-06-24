// Given an array of 0s and 1s, sorts the array:
//
// Runs in O(n) time (faster than regular sort algorithms which are O(n log n)):
export function sortOnesAndZerosImperative(list: (0 | 1)[]): (0 | 1)[] {
  let numZeros = 0;
  for (const value of list) {
    if (value === 0) {
      numZeros++;
    }
  }
  let numOnes = list.length - numZeros;

  let result: (0 | 1)[] = [];
  for (let i = 0; i < numZeros; i++) {
    result.push(0);
  }
  for (let i = 0; i < numOnes; i++) {
    result.push(1);
  }
  return result;
}


// Given an array of 0s and 1s, sorts the array:
//
// Runs in O(n) time (faster than regular sort algorithms which are O(n log n)):
export function sortOnesAndZerosFunctional(list: (0 | 1)[]): (0 | 1)[] {
  const numZeros = (list as number[]).reduce(
    (zerosCount, nextValue) => zerosCount + (nextValue === 0 ? 1 : 0),
    0, // initial value for zerosCount is 0
  );
  return list.map((_, index) => index < numZeros ? 0 : 1);
}
