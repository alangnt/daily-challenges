# Palindrome 🏎️
# Valérie

def check_palindrome(sequence):
  # Write code below 💖
  worky_sequence = sequence.replace(' ', '').lower()
  
  return worky_sequence == worky_sequence[::-1]
