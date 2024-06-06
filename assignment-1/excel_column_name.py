# Get an excel-style column name, given a column number (1-indexed):
# Examples:
#   1 -> A
#   2 -> B
#   ...
#   26 -> Z
#   27 -> AA
#   28 -> AB
#   ...
#   52 -> AZ
#   53 -> BA
#   ...
#   702 -> ZZ
#   703 -> AAA
#   ...
def getExcelColumnName(n: int) -> str:
    # Algorithm:
    # 
    # Our algorithm is based on 2 observations:
    #   1) The last character of the label cycles A-Z, meaning that knowing
    #      n % 26 gives us the last character
    #   2) The characters that come before the last character have the same
    #      pattern as the entire label itself (except they only change every 26 
    #      labels)
    # This means that we can find the last character by computing n % 26, and
    # then iteratively subtract out the appropriate remainder and divide n by 26
    # to repeatedly compute the remaining characters.

    # Given a number 1-26, returns the corresponding letter (A-Z):
    numberToLetter = lambda num: chr(ord('A') - 1 + num)

    label = ''
    while n > 0:
        # remainder of n / 26 from 1 to 26, not 0 to 25
        remainder = (n - 1) % 26 + 1
        label = numberToLetter(remainder) + label
        n = (n - remainder) // 26
    return label
