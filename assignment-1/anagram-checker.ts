// Returns whether the given strings a and b are anagrams of each other (i.e.
// they can be formed by rearranging each other's letters):
export function isAnagram(a: string, b: string): boolean {
  return charCountsEqual(
    getCharCounts(a),
    getCharCounts(b),
  )
}

function getCharCounts(s: string): Map<string, number> {
  const charCounts = new Map<string, number>();
  for (const c of s) {
    charCounts.set(c, (charCounts.get(c) ?? 0) + 1);
  }
  return charCounts;
}

function charCountsEqual(
  counts1: Map<string, number>,
  counts2: Map<string, number>,
): boolean {
  const allKeys = [...counts1.keys(), ...counts2.keys()];
  return allKeys.every(c => counts1.get(c) === counts2.get(c));
}
