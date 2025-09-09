import re

class Jar:
  def __init__(self, capacity=12):
      self.capacity = capacity
      self.size = 0

  def __str__(self):
      return f"{self.size} / {self.capacity}"
      # return f"{self.size()} / {self.capacity()}"

  def deposit(self, n):
      total = self.size + n
      if total > self.capacity:
        raise ValueError("Jar is full")

      self.size = total

  def withdraw(self, n):
      total = self.size - n
      if total < 0:
        raise ValueError("Jar is empty")

      self.size = total

  @property
  def capacity(self):
    return self._capacity

  @capacity.setter
  def capacity(self, capacity):
    if not re.search(r"^\d+$", str(capacity)) or not int(capacity) >= 0:
      raise ValueError("Invalid capacity")
    self._capacity = int(capacity)

  @property
  def size(self):
    return self._size
  
  @size.setter
  def size(self, size=0):
    if not re.search(r"^\d+$", str(size)) or not int(size) >= 0:
      raise ValueError("Invalid size")
    self._size = int(size)

def main():
  jar = Jar('50')
  print(jar)

if __name__ == "__main__":
  main()