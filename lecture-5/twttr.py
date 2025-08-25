def main():
  print(f"Output: {shorten(input('Input: '))}")
  
def shorten(word):
  str = ""
  for char in word:
      if char in "aeiouAEIOU":
          continue
      str += char
  return str

if __name__ == "__main__":
  main()