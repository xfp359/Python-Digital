def analyze_text(text):
  letter_counts = {}
  total_letters = 0

  for char in text:
      if char.isalpha() and char.islower():
          letter_counts[char] = letter_counts.get(char, 0) + 1
          total_letters += 1

  frequencies = {}
  for letter, count in letter_counts.items():
      frequency = count / total_letters
      frequencies[letter] = frequency

  return frequencies

# Пример использования:
text = "А роза упала на лапу Азора."
result = analyze_text(text)

for letter, frequency in result.items():
  print(f"{letter}: {frequency:.2f}")
