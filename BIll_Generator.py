"""Bill generator for Vohra's movie snacks.

Reads three integers (pizza_count, puffs_count, cooldrink_count) from
standard input (space- or newline-separated) and prints a formatted bill.

Input handling is tolerant: it extracts the first three integers from the
entire input stream. If fewer than three integers are provided, missing
quantities default to 0.

Usage examples:
  echo "2 3 4" | python BIll_Generator.py
  python BIll_Generator.py    # then type numbers and press Ctrl+Z (Windows) / Ctrl+D (Unix)
"""

pizza_count=int(input("Enter number of pizzas: ") or 0)
puffs_count=int(input("Enter number of puffs: ") or 0)
cooldrink_count=int(input("Enter number of cool drinks: ") or 0)    
bill=(pizza_count*100)+(puffs_count*20)+(cooldrink_count*10)
print("Bill Details")
print(f"Number of pizzas: {pizza_count} @ 100 = {pizza_count*100}")
print(f"Number of puffs: {puffs_count} @ 20 = {puffs_count*20}")
print(f"Number of cool drinks: {cooldrink_count} @ 10 = {cooldrink_count*10}")
print(f"Total Bill: {bill}")