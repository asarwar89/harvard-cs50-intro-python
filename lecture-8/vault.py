class Vault:
  def __init__(self, gold, silver, bronze):
    self.gold = gold
    self.silver = silver
    self.bronze = bronze

  def __str__(self):
    return f"Vault (gold={self.gold}, silver={self.silver}, bronze={self.bronze})"
  
  def __add__(self, other):
    gold = self.gold + other.gold
    silver = self.silver + other.silver
    bronze = self.bronze + other.bronze
    return Vault(gold, silver, bronze)
  
harry_vault = Vault(10, 20, 30)
ron_vault = Vault(5, 10, 15)

combined_vault = harry_vault + ron_vault
print(combined_vault)