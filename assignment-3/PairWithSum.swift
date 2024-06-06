func findPairWithSumImperative(numbers: [Int], target: Int) -> (Int, Int)? {
  // Create a dictionary representing how many times each number occurs in the
  // list:
  var numCounts: [Int: Int] = [:]
  for num in numbers {
    numCounts[num] = (numCounts[num] ?? 0) + 1
  }

  for num in numbers {
    if numCounts[target - num] != nil {
      if target - num == num && numCounts[num]! < 2 {
        // Can't use the same number twice:
        continue
      }
      return (num, target - num)
    }
  }
  return nil
}

func findPairWithSumFunctional(numbers: [Int], target: Int) -> (Int, Int)? {
  // Create a dictionary representing how many times each number occurs in the
  // list:
  let numCounts = numbers.reduce(into: [Int: Int]()) {
    (counts, num) in counts[num] = (counts[num] ?? 0) + 1
  }

  return numbers.compactMap {
    switch ($0, target - $0, numCounts[target - $0] ?? 0) {
      // Can't use the same number twice:
      case let (x, y, count) where x == y && count >= 2: return (x, y)
      case let (x, y, count) where x != y && count >= 1: return (x, y)
      default: return nil
    }
  }.first
}
