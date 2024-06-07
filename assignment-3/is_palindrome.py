def isPalindromeImperative(s: str) -> bool:
    # We can check the first len(s) // 2 characters rounded down, since if
    # len(s) is odd we don't need to check the middle character:
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return False
    return True

def isPalindromeFunctional(s: str) -> bool:
    # We can check the first len(s) // 2 characters rounded down, since if
    # len(s) is odd we don't need to check the middle character:
    return all(s[i] == s[-1 - i] for i in range(len(s) // 2))
