from word2number import w2n

# test = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

test = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]

def divByThree(nums):
    for n in nums:
        if w2n.word_to_num(n) % 3 == 0:
            print(n)

divByThree(test)